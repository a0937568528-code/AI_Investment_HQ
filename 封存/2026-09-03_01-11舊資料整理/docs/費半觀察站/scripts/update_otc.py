from pathlib import Path
import yfinance as yf

# Save beside the existing Taiwan market data folder.
save_dir = Path(
    r"G:\我的雲端硬碟\Gpt理財\AI_Investment_HQ\09_給Claude\費半觀察站\data\tw_market"
)
save_dir.mkdir(parents=True, exist_ok=True)

# Yahoo Finance: Taipei Exchange / OTC index
symbol = "^TWOII"

print("=" * 60)
print("Taiwan OTC Index data update")
print("=" * 60)
print(f"Downloading: {symbol}")

try:
    df = yf.download(
        symbol,
        period="max",
        interval="1d",
        auto_adjust=False,
        progress=False
    )
except Exception as e:
    print(f"Download failed: {e}")
    input("Press Enter to exit...")
    raise SystemExit(1)

if df is None or df.empty:
    print("No data returned.")
    print("Please check the Yahoo Finance ticker: ^TWOII")
    input("Press Enter to exit...")
    raise SystemExit(1)

# Flatten Yahoo multi-level columns if present.
if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
    df.columns = df.columns.get_level_values(0)

filename = save_dir / "TWOII_櫃買指數.csv"
df.to_csv(filename, encoding="utf-8-sig")

print(f"Completed: {filename}")
print(f"Rows: {len(df)}")
print(f"Date range: {df.index.min()} ~ {df.index.max()}")
print("=" * 60)
print("Only market data updated. No gap calculation or risk-control calculation.")
input("Press Enter to exit...")
