def load_data(transformed_data):
    transformed_data.to_csv(
        "data/transformed_data/cleaned_data.csv", index=False)
