from pathlib import Path
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px

from tabs.tab1 import tab_1


def setup_tab_bar():
    tab_choice = option_menu(
        menu_title="Dashboard",
        options=[
            "Customer Financial Health"
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


main()
