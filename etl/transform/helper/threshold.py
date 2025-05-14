import numpy as np
import pandas as pd


def check_threshold(df) -> pd.DataFrame:
    df = df[df['Age'].apply(check_threshold_age)]
    df = set_monthly_balance_cap(df)
    df = drop_rows_with_negative_value(df)
    return df


def check_threshold_age(val):
    return 10 < val < 100


def set_monthly_balance_cap(df, cap=3000, min_val=0):
    df['Monthly_Balance'] = pd.to_numeric(
        df['Monthly_Balance'], errors='coerce')

    df.loc[(df['Monthly_Balance'] > cap) | (
        df['Monthly_Balance'] < min_val), 'Monthly_Balance'] = np.nan

    return df


def drop_rows_with_negative_value(df):
    numerical_columns = ["Annual_Income", "Monthly_Inhand_Salary", "Outstanding_Debt",
                         "Credit_Utilization_Ratio", "Total_EMI_per_month",
                         "Amount_invested_monthly"]

    for col in numerical_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

        df.loc[df[col] < 0, col] = 0

    return df
