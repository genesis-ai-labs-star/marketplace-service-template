import argparse
from dataclasses import dataclass
from typing import List

import pandas as pd
import yfinance as yf

TICKERS = ["NVDA", "AVGO", "VST", "CEG"]


@dataclass
class BacktestConfig:
    tickers: List[str]
    start: str
    end: str
    initial_capital: float = 100_000.0


def download_prices(tickers: List[str], start: str, end: str) -> pd.DataFrame:
    data = yf.download(tickers, start=start, end=end)["Adj Close"]
    if isinstance(data, pd.Series):
        data = data.to_frame()
    return data.dropna(how="all")


def equal_weight_backtest(prices: pd.DataFrame, initial_capital: float) -> pd.DataFrame:
    returns = prices.pct_change().fillna(0.0)
    n = len(prices.columns)
    weights = pd.Series(1 / n, index=prices.columns)
    daily_portfolio_ret = (returns * weights).sum(axis=1)
    equity_curve = (1 + daily_portfolio_ret).cumprod() * initial_capital

    stats = {
        "start": equity_curve.index[0],
        "end": equity_curve.index[-1],
        "final_equity": equity_curve.iloc[-1],
        "total_return": equity_curve.iloc[-1] / initial_capital - 1,
        "max_drawdown": ((equity_curve.cummax() - equity_curve) / equity_curve.cummax()).max(),
    }

    result = pd.DataFrame({"equity": equity_curve})
    for k, v in stats.items():
        result.attrs[k] = v
    return result


def main():
    parser = argparse.ArgumentParser(description="AI rotation baseline backtest (equal-weight buy & hold)")
    parser.add_argument("--start", type=str, default="2020-01-01")
    parser.add_argument("--end", type=str, default="2024-12-31")
    parser.add_argument("--initial_capital", type=float, default=100_000.0)

    args = parser.parse_args()

    cfg = BacktestConfig(tickers=TICKERS, start=args.start, end=args.end, initial_capital=args.initial_capital)

    print(f"Downloading prices for {cfg.tickers} from {cfg.start} to {cfg.end}...")
    prices = download_prices(cfg.tickers, cfg.start, cfg.end)

    if prices.empty:
        print("No price data downloaded. Check ticker symbols or date range.")
        return

    result = equal_weight_backtest(prices, cfg.initial_capital)

    stats = result.attrs
    print("\nBacktest summary (equal-weight buy & hold):")
    print(f"Start:         {stats['start']}")
    print(f"End:           {stats['end']}")
    print(f"Final equity:  {stats['final_equity']:,.2f}")
    print(f"Total return:  {stats['total_return']*100:,.2f}%")
    print(f"Max drawdown:  {stats['max_drawdown']*100:,.2f}%")

    # Save equity curve for later comparison
    out_path = "ai_rotation_equal_weight_equity.csv"
    result.to_csv(out_path)
    print(f"\nEquity curve saved to {out_path}")


if __name__ == "__main__":
    main()
