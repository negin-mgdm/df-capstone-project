import os
import sys


def load_data(transformed_data):
    output_path = "data/transformed_data/cleaned_data.csv"

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
    print("Exiting the load step.")
    sys.exit()
