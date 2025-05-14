import pandas as pd
import numpy as np

from etl.transform.helper.threshold import check_threshold_age, set_monthly_balance_cap, set_invested_monthly_cap, drop_rows_with_negative_value


def test_check_threshold_age():
    assert check_threshold_age(50) is True
    assert check_threshold_age(10) is False
    assert check_threshold_age(100) is False
    assert check_threshold_age(0) is False


def test_set_monthly_balance_cap():
    df = pd.DataFrame({
        'Monthly_Balance': [1000, 3500, -100, 'invalid']
    })
    result = set_monthly_balance_cap(df.copy(), cap=3000, min_val=0)

    assert np.isnan(result.loc[1, 'Monthly_Balance'])  # Above cap
    assert np.isnan(result.loc[2, 'Monthly_Balance'])  # Below min
    assert np.isnan(result.loc[3, 'Monthly_Balance'])  # Non-numeric
    assert result.loc[0, 'Monthly_Balance'] == 1000  # Valid value


def test_set_invested_monthly_cap():
    df = pd.DataFrame({
        'Amount_invested_monthly': [1500, 2500, -50, 'n/a']
    })
    result = set_invested_monthly_cap(df.copy(), cap=2000, min_val=0)

    assert np.isnan(result.loc[1, 'Amount_invested_monthly'])  # Above cap
    assert np.isnan(result.loc[2, 'Amount_invested_monthly'])  # Below min
    assert np.isnan(result.loc[3, 'Amount_invested_monthly'])  # Non-numeric
    assert result.loc[0, 'Amount_invested_monthly'] == 1500  # Valid value


def test_drop_rows_with_negative_value():
    df = pd.DataFrame({
        'Annual_Income': [50000, -10000],
        'Monthly_Inhand_Salary': [4000, -200],
        'Outstanding_Debt': [15000, -300],
        'Credit_Utilization_Ratio': [0.3, -0.5],
        'Total_EMI_per_month': [500, -50]
    })
    result = drop_rows_with_negative_value(df.copy())

    for col in df.columns:
        assert result.loc[1, col] == 0  # All negatives should be set to 0
        assert result.loc[0, col] == df.loc[0, col]  # Positives unchanged
