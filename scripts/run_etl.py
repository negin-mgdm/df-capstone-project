import os
import sys
from config.env_config import setup_env
from etl.extract.extract import extract_data
from etl.load.load import load_data
from etl.transform.transform import transform_data


def main():
    if len(sys.argv) > 1:
        run_env_setup()

    extracted_data = extract_data()
    transformed_data = transform_data(extracted_data)
    load_data(transformed_data)

    print(
        f"ETL pipeline run successfully in "
        f'{os.getenv("ENV", "error")} environment!'
    )


def run_env_setup():
    print("Setting up environment...")
    setup_env(sys.argv)
    print("Environment setup complete.")


if __name__ == "__main__":
    main()
