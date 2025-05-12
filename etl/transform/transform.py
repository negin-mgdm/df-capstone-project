import pandas as pd
from etl.transform.helper.drop import drop_unwanted_columns
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
