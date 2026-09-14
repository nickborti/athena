from datetime import datetime

from src.backtest.expiry_comparison import ExpiryComparison
from src.backtest.strategy_backtest import run_strategy_backtest
from src.backtest.summary import BacktestSummary
from src.data.market_data_client import MarketDataClient
from src.data.normalizer import normalize_candles


def run_historical_research(
    client: MarketDataClient,
    symbol: str,
    timeframe: str,
    from_timestamp: datetime,
    to_timestamp: datetime,
) -> ExpiryComparison:
    raw_candles = client.get_candles(
        symbol=symbol,
        timeframe=timeframe,
        from_timestamp=from_timestamp.isoformat(),
        to_timestamp=to_timestamp.isoformat(),
    )

    normalized = normalize_candles(
        raw_candles,
        from_timestamp=from_timestamp,
        to_timestamp=to_timestamp,
    )

    candles = normalized.candles

    results_3m = run_strategy_backtest(
        candles=candles,
        expiry_minutes=3,
    )

    results_5m = run_strategy_backtest(
        candles=candles,
        expiry_minutes=5,
    )

    summary_3m = BacktestSummary(
        results=results_3m,
        expiry_minutes=3,
    )

    summary_5m = BacktestSummary(
        results=results_5m,
        expiry_minutes=5,
    )

    return ExpiryComparison(
        summary_3m=summary_3m,
        summary_5m=summary_5m,
    )