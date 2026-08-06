# -*- coding: utf-8 -*-
"""
calc_twii_gap_ma.py
用途：讀取 update_tw.py 已下載的台股加權指數(^TWII)資料，套用
《風險優先模型_v1.0_正式規格書》第4、8節之缺口/均線定義，
逐日計算「候選判斷結果」（缺口狀態、均線狀態、依規則應處於的水位）。

【重要定位提醒 — 請務必詳讀】
本腳本輸出僅為「候選判斷」，不會、也不應該自動寫入
Risk First Model 的《每日執行紀錄》正式檔案。

依 CIO 於 2026/08/04 核可之工作流程：
    風控師（人工）先完成當日OHLC＋缺口/均線/事件/水位判斷 → 交給Claude
    → Claude僅做「規格書一致性核對」，非重新從頭計算
    → 核對無誤才存入 Drive 每日執行紀錄檔
    → 若判斷與規格書SOP不符則提出疑義，不逕自照收

本腳本的角色是：提供一份「機器算好的候選答案」，
供風控師人工判斷時參考比對、或供Claude事後做一致性核對時的輔助依據，
不能取代風控師本人的每日判斷步驟，也不能被視為已核可寫入
每日執行紀錄的正式結果。是否要調整此工作流程（例如改成機器先算、
人工只需核對機器結果），屬於治理層級的SOP變更，須另外經CIO正式核可，
本腳本本身不預設任何工作流程異動。

前提：先執行 update_tw.py，確保
    D:\\AI_Investment_HQ\\data\\tw_market\\TWII.csv
已存在且為最新資料。

執行方式：
    python scripts\\calc_twii_gap_ma.py
"""

import sys
from pathlib import Path
from datetime import datetime
import pandas as pd

# ============================================================
# 參數設定
# ============================================================
INPUT_PATH = Path(r"D:\AI_Investment_HQ\data\tw_market\TWII.csv")
OUTPUT_MONTHS = 6
OUTPUT_PATH = Path(r"D:\AI_Investment_HQ\data\tw_market\TWII_缺口均線候選判斷表.csv")

# 核心倉/機動倉比例（依規格書第6、7節，Official V1固定值）
CORE_RATIO = 50       # 核心倉固定50%
STATE_TOTAL_RATIO = {0: 100, 1: 80, 2: 60, 3: 50}  # State 0~3對應總持股比例


