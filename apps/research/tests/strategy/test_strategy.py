from datetime import datetime, timezone

from src.data.candle import Candle
from src.strategy.strategy import generate_signal


def test_strategy_returns_buy_when_price_increases():
    previous_candle = Candle(
        symbol="EURUSD",
        timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
        timeframe="1m",
        open=1.0,
        high=1.1,
        low=0.9,
        close=1.0,
        volume=None,
    )

    current_candle = Candle(
        symbol="EURUSD",
        timestamp=datetime(2026, 8, 17, 10, 1, tzinfo=timezone.utc),
        timeframe="1m",
        open=1.0,
        high=1.2,
        low=0.95,
        close=1.05,
        volume=None,
    )

    signal = generate_signal(previous_candle, current_candle)

    assert signal.action == "BUY"
    assert signal.timestamp == current_candle.timestamp

def test_strategy_returns_sell_when_price_decreases():
    previous_candle = Candle(
        symbol="EURUSD",
        timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
        timeframe="1m",
        open=1.0,
        high=1.1,
        low=0.9,
        close=1.05,
        volume=None,
    )

    current_candle = Candle(
        symbol="EURUSD",
        timestamp=datetime(2026, 8, 17, 10, 1, tzinfo=timezone.utc),
        timeframe="1m",
        open=1.0,
        high=1.05,
        low=0.9,
        close=1.0,
        volume=None,
    )

    signal = generate_signal(previous_candle, current_candle)

    assert signal.action == "SELL"
    assert signal.timestamp == current_candle.timestamp

def test_strategy_returns_hold_when_price_stays_same():
    previous_candle = Candle(
        symbol="EURUSD",
        timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
        timeframe="1m",
        open=1.0,
        high=1.1,
        low=0.9,
        close=1.05,
        volume=None,
    )

    current_candle = Candle(
        symbol="EURUSD",
        timestamp=datetime(2026, 8, 17, 10, 1, tzinfo=timezone.utc),
        timeframe="1m",
        open=1.0,
        high=1.05,
        low=0.9,
        close=1.05,
        volume=None,
    )

    signal = generate_signal(previous_candle, current_candle)

    assert signal.action == "HOLD"
    assert signal.timestamp == current_candle.timestamp