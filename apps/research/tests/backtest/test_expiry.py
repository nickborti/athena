from datetime import datetime, timezone

from src.data.candle import Candle
from src.backtest.expiry import find_expiry_candle


def test_finds_candle_at_3_minute_expiry():
    candles = [
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 1, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.0,
            high=1.0,
            low=1.0,
            close=1.0,
            volume=None,
        ),
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 2, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.0,
            high=1.0,
            low=1.0,
            close=1.0,
            volume=None,
        ),
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 3, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.0,
            high=1.0,
            low=1.0,
            close=1.0,
            volume=None,
        ),
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 4, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.0,
            high=1.0,
            low=1.0,
            close=1.12,
            volume=None,
        ),
    ]

    result = find_expiry_candle(
        candles,
        signal_timestamp=datetime(2026, 8, 17, 10, 1, tzinfo=timezone.utc),
        expiry_minutes=3,
    )

    assert result.timestamp == datetime(
        2026, 8, 17, 10, 4, tzinfo=timezone.utc
    )