def load_twii_data() -> pd.DataFrame:
    """讀取 update_tw.py 產出的 TWII.csv"""
    if not INPUT_PATH.exists():
        print(f"[錯誤] 找不到 {INPUT_PATH}")
        print("       請先執行 update_tw.py 下載最新台股加權資料。")
        sys.exit(1)

    df = pd.read_csv(INPUT_PATH, skiprows=[1, 2]) if _needs_skip(INPUT_PATH) else pd.read_csv(INPUT_PATH)

    # 統一欄位名稱（yfinance標準輸出應為 Date,Open,High,Low,Close,Adj Close,Volume）
    cols_lower = {c.lower(): c for c in df.columns}
    rename_map = {}
    for target in ["date", "open", "high", "low", "close"]:
        if target in cols_lower:
            rename_map[cols_lower[target]] = target.capitalize()
    df = df.rename(columns=rename_map)

    if "Date" not in df.columns:
        # 有些yfinance輸出把日期放在index欄位，欄名可能是 "Price" 或 "Unnamed: 0"
        first_col = df.columns[0]
        df = df.rename(columns={first_col: "Date"})

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])
    df = df.sort_values("Date").reset_index(drop=True)
    df = df[["Date", "Open", "High", "Low", "Close"]].dropna()
    for c in ["Open", "High", "Low", "Close"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.dropna()

    return df


def _needs_skip(path: Path) -> bool:
    """判斷CSV開頭是否有yfinance新版MultiIndex的多餘標頭列"""
    with open(path, encoding="utf-8") as f:
        second_line = f.readlines()[1] if True else ""
    return second_line.strip().lower().startswith("ticker")


def compute_ma(df: pd.DataFrame) -> pd.DataFrame:
    df["MA10"] = df["Close"].rolling(10).mean()
    df["MA20"] = df["Close"].rolling(20).mean()
    return df


def build_candidate_table(df: pd.DataFrame, output_months: int) -> pd.DataFrame:
    """
    依規格書第4、7、8、9、10節定義，逐日推算：
    - 缺口事件（向上/向下、第幾個同向）
    - 缺口回補（收盤確認制）
    - 均線確認（多方/空方）
    - 依此推導「候選State」（僅供參考，非正式水位）

    候選State邏輯（對應規格書第9、10節事件觸發規則）：
    - State從0起算（100%滿倉）
    - 第一個反向(空方)缺口 → State+1（上限3）
    - 均線空方確認 或 第二個同向(空方)缺口 → State+1（上限3，若尚未因第一個反向缺口升過一階則视为一次性跳2階，此為簡化近似，正式判斷仍須人工依規格書逐步核對）
    - 第三個同向(空方)缺口 → State=3
    - 空方缺口回補（趨勢失敗）→ State-1（棘輪式，下限0）
    - 均線多方確認 或 第二個同向(多方)缺口 → State-1（棘輪式回補，下限0）
    """
    up_gap_tracked = None
    down_gap_tracked = None
    up_gap_count = 0
    down_gap_count = 0
    state = 0  # 初始假設滿倉；僅為腳本內部推算基準，非正式起點

    rows = []
    for i in range(1, len(df)):
        prev = df.iloc[i - 1]
        cur = df.iloc[i]
        events = []

        # 新缺口判定
        if cur["Low"] > prev["High"]:
            up_gap_count += 1
            up_gap_tracked = prev["High"]
            events.append(f"向上缺口(第{up_gap_count}個,下緣{prev['High']:.0f})")
            down_gap_count = 0
            down_gap_tracked = None

        if cur["High"] < prev["Low"]:
            down_gap_count += 1
            down_gap_tracked = prev["Low"]
            events.append(f"向下缺口(第{down_gap_count}個,上緣{prev['Low']:.0f})")
            up_gap_count = 0
            up_gap_tracked = None

            # 減碼觸發（候選判斷）
            if down_gap_count == 1:
                state = min(state + 1, 3)
                events.append(f"候選:第一次減碼觸發 → State{state}")
            elif down_gap_count == 2:
                state = min(max(state, 2), 3)
                events.append(f"候選:第二次減碼觸發(第二個同向缺口) → State{state}")
            elif down_gap_count >= 3:
                state = 3
                events.append(f"候選:第三次減碼觸發(第三個同向缺口) → State{state}")

        # 缺口回補判定（收盤確認制）
        if up_gap_tracked is not None and cur["Close"] <= up_gap_tracked:
            events.append("向上缺口回補")
            up_gap_tracked = None
            up_gap_count = 0

        if down_gap_tracked is not None and cur["Close"] >= down_gap_tracked:
            events.append("向下缺口回補(趨勢失敗)")
            if state > 0:
                state -= 1
                events.append(f"候選:棘輪回升一階 → State{state}")
            down_gap_tracked = None
            down_gap_count = 0

        # 均線確認判定
        ma_status = "中性"
        if pd.notna(cur["MA10"]) and pd.notna(cur["MA20"]):
            prev_bull = pd.notna(prev["MA10"]) and pd.notna(prev["MA20"]) and \
                prev["Close"] > prev["MA10"] and prev["Close"] > prev["MA20"]
            prev_bear = pd.notna(prev["MA10"]) and pd.notna(prev["MA20"]) and \
                prev["Close"] < prev["MA10"] and prev["Close"] < prev["MA20"]

            if cur["Close"] > cur["MA10"] and cur["Close"] > cur["MA20"]:
                ma_status = "多方確認"
                if not prev_bull:
                    events.append("均線多方確認(新)")
                    if state > 0:
                        state -= 1
                        events.append(f"候選:均線多方確認回補一階 → State{state}")
            elif cur["Close"] < cur["MA10"] and cur["Close"] < cur["MA20"]:
                ma_status = "空方確認"
                if not prev_bear:
                    events.append("均線空方確認(新)")
                    state = min(max(state, 2), 3)
                    events.append(f"候選:均線空方確認觸發減碼 → State{state}")

        total_ratio = STATE_TOTAL_RATIO[state]

        rows.append({
            "日期": cur["Date"].strftime("%Y-%m-%d"),
            "開盤": round(cur["Open"], 2),
            "最高": round(cur["High"], 2),
            "最低": round(cur["Low"], 2),
            "收盤": round(cur["Close"], 2),
            "MA10": round(cur["MA10"], 2) if pd.notna(cur["MA10"]) else "",
            "MA20": round(cur["MA20"], 2) if pd.notna(cur["MA20"]) else "",
            "均線狀態": ma_status,
            "多方追蹤中缺口數": up_gap_count,
            "空方追蹤中缺口數": down_gap_count,
            "候選State": state,
            "候選總持股比例": f"{total_ratio}%",
            "當日事件": "；".join(events) if events else "",
        })

    full = pd.DataFrame(rows)
    full["_date_obj"] = pd.to_datetime(full["日期"])
    cutoff = full["_date_obj"].max() - pd.DateOffset(months=output_months)
    out = full[full["_date_obj"] >= cutoff].drop(columns=["_date_obj"]).reset_index(drop=True)
    return out


def main():
    print("=" * 70)
    print("台股加權指數(TWII) 缺口/均線候選判斷表 產生程式")
    print(f"執行時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    print("\n【重要提醒】本腳本輸出僅為候選判斷，不等同於正式《每日執行紀錄》。")
    print("            正式流程仍須風控師人工判斷、Claude做規格書一致性核對後才存檔。\n")

    print("[1/3] 讀取台股加權指數資料...")
    df = load_twii_data()
    print(f"      取得 {len(df)} 筆資料，最新日期：{df['Date'].iloc[-1].strftime('%Y-%m-%d')}")

    print("[2/3] 計算 MA10 / MA20...")
    df = compute_ma(df)

    print("[3/3] 套用缺口/均線定義，逐日推算候選判斷...")
    out = build_candidate_table(df, OUTPUT_MONTHS)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")
    print(f"\n輸出至：{OUTPUT_PATH}")

    latest = out.iloc[-1]
    print("\n" + "=" * 70)
    print("最新一日候選判斷摘要")
    print("=" * 70)
    print(f"日期：{latest['日期']}")
    print(f"收盤：{latest['收盤']}　MA10：{latest['MA10']}　MA20：{latest['MA20']}")
    print(f"均線狀態：{latest['均線狀態']}")
    print(f"多方追蹤中缺口數：{latest['多方追蹤中缺口數']}　"
          f"空方追蹤中缺口數：{latest['空方追蹤中缺口數']}")
    print(f"候選State：{latest['候選State']}（候選總持股比例：{latest['候選總持股比例']}）")
    if latest["當日事件"]:
        print(f"當日事件：{latest['當日事件']}")
    print("=" * 70)
    print("\n※ 此為候選判斷，正式水位仍須依《每日執行紀錄》既定流程人工確認。")
    print(f"\n完成，共輸出 {len(out)} 筆（近{OUTPUT_MONTHS}個月）。")


if __name__ == "__main__":
    main()
