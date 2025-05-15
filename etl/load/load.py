import logging
import os
import sys

from utils.logging_utils import setup_logger

logger = setup_logger(
    __name__,
    'run.log',
    level=logging.DEBUG
)


def load_data(transformed_data):
    output_path = "data/processed_data/processed_data.csv"

    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        transformed_data.to_csv(output_path, index=False)
        print(f"Data successfully saved to {output_path}")

    except FileNotFoundError:
        message = "Directory not found."
        terminate(message)
    except PermissionError:
        message = "Permission denied."
        terminate(message)
    except OSError as e:
        message = f"OS error while saving file: {e}"
        terminate(message)
    except (TypeError, ValueError) as e:
        message = f"Data contains invalid values or types: {e}"
        terminate(message)
    except Exception as e:
        message = f"Unexpected error: {e}"
        terminate(message)


def terminate(message):
    print(message)
    logger.setLevel(logging.ERROR)
    logger.error(f"Failed to extract data: {message}")
    print("Exiting the load step.")
    sys.exit()
