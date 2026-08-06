from pathlib import Path
import yfinance as yf

save_dir = Path(r"G:\我的雲端硬碟\Gpt理財\AI_Investment_HQ\09_給Claude\費半觀察站\data\tw_market")
save_dir.mkdir(parents=True, exist_ok=True)

symbols = [
   "^TWII"
]

for symbol in symbols:
    print(f"下載中：{symbol}")

    df = yf.download(
        symbol,
        period="10y",
        interval="1d",
        auto_adjust=False,
        progress=False
    )

    filename = save_dir / f"{symbol.replace('^','')}.csv"
    df.to_csv(filename)

    print(f"完成：{filename}")

print("全部完成！")