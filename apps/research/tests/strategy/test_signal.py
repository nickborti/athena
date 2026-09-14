from datetime import datetime, timezone

from src.strategy.signal import Signal


def test_signal_contains_action_and_timestamp():
    timestamp = datetime(2026, 8, 17, 10, 1, tzinfo=timezone.utc)

    signal = Signal(
        action="UP",
        timestamp=timestamp,
    )

    assert signal.action == "UP"
    assert signal.timestamp == timestamp