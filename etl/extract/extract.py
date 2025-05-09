import pandas as pd


def extract_data() -> pd.DataFrame:
    credit_scores = pd.read_csv("data/raw_data/raw_data.csv")
    return (credit_scores)
