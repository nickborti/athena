from datetime import datetime

import httpx

from src.data.candle import Candle


class MarketDataClient:
    def __init__(self, base_url: str, http_client: httpx.Client | None = None,):
        self.base_url = base_url
        self.http_client = http_client or httpx.Client()

    def get_candles(
        self,
        symbol: str,
        timeframe: str,
        from_timestamp: str,
        to_timestamp: str,
    ) -> list[Candle]:
        response = self.http_client.get(
            f"{self.base_url}/api/market-data/candles",
            params={
                "symbol": symbol,
                "timeframe": timeframe,
                "from": from_timestamp,
                "to": to_timestamp,
            },
        )

        response.raise_for_status()

        return self.parse_candles(response.json())

    def parse_candles(self, response: list[dict]) -> list[Candle]:
        return [
            Candle(
                symbol=item["symbol"],
                timestamp=datetime.fromisoformat(
                    item["timestamp"].replace("Z", "+00:00")
                ),
                timeframe=item["timeframe"],
                open=float(item["open"]),
                high=float(item["high"]),
                low=float(item["low"]),
                close=float(item["close"]),
                volume=float(item["volume"])
                if item["volume"] is not None
                else None,
            )
            for item in response
        ]