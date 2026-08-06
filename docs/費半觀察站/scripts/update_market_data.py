# -*- coding: utf-8 -*-
"""
update_market_data.py
用途：抓取費城半導體指數(^SOX)最新資料，套用與《風險優先模型》相同的
缺口(Gap)、均線(MA10/MA20)定義，產出「近半年缺口均線追蹤表」。

v3版變更（2026-08-06）：
修正減碼規則之階段限制bug，同TWII候選腳本v4版——「均線空方確認」
僅為「第二次減碼」之有效觸發條件（僅state==1時有效），不適用於
第三次減碼。詳見TWII候選腳本v4版說明。

【重要定位提醒】
本腳本純屬 Core Layer 輔助觀察指標，資料來源與計算結果
不影響、也不觸發 Risk First Model 的水位動作。
Risk First Model 的水位判斷一律只依台股加權指數(TAIEX)，
與本腳本產出的費半追蹤表完全分開，不可混用。

執行方式：由 更新美股資料.bat 呼叫，或直接執行
    python scripts\\update_market_data.py
"""

import sys
from datetime import datetime
import pandas as pd

YF_TICKER = "^SOX"
OUTPUT_MONTHS = 6
RAW_OUTPUT_PATH = r"G:\我的雲端硬碟\Gpt理財\AI_Investment_HQ\09_給Claude\費半觀察站\data\us_market\SOX.csv"
OUTPUT_PATH = r"G:\我的雲端硬碟\Gpt理財\AI_Investment_HQ\09_給Claude\費半觀察站\data\us_market\SOX_費半_近半年缺口均線追蹤表.csv"

STATE_TOTAL_RATIO = {0: 100, 1: 80, 2: 60, 3: 50}


def fetch_sox_data() -> pd.DataFrame:
    try:
        import yfinance as yf
    except ImportError:
        print("[錯誤] 尚未安裝 yfinance 套件，請先執行：pip install yfinance")
        sys.exit(1)

    try:
        raw = yf.download(YF_TICKER, period="max", interval="1d",
                           auto_adjust=False, progress=False)
    except Exception as e:
        print(f"[錯誤] 無法從 Yahoo Finance 下載資料，請檢查網路連線：{e}")
        sys.exit(1)

    if raw is None or raw.empty:
        print("[錯誤] 下載資料為空，請確認 Yahoo Finance 服務是否正常，或稍後重試。")
        sys.exit(1)

    if isinstance(raw.columns, pd.MultiIndex):
        raw.columns = raw.columns.get_level_values(0)

    df = raw.reset_index()
    df = df.rename(columns={"Date": "Date", "Open": "Open", "High": "High",
                             "Low": "Low", "Close": "Close"})
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date").reset_index(drop=True)
    df = df[["Date", "Open", "High", "Low", "Close"]].dropna()

    return df


def compute_ma(df: pd.DataFrame) -> pd.DataFrame:
    df["MA10"] = df["Close"].rolling(10).mean()
    df["MA20"] = df["Close"].rolling(20).mean()
    return df


def step_down(state: int) -> int:
    return min(state + 1, 3)


def step_up(state: int) -> int:
    return max(state - 1, 0)


def apply_ma_bear_confirm(state: int):
    """均線空方確認僅在state==1時有效，觸發至state=2。"""
    if state == 1:
        return 2, True
    return state, False


def build_gap_ma_table(df: pd.DataFrame, output_months: int) -> pd.DataFrame:
    track_dir = None
    gap_count = 0
    gap_benchmark = None
    bull_observation = False
    state = 0

    rows = []
    for i in range(1, len(df)):
        prev = df.iloc[i - 1]
        cur = df.iloc[i]
        events = []

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
                if not prev_bull:
                    events.append("均線多方確認(新)")
                    state = step_up(state)
                    bull_observation = False
                    events.append(f"候選:均線多方確認→回補一階 → State{state}")
            elif cur["Close"] < cur["MA10"] and cur["Close"] < cur["MA20"]:
                ma_status = "空方確認"
                if not prev_bear:
                    events.append("均線空方確認(新)")
                    new_state, triggered = apply_ma_bear_confirm(state)
                    if triggered:
                        state = new_state
                        events.append(f"候選:均線空方確認→第二次減碼觸發 → State{state}")
                    else:
                        events.append(f"（均線空方確認於State{state}非有效觸發條件，不改變水位）")
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
    print("=" * 60)
    print("費半(SOX)缺口/均線追蹤表 更新程式 v3")
    print(f"執行時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print("\n【重要提醒】本表僅為Core Layer輔助觀察，不觸發任何水位動作，")
    print("            不得作為Risk First Model之判定依據。\n")

    import os

    print("[1/5] 從 Yahoo Finance 下載費半歷史資料...")
    df = fetch_sox_data()
    print(f"      取得 {len(df)} 筆資料，最新日期：{df['Date'].iloc[-1].strftime('%Y-%m-%d')}")

    print(f"[2/5] 儲存原始資料至 {RAW_OUTPUT_PATH} ...")
    os.makedirs(os.path.dirname(RAW_OUTPUT_PATH), exist_ok=True)
    df.to_csv(RAW_OUTPUT_PATH, index=False, encoding="utf-8-sig")

    print("[3/5] 計算 MA10 / MA20...")
    df = compute_ma(df)

    print("[4/5] 套用缺口/均線定義，逐日推算追蹤狀態（逐階狀態機，不簡化跳階）...")
    out = build_gap_ma_table(df, OUTPUT_MONTHS)

    print(f"[5/5] 輸出追蹤表至 {OUTPUT_PATH} ...")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    out.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")

    latest = out.iloc[-1]
    print("\n" + "=" * 60)
    print("目前最新狀態摘要（Core Layer輔助觀察，不觸發水位動作）")
    print("=" * 60)
    print(f"日期：{latest['日期']}")
    print(f"收盤：{latest['收盤']}　MA10：{latest['MA10']}　MA20：{latest['MA20']}")
    print(f"均線狀態：{latest['均線狀態']}")
    print(f"追蹤方向：{latest['追蹤方向']}　追蹤中缺口數：{latest['追蹤中缺口數']}　"
          f"缺口回補基準值：{latest['缺口回補基準值']}")
    print(f"候選State：{latest['候選State']}（候選總持股比例：{latest['候選總持股比例']}）")
    if latest["當日事件"]:
        print(f"當日事件：{latest['當日事件']}")
    print("=" * 60)
    print(f"\n完成，共輸出 {len(out)} 筆（近{OUTPUT_MONTHS}個月）。")


if __name__ == "__main__":
    main()