from src.backtest.summary import BacktestSummary

def test_backtest_summary_calculates_statistics():
    summary = BacktestSummary(
        results=["WIN", "WIN", "LOSS", "TIE"],
        expiry_minutes=3,
    )

    assert summary.total_trades == 4
    assert summary.wins == 2
    assert summary.losses == 1
    assert summary.ties == 1
    assert summary.win_rate == 66.67
