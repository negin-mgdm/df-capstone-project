import pandas as pd
import streamlit as st
import plotly.express as px


def setup_filter(df):
    with st.sidebar:
        st.markdown("---")
        st.subheader("Filters")
        credit_score_options = df['Credit_Score'].dropna().unique()
        selected_credit_score = st.multiselect(
            "Credit Score", credit_score_options, default=credit_score_options)
        selected_age = st.slider("Age Range", int(
            df['Age'].min()), int(df['Age'].max()), (20, 60))
        selected_history = st.slider("Credit History Age (Months)", int(
            df['Credit_History_Age'].min()), int(df['Credit_History_Age'].max()), (0, 400))

        return (selected_credit_score, selected_age, selected_history)


def tab_2(df, selected_credit_score, selected_age, selected_history):
    st.header("Segment Analysis & Trends")
    filtered_df = df[
        (df['Credit_Score'].isin(selected_credit_score)) &
        (df['Age'].between(*selected_age)) &
        (df['Credit_History_Age'].between(*selected_history))
    ]

    draw_creditscore_occupation_graph(filtered_df)
    draw_avg_monthly_balance_occupation_graph(filtered_df)
    draw_total_emi_per_month_graph(filtered_df)


def draw_creditscore_occupation_graph(filtered_df):
    st.subheader("Credit Score Distribution by Occupation")

    credit_score_dist = (
        filtered_df.groupby(['Occupation', 'Credit_Score'])
        .size()
        .reset_index(name='Count')
    )

    colour_map = {
        'Good': '#1f77b4',
        'Standard': 'gold',
        'Bad': '#d62728'
    }

    fig_mix = px.bar(
        credit_score_dist,
        x='Occupation',
        y='Count',
        color='Credit_Score',
        barmode='stack',
        color_discrete_map=colour_map,
        title=None
    )

    st.plotly_chart(fig_mix, use_container_width=True)


def draw_avg_monthly_balance_occupation_graph(filtered_df):
    st.subheader("Average Monthly Balance per Occupation")

    avg_balance = (
        filtered_df.groupby('Occupation')['Monthly_Balance']
        .mean()
        .reset_index()
        .sort_values('Monthly_Balance', ascending=False)
    )

    fig_balance = px.bar(
        avg_balance,
        x='Occupation',
        y='Monthly_Balance',
        color='Occupation',
        title=None
    )
    st.plotly_chart(fig_balance, use_container_width=True)


def draw_total_emi_per_month_graph(filtered_df):
    st.subheader("Total EMI per Month by Age Group")
    age_bins = pd.cut(filtered_df['Age'], bins=[
                      18, 25, 35, 45, 55, 65, 100], right=False)
    emi_by_age_group = (
        filtered_df.groupby(age_bins)['Total_EMI_per_month']
        .sum()
        .reset_index()
    )
    emi_by_age_group['Age Group'] = emi_by_age_group['Age'].astype(str)

    fig_emi = px.bar(
        emi_by_age_group,
        x='Age Group',
        y='Total_EMI_per_month',
        color='Age Group',
        title=None
    )
    st.plotly_chart(fig_emi, use_container_width=True)
