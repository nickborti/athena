from datetime import datetime, timezone

from src.data.candle import Candle
from src.data.normalizer import normalize_candles


def test_normalize_candles_sorts_chronologically():
    candles = [
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
            timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.0,
            high=1.0,
            low=1.0,
            close=1.0,
            volume=None,
        ),
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
    ]

    result = normalize_candles(
        candles,
        from_timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
        to_timestamp=datetime(2026, 8, 17, 10, 3, tzinfo=timezone.utc),
    )

    timestamps = [candle.timestamp for candle in result.candles]

    assert timestamps == [
        datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
        datetime(2026, 8, 17, 10, 1, tzinfo=timezone.utc),
        datetime(2026, 8, 17, 10, 2, tzinfo=timezone.utc),
    ]

def test_normalize_candles_includes_from_and_to_boundaries():
    candles = [
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 9, 59, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.0,
            high=1.0,
            low=1.0,
            close=1.0,
            volume=None,
        ),
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.0,
            high=1.0,
            low=1.0,
            close=1.0,
            volume=None,
        ),
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
            close=1.0,
            volume=None,
        ),
    ]

    result = normalize_candles(
        candles,
        from_timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
        to_timestamp=datetime(2026, 8, 17, 10, 3, tzinfo=timezone.utc),
    )

    timestamps = [candle.timestamp for candle in result.candles]

    assert timestamps == [
        datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
        datetime(2026, 8, 17, 10, 1, tzinfo=timezone.utc),
        datetime(2026, 8, 17, 10, 2, tzinfo=timezone.utc),
        datetime(2026, 8, 17, 10, 3, tzinfo=timezone.utc),
    ]

def test_normalize_candles_removes_duplicate_timestamps():
    candles = [
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.0,
            high=1.0,
            low=1.0,
            close=1.0,
            volume=None,
        ),
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
    ]

    result = normalize_candles(
        candles,
        from_timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
        to_timestamp=datetime(2026, 8, 17, 10, 2, tzinfo=timezone.utc),
    )

    timestamps = [candle.timestamp for candle in result.candles]

    assert timestamps == [
        datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
        datetime(2026, 8, 17, 10, 1, tzinfo=timezone.utc),
        datetime(2026, 8, 17, 10, 2, tzinfo=timezone.utc),
    ]

def test_normalize_candles_detects_gap():
    candles = [
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.0,
            high=1.0,
            low=1.0,
            close=1.0,
            volume=None,
        ),
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
            timestamp=datetime(2026, 8, 17, 10, 5, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.0,
            high=1.0,
            low=1.0,
            close=1.0,
            volume=None,
        ),
    ]

    result = normalize_candles(
        candles,
        from_timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
        to_timestamp=datetime(2026, 8, 17, 10, 5, tzinfo=timezone.utc),
    )

    assert len(result.gaps) == 1

    gap = result.gaps[0]

    assert gap.previous_timestamp == datetime(
        2026, 8, 17, 10, 2, tzinfo=timezone.utc
    )

    assert gap.next_timestamp == datetime(
        2026, 8, 17, 10, 5, tzinfo=timezone.utc
    )

def test_normalize_candles_detects_gap_for_5m_timeframe():
    candles = [
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
            timeframe="5m",
            open=1.0,
            high=1.0,
            low=1.0,
            close=1.0,
            volume=None,
        ),
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 5, tzinfo=timezone.utc),
            timeframe="5m",
            open=1.0,
            high=1.0,
            low=1.0,
            close=1.0,
            volume=None,
        ),
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 20, tzinfo=timezone.utc),
            timeframe="5m",
            open=1.0,
            high=1.0,
            low=1.0,
            close=1.0,
            volume=None,
        ),
    ]

    result = normalize_candles(
        candles,
        from_timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
        to_timestamp=datetime(2026, 8, 17, 10, 20, tzinfo=timezone.utc),
    )

    assert len(result.gaps) == 1

    gap = result.gaps[0]

    assert gap.previous_timestamp == datetime(
        2026, 8, 17, 10, 5, tzinfo=timezone.utc
    )

    assert gap.next_timestamp == datetime(
        2026, 8, 17, 10, 20, tzinfo=timezone.utc
    )

def test_normalize_candles_detects_gap_for_1h_timeframe():
    candles = [
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
            timeframe="1h",
            open=1.0,
            high=1.0,
            low=1.0,
            close=1.0,
            volume=None,
        ),
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 11, 0, tzinfo=timezone.utc),
            timeframe="1h",
            open=1.0,
            high=1.0,
            low=1.0,
            close=1.0,
            volume=None,
        ),
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 13, 0, tzinfo=timezone.utc),
            timeframe="1h",
            open=1.0,
            high=1.0,
            low=1.0,
            close=1.0,
            volume=None,
        ),
    ]

    result = normalize_candles(
        candles,
        from_timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
        to_timestamp=datetime(2026, 8, 17, 13, 0, tzinfo=timezone.utc),
    )

    assert len(result.gaps) == 1

    gap = result.gaps[0]

    assert gap.previous_timestamp == datetime(
        2026, 8, 17, 11, 0, tzinfo=timezone.utc
    )

    assert gap.next_timestamp == datetime(
        2026, 8, 17, 13, 0, tzinfo=timezone.utc
    )
