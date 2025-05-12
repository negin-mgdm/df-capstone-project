import pandas as pd
from etl.transform.helper.clean import clean_data
from etl.transform.helper.convert import convert_data
from etl.transform.helper.nulls import handle_null_values
from etl.transform.helper.threshold import check_threshold


def transform_data(df) -> pd.DataFrame:
    df_transformed = drop_unwanted_columns(df)
    df_transformed = clean_data(df_transformed)
    df_transformed = convert_data(df_transformed)
    df_transformed = check_threshold(df_transformed)
    df_transformed = handle_null_values(df_transformed)

    return df_transformed


def drop_unwanted_columns(df) -> pd.DataFrame:
    columns_to_drop = [
        'ID', 'SSN', 'Num_Bank_Accounts', 'Num_Credit_Card', 'Interest_Rate',
        'Num_of_Loan', 'Type_of_Loan', 'Delay_from_due_date',
        'Num_of_Delayed_Payment', 'Changed_Credit_Limit', 'Num_Credit_Inquiries'
    ]
    df_dropped = df.drop(columns=columns_to_drop)
    return df_dropped
