# -*- coding: utf-8 -*-
"""
update_us_indices.py

用途：
    抓取美國主要指數長期日線資料，供「MA21/81＋100/80/80/0」
    新風控模型進行跨市場驗證。

本程式只負責：
    1. 下載資料
    2. 儲存原始日線資料
    3. 不計算缺口
    4. 不計算風控水位
    5. 不做任何模型判定

驗證標的：
    ^SOX   費城半導體指數
    ^NDX   那斯達克100指數
    ^IXIC  那斯達克綜合指數
    ^GSPC  標普500指數
    ^DJI   道瓊工業指數（非AI市場控制組）

資料來源：
    Yahoo Finance（透過 yfinance）

執行方式：
    python scripts\\update_us_indices.py
"""

from pathlib import Path
from datetime import datetime
import sys
import pandas as pd

# ------------------------------------------------------------
# 路徑
# ------------------------------------------------------------

SAVE_DIR = Path(
    r"G:\我的雲端硬碟\Gpt理財\AI_Investment_HQ"
    r"\09_給Claude\費半觀察站\data\us_market"
)

# ------------------------------------------------------------
# 美國指數
# ------------------------------------------------------------

INDICES = {
    "^SOX": "SOX_費城半導體指數.csv",
    "^NDX": "NDX_那斯達克100指數.csv",
    "^IXIC": "IXIC_那斯達克綜合指數.csv",
    "^GSPC": "GSPC_標普500指數.csv",
    "^DJI": "DJI_道瓊工業指數.csv",
}


def download_index(symbol: str) -> pd.DataFrame:
    try:
        import yfinance as yf
    except ImportError:
        print("[錯誤] 尚未安裝 yfinance。")
        print("請執行：pip install yfinance")
        sys.exit(1)

    print(f"\n下載：{symbol}")

    try:
        raw = yf.download(
            symbol,
            period="max",
            interval="1d",
            auto_adjust=False,
            progress=False
        )
    except Exception as e:
        print(f"[錯誤] {symbol} 下載失敗：{e}")
        return pd.DataFrame()

    if raw is None or raw.empty:
        print(f"[錯誤] {symbol} 沒有取得資料。")
        return pd.DataFrame()

    if isinstance(raw.columns, pd.MultiIndex):
        raw.columns = raw.columns.get_level_values(0)

    raw = raw.reset_index()

    # Yahoo Finance 日期欄可能為 Date 或 Datetime
    date_col = "Date" if "Date" in raw.columns else "Datetime"

    required = ["Open", "High", "Low", "Close"]
    missing = [c for c in required if c not in raw.columns]

    if missing:
        print(f"[錯誤] {symbol} 缺少欄位：{missing}")
        return pd.DataFrame()

    df = raw[[date_col] + required].copy()
    df = df.rename(columns={date_col: "日期"})
    df["日期"] = pd.to_datetime(df["日期"], errors="coerce")

    for col in required:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = (
        df.dropna()
          .sort_values("日期")
          .drop_duplicates("日期")
          .reset_index(drop=True)
    )

    return df


def main():
    print("=" * 70)
    print("美國主要指數長期資料更新")
    print("用途：MA21/81＋100/80/80/0 跨市場驗證")
    print(f"執行時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    SAVE_DIR.mkdir(parents=True, exist_ok=True)

    success = 0

    for symbol, filename in INDICES.items():
        df = download_index(symbol)

        if df.empty:
            continue

        output = SAVE_DIR / filename
        df.to_csv(output, index=False, encoding="utf-8-sig")

        print(
            f"完成：{filename} | "
            f"{len(df)}筆 | "
            f"{df['日期'].iloc[0].strftime('%Y-%m-%d')} ~ "
            f"{df['日期'].iloc[-1].strftime('%Y-%m-%d')}"
        )

        success += 1

    print("\n" + "=" * 70)
    print(f"完成：{success}/{len(INDICES)} 個指數")
    print(f"資料位置：{SAVE_DIR}")
    print("=" * 70)
    print("\n注意：本程式只更新收盤資料，不計算缺口，也不產生風控判定。")


if __name__ == "__main__":
    main()
