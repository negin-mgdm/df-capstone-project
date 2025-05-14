import pandas as pd
from etl.transform.helper.drop import drop_unwanted_columns


def test_drop_unwanted_columns():
    data = {
        'ID': [1],
        'SSN': ['XXX-XX-1234'],
        'Num_Bank_Accounts': [5],
        'Num_Credit_Card': [2],
        'Interest_Rate': [12.5],
        'Num_of_Loan': [1],
        'Type_of_Loan': ['Home Loan'],
        'Delay_from_due_date': [5],
        'Num_of_Delayed_Payment': [2],
        'Changed_Credit_Limit': [None],
        'Num_Credit_Inquiries': [3],
        'Customer_ID': ['C001'],
        'Annual_Income': [50000]
    }

    df = pd.DataFrame(data)
    result_df = drop_unwanted_columns(df)

    # Ensure dropped columns are not in the result
    dropped_columns = [
        'ID', 'SSN', 'Num_Bank_Accounts', 'Num_Credit_Card', 'Interest_Rate',
        'Num_of_Loan', 'Type_of_Loan', 'Delay_from_due_date',
        'Num_of_Delayed_Payment', 'Changed_Credit_Limit', 'Num_Credit_Inquiries'
    ]
    for col in dropped_columns:
        assert col not in result_df.columns

    # Ensure expected columns are retained
    assert 'Customer_ID' in result_df.columns
    assert 'Annual_Income' in result_df.columns

    # Ensure data integrity
    assert result_df.shape[1] == 2  # Only 2 columns remain
