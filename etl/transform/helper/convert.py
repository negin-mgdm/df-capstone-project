import re
import numpy as np
import pandas as pd


def convert_data(df) -> pd.DataFrame:
    df["Credit_History_Age"] = df["Credit_History_Age"].apply(
        convert_credit_history_age)
    return df


def convert_credit_history_age(val):
    if isinstance(val, str):
        match = re.match(r"(\d+)\s+Years\s+and\s+(\d+)\s+Months", val.strip())
        if match:
            years = int(match.group(1))
            months = int(match.group(2))
            return years * 12 + months
    return np.nan
