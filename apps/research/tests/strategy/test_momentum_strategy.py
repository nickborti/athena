from datetime import datetime, timezone

from src.data.candle import Candle
from src.strategy.signal import Signal
from src.strategy.momentum import generate_momentum_signal


def test_momentum_strategy_returns_buy_after_two_up_moves():
    candle_1 = Candle(
        symbol="EURUSD",
        timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
        timeframe="1m",
        open=1.00,
        high=1.01,
        low=0.99,
        close=1.00,
        volume=None,
    )

    candle_2 = Candle(
        symbol="EURUSD",
        timestamp=datetime(2026, 8, 17, 10, 1, tzinfo=timezone.utc),
        timeframe="1m",
        open=1.00,
        high=1.06,
        low=0.99,
        close=1.05,
        volume=None,
    )

    candle_3 = Candle(
        symbol="EURUSD",
        timestamp=datetime(2026, 8, 17, 10, 2, tzinfo=timezone.utc),
        timeframe="1m",
        open=1.05,
        high=1.09,
        low=1.04,
        close=1.08,
        volume=None,
    )

    signal_1 = generate_momentum_signal(candle_1, candle_2)
    signal_2 = generate_momentum_signal(candle_2, candle_3)

    assert signal_1.action == "BUY"
    assert signal_2.action == "BUY"


def test_momentum_strategy_returns_sell_after_two_down_moves():
    candle_1 = Candle(
        symbol="EURUSD",
        timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
        timeframe="1m",
        open=1.08,
        high=1.09,
        low=1.07,
        close=1.08,
        volume=None,
    )

    candle_2 = Candle(
        symbol="EURUSD",
        timestamp=datetime(2026, 8, 17, 10, 1, tzinfo=timezone.utc),
        timeframe="1m",
        open=1.08,
        high=1.09,
        low=1.04,
        close=1.05,
        volume=None,
    )

    signal = generate_momentum_signal(candle_1, candle_2)

    assert signal.action == "SELL"