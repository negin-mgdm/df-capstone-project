import re
import pandas as pd


def transform_data(df) -> pd.DataFrame:
    df_transformed = drop_unwanted_columns(df)
    df_transformed = clean_data(df_transformed)
    return df_transformed

def clean_data(df) -> pd.DataFrame:
    string_columns = ["Month", "Name", "Occupation",
                      "Credit_Mix", "Payment_of_Min_Amount", "Payment_Behaviour"]
    for col in string_columns:
        df[col] = df[col].apply(clean_special_chars_string)

    df["Credit_History_Age"] = df["Credit_History_Age"].apply(
        clean_credit_history_age_column)

    numerical_columns = ["Age", "Annual_Income", "Monthly_Inhand_Salary", "Outstanding_Debt",
                         "Credit_Utilization_Ratio", "Total_EMI_per_month", "Amount_invested_monthly", "Monthly_Balance"]
    for col in numerical_columns:
        df[col] = df[col].apply(clean_special_chars_number)

    return df

def clean_special_chars_string(val):
    if isinstance(val, str) and all(char.isalpha() or char.isspace() for char in val):
        return val
    else:
        return "N/A"

def clean_special_chars_number(val):
    if pd.isnull(val) or (isinstance(val, str) and val.strip() == ''):
        return "N/A"

    if isinstance(val, (int, float)):
        return round(float(val), 2)

    if isinstance(val, str):
        match = re.search(r'\d+\.?\d*', val)
        if match:
            return round(float(match.group()), 2)

    return "N/A"

def clean_credit_history_age_column(val):
    pattern = r"^\d+\s+Years\s+and\s+\d+\s+Months$"
    if isinstance(val, str) and re.match(pattern, val.strip()):
        return val
    else:
        return "N/A"

def drop_unwanted_columns(df) -> pd.DataFrame:
    columns_to_drop = [
        'ID', 'SSN', 'Num_Bank_Accounts', 'Num_Credit_Card', 'Interest_Rate',
        'Num_of_Loan', 'Type_of_Loan', 'Delay_from_due_date',
        'Num_of_Delayed_Payment', 'Changed_Credit_Limit', 'Num_Credit_Inquiries'
    ]
    df_dropped = df.drop(columns=columns_to_drop)
    return df_dropped
