from src.backtest.strategy_backtest import run_strategy_backtest
from src.backtest.summary import BacktestSummary


def test_backtest_can_compare_3m_and_5m(backtest_candles):
    results_3m = run_strategy_backtest(
        candles=backtest_candles,
        expiry_minutes=3,
    )

    results_5m = run_strategy_backtest(
        candles=backtest_candles,
        expiry_minutes=5,
    )

    summary_3m = BacktestSummary(results_3m, expiry_minutes=3)
    summary_5m = BacktestSummary(results_5m, expiry_minutes=5)

    assert isinstance(summary_3m, BacktestSummary)
    assert isinstance(summary_5m, BacktestSummary)

    assert summary_3m.expiry_minutes == 3
    assert summary_5m.expiry_minutes == 5

from src.backtest.expiry_comparison import ExpiryComparison
from src.backtest.summary import BacktestSummary


from src.backtest.expiry_comparison import ExpiryComparison
from src.backtest.summary import BacktestSummary


def test_expiry_comparison_selects_higher_win_rate():
    summary_3m = BacktestSummary(
        results=["WIN", "LOSS", "LOSS"],
        expiry_minutes=3,
    )

    summary_5m = BacktestSummary(
        results=["WIN", "WIN", "LOSS"],
        expiry_minutes=5,
    )

    comparison = ExpiryComparison(
        summary_3m=summary_3m,
        summary_5m=summary_5m,
    )

    assert comparison.summary_3m is summary_3m
    assert comparison.summary_5m is summary_5m
    assert comparison.better_expiry == 5