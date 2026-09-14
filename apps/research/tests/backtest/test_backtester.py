from datetime import datetime, timezone

from src.data.candle import Candle
from src.strategy.strategy import generate_signal
from src.backtest.backtester import Backtester


def test_backtester_opens_position_on_buy_signal():
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

    backtester = Backtester()

    result = backtester.process_signal(
        signal=signal,
        price=current_candle.close,
        timestamp=current_candle.timestamp,
    )

    assert result.position == 1
    assert result.entry_price == 1.05