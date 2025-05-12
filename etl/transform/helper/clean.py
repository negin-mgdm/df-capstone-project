import re
import numpy as np
import pandas as pd


def clean_data(df) -> pd.DataFrame:
    string_columns = ["Month", "Name", "Occupation",
                      "Credit_Mix"]
    for col in string_columns:
        df[col] = df[col].apply(clean_special_chars_string)

    df["Credit_History_Age"] = df["Credit_History_Age"].apply(
        clean_credit_history_age_amount)

    df["Payment_of_Min_Amount"] = df["Payment_of_Min_Amount"].apply(
        clean_payment_of_min_amount)

    df["Payment_Behaviour"] = df["Payment_Behaviour"].apply(
        clean_payment_behaviour)

    numerical_columns = ["Age", "Annual_Income", "Monthly_Inhand_Salary", "Outstanding_Debt",
                         "Credit_Utilization_Ratio", "Total_EMI_per_month", "Amount_invested_monthly", "Monthly_Balance"]
    for col in numerical_columns:
        df[col] = df[col].apply(clean_special_chars_number)

    return df


def clean_special_chars_string(val):
    if isinstance(val, str) and all(char.isalpha() or char.isspace() for char in val):
        return val
    else:
        return np.nan


def clean_special_chars_number(val):
    if pd.isnull(val) or (isinstance(val, str) and val.strip() == ''):
        return np.nan

    if isinstance(val, (int, float)):
        return round(float(val), 2)

    if isinstance(val, str):
        match = re.search(r'\d+\.?\d*', val)
        if match:
            return round(float(match.group()), 2)

    return np.nan


def clean_credit_history_age_amount(val):
    pattern = r"^\d+\s+Years\s+and\s+\d+\s+Months$"
    if isinstance(val, str) and re.match(pattern, val.strip()):
        return val
    else:
        return np.nan


def clean_payment_of_min_amount(val):
    if isinstance(val, str) and val.strip().upper() == 'NM':
        return np.nan
    elif isinstance(val, str) and any(char.isalpha() for char in val):
        return val.strip()
    else:
        return np.nan


def clean_payment_behaviour(val):
    pattern = r"^(High|Low)_spent_(Small|Medium|Large)_value_payments$"
    if isinstance(val, str) and re.match(pattern, val.strip()):
        return val.strip()
    return np.nan
