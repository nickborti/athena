from src.backtest.binary_backtest import run_binary_backtest
from src.backtest.expiry import find_expiry_candle
from src.data.candle import Candle
from src.strategy.strategy import generate_signal


def run_strategy_backtest(
    candles: list[Candle],
    expiry_minutes: int,
    strategy=generate_signal,
) -> list[str]:
    results = []
    index = 1

    while index < len(candles):
        previous_candle = candles[index - 1]
        current_candle = candles[index]

        signal = strategy(
            previous_candle,
            current_candle,
        )

        if signal.action == "HOLD":
            index += 1
            continue

        try:
            expiry_candle = find_expiry_candle(
                candles,
                signal_timestamp=signal.timestamp,
                expiry_minutes=expiry_minutes,
            )
        except ValueError:
            index += 1
            continue

        result = run_binary_backtest(
            candles=candles,
            signal=signal,
            entry_price=current_candle.close,
            expiry_minutes=expiry_minutes,
        )

        results.append(result)

        expiry_index = next(
            i
            for i, candle in enumerate(candles)
            if candle.timestamp == expiry_candle.timestamp
        )

        index = expiry_index + 1

    return results