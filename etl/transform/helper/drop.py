import pandas as pd


def drop_unwanted_columns(df) -> pd.DataFrame:
    columns_to_drop = [
        'ID', 'SSN', 'Num_Bank_Accounts', 'Num_Credit_Card', 'Interest_Rate',
        'Num_of_Loan', 'Type_of_Loan', 'Delay_from_due_date',
        'Num_of_Delayed_Payment', 'Changed_Credit_Limit', 'Num_Credit_Inquiries'
    ]
    df_dropped = df.drop(columns=columns_to_drop)
    return df_dropped
