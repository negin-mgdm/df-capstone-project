import pandas as pd


def handle_null_values(df) -> pd.DataFrame:
    df['Name'] = df.groupby('Customer_ID')['Name'].transform(
        lambda x: x.ffill().bfill())

    avg_salary_to_income_ratio = (df['Monthly_Inhand_Salary'] / df['Annual_Income'])[
        df['Monthly_Inhand_Salary'].notnull()].mean()
    df['Monthly_Inhand_Salary'] = df['Monthly_Inhand_Salary'].fillna(
        df['Annual_Income'] * avg_salary_to_income_ratio)

    df['Credit_History_Age'].fillna(
        df['Credit_History_Age'].median(), inplace=True)

    df['Amount_invested_monthly'].fillna(0, inplace=True)

    df['Monthly_Balance'] = df.groupby(
        'Customer_ID')['Monthly_Balance'].transform(lambda x: x.ffill().bfill())

    df['Occupation'] = df.groupby('Customer_ID')['Occupation'].transform(
        lambda x: x.ffill().bfill()
    )
    df['Occupation'] = df['Occupation'].fillna('Unknown')

    df['Credit_Mix'] = df.groupby('Customer_ID')[
        'Credit_Mix'].transform(lambda x: x.ffill().bfill())

    df['Credit_Score'] = df.groupby('Customer_ID')[
        'Credit_Score'].transform(lambda x: x.ffill().bfill())

    df['Payment_Behaviour'] = df.groupby(
        'Customer_ID')['Payment_Behaviour'].transform(lambda x: x.ffill().bfill())

    df['Payment_of_Min_Amount'] = df['Payment_of_Min_Amount'].fillna('N/A')

    df = df.dropna(
        subset=['Credit_Mix', 'Payment_Behaviour', 'Name', 'Monthly_Balance'])

    return df
