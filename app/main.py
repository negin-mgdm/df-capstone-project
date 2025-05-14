from pathlib import Path
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

from tabs.tab3 import tab_3
from tabs.tab2 import setup_filter, tab_2
from tabs.tab1 import tab_1


def setup_tab_bar():
    tab_choice = option_menu(
        menu_title="Dashboard",
        options=[
            "Customer Financial Health",
            "Segment Analysis & Trends",
            "Risk & Behaviour Insights"
        ],
        icons=["activity", "bar-chart-line", "exclamation-triangle"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#0e1117"},
            "icon": {"color": "white", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "2px",
                "--hover-color": "#6c757d"
            },
            "nav-link-selected": {"background-color": "#ff4b4b", "color": "white"},
        }
    )
    return tab_choice


def main():
    BASE_DIR = Path("main.py").resolve().parent
    DATA_PATH = BASE_DIR / 'data' / "processed_data" / "processed_data.csv"

    df = pd.read_csv(DATA_PATH)

    # --- SIDEBAR MENU ---
    with st.sidebar:
        tab_choice = setup_tab_bar()

    # --- TAB 1 ---
    if tab_choice == "Customer Financial Health":
        tab_1(df)

    # --- TAB 2 ---
    elif tab_choice == "Segment Analysis & Trends":
        selected_credit_score, selected_age, selected_history = setup_filter(
            df)
        tab_2(df, selected_credit_score, selected_age, selected_history)

    # --- TAB 3 ---
    elif tab_choice == "Risk & Behaviour Insights":
        tab_3(df)


main()
