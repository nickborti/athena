from src.data.market_data_client import MarketDataClient


def test_market_data_client_calls_nestjs_api():
    client = MarketDataClient("http://localhost:3001")

    candles = client.get_candles(
        symbol="EURUSD",
        timeframe="1m",
        from_timestamp="2026-08-17T10:00:00Z",
        to_timestamp="2026-08-17T10:05:00Z",
    )

    assert len(candles) > 0
    assert candles[0].symbol == "EURUSD"
    assert candles[0].timeframe == "1m"