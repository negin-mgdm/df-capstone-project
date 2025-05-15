import logging
import pandas as pd
import sys

from utils.logging_utils import setup_logger

logger = setup_logger(
    __name__,
    'run.log',
    level=logging.DEBUG
)


def extract_data() -> pd.DataFrame:
    try:
        credit_scores = pd.read_csv("data/raw_data/raw_data.csv")
        return credit_scores

    except FileNotFoundError:
        message = "Raw data file not found."
        terminate(message)
    except PermissionError:
        message = "Permission denied while reading raw data."
        terminate(message)
    except pd.errors.ParserError as e:
        message = f"Error parsing CSV: {e}"
        terminate(message)
    except Exception as e:
        message = f"Unexpected error during extraction: {e}"
        terminate(message)


def terminate(message):
    print(message)
    logger.setLevel(logging.ERROR)
    logger.error(f"Failed to extract data: {message}")
    print("Exiting the extract step.")
    sys.exit()
