def load_data(transformed_data):
    transformed_data.to_csv(
        "data/processed_data/processed_data.csv", index=False)
