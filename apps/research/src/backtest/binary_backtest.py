from src.backtest.expiry import find_expiry_candle
from src.data.candle import Candle
from src.strategy.signal import Signal


def evaluate_binary_trade(
    signal,
    entry_price: float,
    expiry_price: float,
    expiry_minutes: int,
) -> str:
    if expiry_minutes not in (3, 5):
        raise ValueError("expiry_minutes must be 3 or 5")

    if expiry_price == entry_price:
        return "TIE"

    if signal.action == "BUY":
        return "WIN" if expiry_price > entry_price else "LOSS"

    if signal.action == "SELL":
        return "WIN" if expiry_price < entry_price else "LOSS"

    return "WAIT"


def run_binary_backtest(
    candles: list[Candle],
    signal: Signal,
    entry_price: float,
    expiry_minutes: int,
) -> str:
    expiry_candle = find_expiry_candle(
        candles,
        signal_timestamp=signal.timestamp,
        expiry_minutes=expiry_minutes,
    )

    expiry_price = expiry_candle.close

    return evaluate_binary_trade(
        signal=signal,
        entry_price=entry_price,
        expiry_price=expiry_price,
        expiry_minutes=expiry_minutes,
    )