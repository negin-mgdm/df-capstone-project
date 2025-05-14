import pandas as pd
import streamlit as st
import plotly.express as px


def tab_3(df):
    st.header("Risk & Behavior Insights")

    top_risk1 = draw_high_debt_low_salary_graph(df)
    top_low_spend = draw_missed_payments_low_spending_graph(df)
    draw_risk_summary_chart(top_risk1, top_low_spend)


def draw_high_debt_low_salary_graph(df):
    st.subheader("Customers with High Debt and Low Salary")
    risk1 = df[df['Outstanding_Debt'] > 2 * df['Monthly_Inhand_Salary']]
    grouped_risk1 = risk1.groupby(['Customer_ID', 'Name']).agg({
        'Monthly_Inhand_Salary': 'mean',
        'Outstanding_Debt': 'mean'
    }).reset_index()
    top_risk1 = grouped_risk1.sort_values(
        by='Outstanding_Debt', ascending=False)
    st.dataframe(top_risk1)
    return top_risk1


def draw_missed_payments_low_spending_graph(df):
    st.subheader("Customers with Missed Payments and Low Spending")
    low_spend = df[
        (df['Payment_of_Min_Amount'] == 'No') &
        (df['Payment_Behaviour'].str.contains("Low_spent", na=False))
    ]
    grouped_low_spend = low_spend.groupby(['Customer_ID', 'Name']).agg({
        'Outstanding_Debt': 'mean',
        'Payment_Behaviour': 'first',
    }).reset_index()
    top_low_spend = grouped_low_spend.sort_values(
        by='Outstanding_Debt', ascending=False)
    st.dataframe(top_low_spend)
    return top_low_spend


def draw_risk_summary_chart(top_risk1, top_low_spend):
    high_debt_ids = set(top_risk1['Customer_ID'])
    low_spend_ids = set(top_low_spend['Customer_ID'])

    both_risks = high_debt_ids & low_spend_ids
    only_high_debt = high_debt_ids - both_risks
    only_low_spend = low_spend_ids - both_risks

    risk_summary_df = pd.DataFrame({
        'Risk Type': ['High Debt Only', 'Low Spending Only', 'Both'],
        'Count': [len(only_high_debt), len(only_low_spend), len(both_risks)]
    })

    fig_risk_summary = px.bar(
        risk_summary_df,
        x='Risk Type',
        y='Count',
        color='Risk Type',
        text='Count',
        title="Customer Risk Summary"
    )
    fig_risk_summary.update_layout(showlegend=False)
    st.plotly_chart(fig_risk_summary, use_container_width=True)
