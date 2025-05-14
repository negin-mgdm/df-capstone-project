import pandas as pd
import streamlit as st
import plotly.express as px


def tab_1(df):
    st.header("Customer Financial Health")
    df['Customer_Label'] = df['Name'] + " (" + df['Customer_ID'] + ")"
    customer_options = df[['Customer_Label', 'Customer_ID']
                          ].drop_duplicates().sort_values('Customer_Label')
    selected_customer_label = st.selectbox(
        "Select a Customer", customer_options['Customer_Label'])
    selected_customer_id = customer_options[customer_options['Customer_Label']
                                            == selected_customer_label]['Customer_ID'].values[0]
    customer_data = df[df['Customer_ID'] == selected_customer_id].copy()

    latest = customer_data.sort_values('Month').iloc[-1]

    draw_customer_overview_metrics(latest)
    draw_balance_and_investment_graph(customer_data)
    draw_emi_investment_balance_graph(latest)


def draw_customer_overview_metrics(latest):
    income = latest['Monthly_Inhand_Salary']
    debt = latest['Outstanding_Debt']
    ratio = income / debt if debt != 0 else float('inf')
    st.subheader("Overview")
    col1, col2 = st.columns(2)

    with col1:
        if ratio >= 2.0:
            delta = "🟢 Healthy"
            delta_color = "normal"
        elif ratio >= 1.0:
            delta = "🟡 Moderate"
            delta_color = "off"
        else:
            delta = "🔴 At Risk"
            delta_color = "inverse"

        st.metric(
            label="Income vs Debt Ratio",
            value=f"{ratio:.2f}",
            delta=delta,
            delta_color=delta_color
        )

    with col2:
        st.metric(label="Annual Income",
                  value=f"${latest['Annual_Income']:,.0f}")

    col3, col4 = st.columns(2)

    with col3:
        st.metric(label="Occupation", value=latest['Occupation'])

    with col4:
        st.metric(label="Credit Score", value=latest['Credit_Score'])


def draw_balance_and_investment_graph(customer_data):
    st.subheader("Balance & Investment Over Time")
    combined_data = customer_data.set_index(
        'Month')[['Monthly_Balance', 'Amount_invested_monthly']].copy()
    combined_data.columns = ['Monthly Balance', 'Monthly Investment']

    fig = px.line(
        combined_data,
        x=combined_data.index,
        y=combined_data.columns,
        labels={'value': 'Amount', 'Month': 'Month'},
        title=None
    )
    fig.update_traces(mode='lines+markers')
    fig.update_traces(selector=dict(name='Monthly Balance'),
                      line=dict(color='blue'))
    fig.update_traces(selector=dict(name='Monthly Investment'),
                      line=dict(color='orange'))

    st.plotly_chart(fig, use_container_width=True)


def draw_emi_investment_balance_graph(latest):
    st.subheader("EMI vs Investment vs Balance")
    bar_data = pd.DataFrame({
        'Category': ['Total EMI', 'Monthly Investment', 'Monthly Balance'],
        'Amount': [latest['Total_EMI_per_month'], latest['Amount_invested_monthly'], latest['Monthly_Balance']]
    })

    fig_bar = px.bar(
        bar_data,
        x='Category',
        y='Amount',
        color='Category',
        color_discrete_map={
            'Total EMI': 'red',
            'Monthly Investment': 'orange',
            'Monthly Balance': 'blue'
        },
        title=None
    )
    fig_bar.update_layout(showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)
