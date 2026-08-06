# -*- coding: utf-8 -*-
"""
update_market_data.py
用途：抓取費城半導體指數(^SOX)最新資料，套用與《風險優先模型》相同的
缺口(Gap)、均線(MA10/MA20)定義，產出「近半年缺口均線追蹤表」。

【重要定位提醒】
本腳本純屬 Core Layer 輔助觀察指標，資料來源與計算結果
不影響、也不觸發 Risk First Model 的水位動作。
Risk First Model 的水位判斷一律只依台股加權指數(TAIEX)，
與本腳本產出的費半追蹤表完全分開，不可混用。

資料來源：Yahoo Finance（透過 yfinance 套件下載，免登入、免API Key，
套件會自動處理 Yahoo 端的驗證機制，比自行組網址請求穩定）。

執行方式：由 更新美股資料.bat 呼叫，或直接執行
    python scripts\\update_market_data.py
"""

import sys
from datetime import datetime
import pandas as pd

# ============================================================
# 參數設定（可依需求調整）
# ============================================================
YF_TICKER = "^SOX"
OUTPUT_MONTHS = 6  # 輸出近幾個月的追蹤表
RAW_OUTPUT_PATH = r"D:\AI_Investment_HQ\data\us_market\SOX.csv"
OUTPUT_PATH = r"D:\AI_Investment_HQ\data\us_market\SOX_費半_近半年缺口均線追蹤表.csv"
# 若你的資料夾結構不同，只需修改上面這兩個路徑即可


def fetch_sox_data() -> pd.DataFrame:
    """
    透過 yfinance 套件下載費半(^SOX)完整歷史日K資料。
    改用 yfinance 而非直接組網址請求，是因為 Yahoo/Stooq 的下載端點
    經常變動或需要驗證，yfinance套件會自動處理這些細節，較穩定。

    首次執行前請先安裝套件：
        pip install yfinance
    """
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
        print("[錯誤] 下載資料為空，請確認 Yahoo Finance 服務是否正常，"
              "或稍後重試。")
        sys.exit(1)

    # yfinance新版可能回傳多層欄位(MultiIndex)，統一攤平
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
    """計算 MA10 / MA20（以收盤價為準）"""
    df["MA10"] = df["Close"].rolling(10).mean()
    df["MA20"] = df["Close"].rolling(20).mean()
    return df


def build_gap_ma_table(df: pd.DataFrame, output_months: int) -> pd.DataFrame:
    """
    套用《風險優先模型》缺口/均線定義（僅作觀察，不觸發水位）：
    - 向上缺口：當日最低價 > 前一日最高價
    - 向下缺口：當日最高價 < 前一日最低價
    - 缺口回補（收盤確認制）：
        向上缺口：收盤價 ≤ 缺口下緣（前一日最高價）
        向下缺口：收盤價 ≥ 缺口上緣（前一日最低價）
    - 均線確認：收盤價同時高於/低於 MA10 與 MA20
    為確保追蹤連續性正確，一律從完整歷史資料開始逐日推算，
    最後再截取近 output_months 個月輸出。
    """
    up_gap_tracked = None
    down_gap_tracked = None
    up_gap_count = 0
    down_gap_count = 0

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

        # 缺口回補判定（收盤確認制）
        if up_gap_tracked is not None and cur["Close"] <= up_gap_tracked:
            events.append("向上缺口回補")
            up_gap_tracked = None
            up_gap_count = 0

        if down_gap_tracked is not None and cur["Close"] >= down_gap_tracked:
            events.append("向下缺口回補")
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
            elif cur["Close"] < cur["MA10"] and cur["Close"] < cur["MA20"]:
                ma_status = "空方確認"
                if not prev_bear:
                    events.append("均線空方確認(新)")

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
            "當日事件": "；".join(events) if events else "",
        })

    full = pd.DataFrame(rows)
    full["_date_obj"] = pd.to_datetime(full["日期"])
    cutoff = full["_date_obj"].max() - pd.DateOffset(months=output_months)
    out = full[full["_date_obj"] >= cutoff].drop(columns=["_date_obj"]).reset_index(drop=True)
    return out


def main():
    print("=" * 60)
    print(f"費半(SOX)缺口/均線追蹤表 更新程式")
    print(f"執行時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    import os

    print("\n[1/5] 從 Yahoo Finance 下載費半歷史資料...")
    df = fetch_sox_data()
    print(f"      取得 {len(df)} 筆資料，最新日期：{df['Date'].iloc[-1].strftime('%Y-%m-%d')}")

    print(f"[2/5] 儲存原始資料至 {RAW_OUTPUT_PATH} ...")
    os.makedirs(os.path.dirname(RAW_OUTPUT_PATH), exist_ok=True)
    df.to_csv(RAW_OUTPUT_PATH, index=False, encoding="utf-8-sig")

    print("[3/5] 計算 MA10 / MA20...")
    df = compute_ma(df)

    print("[4/5] 套用缺口/均線定義，逐日推算追蹤狀態...")
    out = build_gap_ma_table(df, OUTPUT_MONTHS)

    print(f"[5/5] 輸出追蹤表至 {OUTPUT_PATH} ...")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    out.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")

    # 顯示目前最新狀態摘要
    latest = out.iloc[-1]
    print("\n" + "=" * 60)
    print("目前最新狀態摘要（Core Layer輔助觀察，不觸發水位動作）")
    print("=" * 60)
    print(f"日期：{latest['日期']}")
    print(f"收盤：{latest['收盤']}　MA10：{latest['MA10']}　MA20：{latest['MA20']}")
    print(f"均線狀態：{latest['均線狀態']}")
    print(f"多方追蹤中缺口數：{latest['多方追蹤中缺口數']}　"
          f"空方追蹤中缺口數：{latest['空方追蹤中缺口數']}")
    if latest["當日事件"]:
        print(f"當日事件：{latest['當日事件']}")
    print("=" * 60)
    print(f"\n完成，共輸出 {len(out)} 筆（近{OUTPUT_MONTHS}個月）。")


if __name__ == "__main__":
    main()
