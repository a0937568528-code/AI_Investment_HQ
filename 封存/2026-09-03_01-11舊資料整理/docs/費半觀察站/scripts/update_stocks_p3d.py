from pathlib import Path
import yfinance as yf

# Save beside the existing Taiwan market data folder.
save_dir = Path(
    r"G:\我的雲端硬碟\Gpt理財\AI_Investment_HQ\09_給Claude\費半觀察站\data\tw_market"
)
save_dir.mkdir(parents=True, exist_ok=True)

# 要抓取的個股清單：(symbol, 中文檔名)
# 第二階段剩餘2檔：旺矽、聖暉皆為上櫃股，需用.TWO而非.TW
stocks = [
    ("6223.TWO", "6223_旺矽"),
    ("5536.TWO", "5536_聖暉"),
]
# 註：2327國巨、2303聯電、8996高力已抓過，此處不重複

print("=" * 60)
print("Taiwan stock data update")
print("=" * 60)

for symbol, name in stocks:
    print(f"Downloading: {symbol} ({name})")
    try:
        df = yf.download(
            symbol,
            period="max",
            interval="1d",
            auto_adjust=True,  # 還原股價：股利/減資已還原回股價，適合長期回測
            progress=False
        )
    except Exception as e:
        print(f"Download failed for {symbol}: {e}")
        continue

    if df is None or df.empty:
        print(f"No data returned for {symbol}.")
        print(f"Please check the Yahoo Finance ticker: {symbol}")
        continue

    # Flatten Yahoo multi-level columns if present.
    if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
        df.columns = df.columns.get_level_values(0)

    filename = save_dir / f"{name}.csv"
    df.to_csv(filename, encoding="utf-8-sig")

    print(f"Completed: {filename}")
    print(f"Rows: {len(df)}")
    print(f"Date range: {df.index.min()} ~ {df.index.max()}")
    print("-" * 60)

print("=" * 60)
print("Only market data updated. No gap calculation or risk-control calculation.")
input("Press Enter to exit...")
