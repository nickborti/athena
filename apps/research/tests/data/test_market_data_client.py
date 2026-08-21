from datetime import datetime, timezone

from src.data.candle import Candle
from src.data.market_data_client import MarketDataClient

from unittest.mock import Mock


def test_market_data_client_parses_candles():
    response = [
        {
            "symbol": "EURUSD",
            "timestamp": "2026-08-17T10:00:00.000Z",
            "timeframe": "1m",
            "open": 1.0,
            "high": 1.1,
            "low": 0.9,
            "close": 1.05,
            "volume": None,
        }
    ]

    client = MarketDataClient("http://localhost:3000")

    candles = client.parse_candles(response)

    assert candles == [
        Candle(
            symbol="EURUSD",
            timestamp=datetime(2026, 8, 17, 10, 0, tzinfo=timezone.utc),
            timeframe="1m",
            open=1.0,
            high=1.1,
            low=0.9,
            close=1.05,
            volume=None,
        )
    ]


def test_market_data_client_get_candles():
    response = [
        {
            "symbol": "EURUSD",
            "timestamp": "2026-08-17T10:00:00.000Z",
            "timeframe": "1m",
            "open": 1.0,
            "high": 1.1,
            "low": 0.9,
            "close": 1.05,
            "volume": None,
        }
    ]

    http_client = Mock()
    http_client.get.return_value.json.return_value = response

    client = MarketDataClient(
        "http://localhost:3001",
        http_client=http_client,
    )

    candles = client.get_candles(
        symbol="EURUSD",
        timeframe="1m",
        from_timestamp="2026-08-17T10:00:00Z",
        to_timestamp="2026-08-17T10:05:00Z",
    )

    assert candles[0].symbol == "EURUSD"
    assert candles[0].timestamp == datetime(
        2026, 8, 17, 10, 0, tzinfo=timezone.utc
    )

    http_client.get.assert_called_once()