import pandas as pd
from etl.transform.helper.nulls import handle_null_values


def test_handle_null_values():
    data = {
        'Customer_ID': [1, 1, 1, 2, 2],
        'Name': [None, 'Alice', None, None, 'Bob'],
        'Monthly_Inhand_Salary': [2000, None, None, 3000, None],
        'Annual_Income': [24000, 24000, 24000, 36000, 36000],
        'Credit_History_Age': [5.0, None, None, None, 6.0],
        'Amount_invested_monthly': [100, None, None, None, 150],
        'Monthly_Balance': [500, None, None, None, 600],
        'Occupation': [None, 'Engineer', None, None, 'Doctor'],
        'Credit_Mix': ['Standard', None, None, None, 'Good'],
        'Credit_Score': ['Good', None, None, None, 'Poor'],
        'Payment_Behaviour': ['Regular', None, None, None, 'Irregular'],
        'Payment_of_Min_Amount': [None, 'Yes', None, 'No', None],
    }

    df = pd.DataFrame(data)
    processed_df = handle_null_values(df)

    # Name filled with forward/backward
    assert processed_df['Name'].isnull().sum() == 0

    # Monthly salary calculated based on income
    assert processed_df['Monthly_Inhand_Salary'].isnull().sum() == 0

    # Credit history filled with median
    assert processed_df['Credit_History_Age'].isnull().sum() == 0

    # Group-wise ffill/bfill for amount invested and balance
    assert processed_df['Amount_invested_monthly'].isnull().sum() == 0
    assert processed_df['Monthly_Balance'].isnull().sum() == 0

    # Occupation: ffill/bfill then 'Unknown' if still null
    assert processed_df['Occupation'].isnull().sum() == 0
    # all values recovered
    assert 'Unknown' not in processed_df['Occupation'].values

    # Credit_Mix and Credit_Score filled
    assert processed_df['Credit_Mix'].isnull().sum() == 0
    assert processed_df['Credit_Score'].isnull().sum() == 0

    # Payment behaviour filled
    assert processed_df['Payment_Behaviour'].isnull().sum() == 0

    # Payment of min amount defaults to 'N/A'
    assert 'N/A' in processed_df['Payment_of_Min_Amount'].values

    # Final drop: should not contain any nulls in critical columns
    assert not processed_df[['Credit_Mix', 'Payment_Behaviour',
                             'Name', 'Monthly_Balance']].isnull().any().any()
