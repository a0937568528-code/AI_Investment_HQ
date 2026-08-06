# -*- coding: utf-8 -*-
"""
calc_twii_gap_ma.py
用途：讀取 update_tw.py 已下載的台股加權指數(^TWII)資料，套用
《風險優先模型_v1.0.4_正式規格書》第4、7、8、9、10節之缺口/均線/
狀態機定義，逐日計算「候選判斷結果」（缺口狀態、均線狀態、依規則
應處於的水位）。

v4版變更（2026-08-06）：
修正減碼規則之階段限制bug。依規格書第9節，「均線空方確認」僅為
「第二次減碼（80%→60%，即State1→State2）」之有效觸發條件，
不適用於第三次減碼（60%→50%）；第三次減碼僅能由「第三個同向缺口」
觸發。v3版錯誤地讓均線空方確認在任何State下都能再減碼一階，
導致候選State在State2之後又被均線確認多減了一階，與官方回補規則
表不符。本版修正為：均線空方確認僅在state==1時才轉移至state=2，
其餘狀態下均線空方確認不產生任何狀態轉移效果。
均線多方確認（回補方向）不受此限制，依規格書第10節三個回補階段
皆適用均線多方確認觸發，維持原邏輯不變。

【重要定位提醒 — 請務必詳讀】
本腳本輸出僅為「候選判斷」，供順手查看／核對比對用，
不會、也不應該自動寫入 Risk First Model 的《每日執行紀錄》正式檔案。
正式每日判定仍須由風控師（GPT）依v1.0.4 SOP完整執行，本腳本結果
僅供事後核對比對參考。

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
INPUT_PATH = Path(r"G:\我的雲端硬碟\Gpt理財\AI_Investment_HQ\09_給Claude\費半觀察站\data\tw_market\TWII.csv")
OUTPUT_MONTHS = 6
OUTPUT_PATH = Path(r"G:\我的雲端硬碟\Gpt理財\AI_Investment_HQ\09_給Claude\費半觀察站\data\tw_market\TWII_缺口均線候選判斷表.csv")

# Cold Start起點：官方多頭「逐日事件與水位」CSV開始追蹤之日
COLD_START_DATE = pd.Timestamp("2025-07-22")

STATE_TOTAL_RATIO = {0: 100, 1: 80, 2: 60, 3: 50}


def load_twii_data() -> pd.DataFrame:
    if not INPUT_PATH.exists():
        print(f"[錯誤] 找不到 {INPUT_PATH}")
        print("       請先執行 update_tw.py 下載最新台股加權資料。")
        sys.exit(1)

    df = pd.read_csv(INPUT_PATH, skiprows=[1, 2]) if _needs_skip(INPUT_PATH) else pd.read_csv(INPUT_PATH)

    cols_lower = {c.lower(): c for c in df.columns}
    rename_map = {}
    for target in ["date", "open", "high", "low", "close"]:
        if target in cols_lower:
            rename_map[cols_lower[target]] = target.capitalize()
    df = df.rename(columns=rename_map)

    if "Date" not in df.columns:
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
    with open(path, encoding="utf-8") as f:
        second_line = f.readlines()[1] if True else ""
    return second_line.strip().lower().startswith("ticker")


def compute_ma(df: pd.DataFrame) -> pd.DataFrame:
    df["MA10"] = df["Close"].rolling(10).mean()
    df["MA20"] = df["Close"].rolling(20).mean()
    return df


def step_down(state: int) -> int:
    """減碼一階，上限State3，用於缺口觸發（第一/二/三個同向缺口）。"""
    return min(state + 1, 3)


def step_up(state: int) -> int:
    """回補一階，下限State0，用於缺口回補與均線多方確認。"""
    return max(state - 1, 0)


def apply_ma_bear_confirm(state: int) -> tuple[int, bool]:
    """
    均線空方確認：依第9節，僅為「第二次減碼」之有效觸發條件，
    僅在state==1（80%）時才轉移至state=2（60%）。
    其餘狀態（0、2、3）均線空方確認不產生任何轉移效果。
    """
    if state == 1:
        return 2, True
    return state, False


def build_candidate_table(df: pd.DataFrame, output_months: int, cold_start: pd.Timestamp) -> pd.DataFrame:
    track_dir = None
    gap_count = 0
    gap_benchmark = None
    bull_observation = False
    state = 0

    rows = []
    for i in range(1, len(df)):
        prev = df.iloc[i - 1]
        cur = df.iloc[i]

        if cur["Date"] < cold_start:
            continue

        events = []
        is_cold_start_day = cur["Date"] == cold_start

        if is_cold_start_day:
            events.append("Cold Start起點（State歸零重新計算，此日前訊號不追認）")

        new_up_gap = cur["Low"] > prev["High"]
        new_down_gap = cur["High"] < prev["Low"]

        if new_down_gap:
            if track_dir != "down":
                track_dir = "down"
                gap_count = 0
                bull_observation = False
            gap_count += 1
            gap_benchmark = prev["Low"]
            events.append(f"向下缺口(第{gap_count}個,上緣{gap_benchmark:.0f})")

            state = step_down(state)
            if gap_count == 1:
                events.append(f"候選:第一個反向缺口→第一次減碼一階 → State{state}")
            elif gap_count == 2:
                events.append(f"候選:第二個同向缺口→減碼一階 → State{state}")
            else:
                events.append(f"候選:第三個以上同向缺口→減碼一階 → State{state}")

        elif new_up_gap:
            if track_dir != "up":
                is_first_reversal = track_dir == "down"
                track_dir = "up"
                gap_count = 0
                bull_observation = is_first_reversal
            gap_count += 1
            gap_benchmark = prev["High"]
            events.append(f"向上缺口(第{gap_count}個,下緣{gap_benchmark:.0f})")

            if gap_count == 1:
                events.append("候選:第一個多方反向缺口→僅進入觀察期，水位不變")
            else:
                state = step_up(state)
                bull_observation = False
                events.append(f"候選:第二個同向多方缺口→回補一階 → State{state}")

        if track_dir == "down" and gap_benchmark is not None and cur["Close"] >= gap_benchmark:
            events.append("空方缺口回補(收盤確認)")
            state = step_up(state)
            events.append(f"候選:空方缺口回補→趨勢失敗，回升一階 → State{state}")
            track_dir, gap_count, gap_benchmark = None, 0, None

        elif track_dir == "up" and gap_benchmark is not None and cur["Close"] <= gap_benchmark:
            events.append("多方缺口回補(收盤確認)")
            events.append("候選:多方缺口回補→僅重置追蹤，不影響水位")
            track_dir, gap_count, gap_benchmark = None, 0, None
            bull_observation = False

        ma_status = "中性"
        if pd.notna(cur["MA10"]) and pd.notna(cur["MA20"]):
            prev_bull = pd.notna(prev["MA10"]) and pd.notna(prev["MA20"]) and \
                prev["Close"] > prev["MA10"] and prev["Close"] > prev["MA20"]
            prev_bear = pd.notna(prev["MA10"]) and pd.notna(prev["MA20"]) and \
                prev["Close"] < prev["MA10"] and prev["Close"] < prev["MA20"]

            if cur["Close"] > cur["MA10"] and cur["Close"] > cur["MA20"]:
                ma_status = "多方確認"
                if not prev_bull and not is_cold_start_day:
                    events.append("均線多方確認(新)")
                    state = step_up(state)
                    bull_observation = False
                    events.append(f"候選:均線多方確認→回補一階 → State{state}")
            elif cur["Close"] < cur["MA10"] and cur["Close"] < cur["MA20"]:
                ma_status = "空方確認"
                if not prev_bear and not is_cold_start_day:
                    events.append("均線空方確認(新)")
                    new_state, triggered = apply_ma_bear_confirm(state)
                    if triggered:
                        state = new_state
                        events.append(f"候選:均線空方確認→第二次減碼觸發 → State{state}")
                    else:
                        events.append(f"（均線空方確認於State{state}非有效觸發條件，依第9節僅State1適用，不改變水位）")
            else:
                if track_dir is not None and gap_benchmark is not None:
                    events.append("均線退回中性，追蹤中缺口未回補→盤整中")

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
            "追蹤方向": track_dir if track_dir else "",
            "追蹤中缺口數": gap_count,
            "缺口回補基準值": round(gap_benchmark, 2) if gap_benchmark is not None else "",
            "多方觀察期中": "是" if bull_observation else "",
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
    print("台股加權指數(TWII) 缺口/均線候選判斷表 產生程式 v4")
    print(f"執行時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Cold Start起點：{COLD_START_DATE.strftime('%Y-%m-%d')}（State自此日歸零重新計算）")
    print("=" * 70)
    print("\n【重要提醒】本腳本輸出僅為候選判斷／核對比對用，不等同於正式《每日執行紀錄》。")
    print("            正式流程仍須風控師依v1.0.4 SOP人工判斷後才存檔。\n")

    print("[1/3] 讀取台股加權指數資料...")
    df = load_twii_data()
    print(f"      取得 {len(df)} 筆資料，最新日期：{df['Date'].iloc[-1].strftime('%Y-%m-%d')}")

    print("[2/3] 計算 MA10 / MA20（使用完整歷史資料暖身）...")
    df = compute_ma(df)

    print("[3/3] 套用缺口/均線定義，自Cold Start起點逐日推算候選判斷...")
    out = build_candidate_table(df, OUTPUT_MONTHS, COLD_START_DATE)

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
    print(f"追蹤方向：{latest['追蹤方向']}　追蹤中缺口數：{latest['追蹤中缺口數']}　"
          f"缺口回補基準值：{latest['缺口回補基準值']}")
    print(f"候選State：{latest['候選State']}（候選總持股比例：{latest['候選總持股比例']}）")
    if latest["當日事件"]:
        print(f"當日事件：{latest['當日事件']}")
    print("=" * 70)
    print("\n※ 此為候選判斷，正式水位仍須依《每日執行紀錄》既定流程人工確認。")
    print(f"\n完成，共輸出 {len(out)} 筆（Cold Start起點{COLD_START_DATE.strftime('%Y-%m-%d')}至今）。")


if __name__ == "__main__":
    main()