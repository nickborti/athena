from datetime import datetime, timezone

from src.data.candle import Candle
from src.backtest.strategy_backtest import run_strategy_backtest


def test_runs_strategy_across_candles_and_collects_results():
    candles = [
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.00,
            high=1.01,
            low=0.99,
            close=1.00,
            volume=None,
        ),
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 1, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.00,
            high=1.06,
            low=0.99,
            close=1.05,
            volume=None,
        ),
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 2, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.05,
            high=1.06,
            low=1.04,
            close=1.04,
            volume=None,
        ),
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 3, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.04,
            high=1.06,
            low=1.04,
            close=1.05,
            volume=None,
        ),
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 4, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.05,
            high=1.07,
            low=1.04,
            close=1.06,
            volume=None,
        ),
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 5, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.06,
            high=1.06,
            low=1.04,
            close=1.05,
            volume=None,
        ),
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 6, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.05,
            high=1.06,
            low=1.04,
            close=1.04,
            volume=None,
        ),
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 7, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.04,
            high=1.06,
            low=1.04,
            close=1.05,
            volume=None,
        ),
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 8, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.05,
            high=1.06,
            low=1.03,
            close=1.04,
            volume=None,
        ),
    ]

    results = run_strategy_backtest(
        candles=candles,
        expiry_minutes=3,
    )

    assert len(results) == 2
    assert results[0] == "WIN"
    assert results[1] == "WIN"

from datetime import datetime, timezone

from src.data.candle import Candle
from src.strategy.signal import Signal


def test_backtest_accepts_custom_strategy(backtest_candles):
    def custom_strategy(previous_candle, current_candle):
        return Signal(
            action="HOLD",
            timestamp=current_candle.timestamp,
        )

    results = run_strategy_backtest(
        candles=backtest_candles,
        expiry_minutes=3,
        strategy=custom_strategy,
    )

    assert results == []