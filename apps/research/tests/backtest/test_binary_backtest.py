from datetime import datetime, timezone

from src.backtest.binary_backtest import (
    evaluate_binary_trade,
    run_binary_backtest,
)
from src.data.candle import Candle
from src.strategy.signal import Signal


def test_buy_signal_wins_after_3_minute_expiry():
    signal = Signal(
        action="BUY",
        timestamp=datetime(2026, 8, 17, 10, 1, tzinfo=timezone.utc),
    )

    result = evaluate_binary_trade(
        signal=signal,
        entry_price=1.10,
        expiry_price=1.12,
        expiry_minutes=3,
    )

    assert result == "WIN"


def test_binary_backtest_evaluates_3_minute_trade():
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
            timestamp=datetime(2026, 8, 17, 10, 4, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.04,
            high=1.05,
            low=1.03,
            close=1.04,
            volume=None,
        ),
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 5, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.04,
            high=1.05,
            low=1.03,
            close=1.04,
            volume=None,
        ),
    ]

    signal = Signal(
        action="BUY",
        timestamp=datetime(2026, 8, 17, 10, 1, tzinfo=timezone.utc),
    )

    result = run_binary_backtest(
        candles=candles,
        signal=signal,
        entry_price=1.03,
        expiry_minutes=3,
    )

    assert result == "WIN"