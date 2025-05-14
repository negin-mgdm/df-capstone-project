import pandas as pd
from unittest import mock

from etl.load.load import load_data


@mock.patch("etl.load.load.terminate")
def test_load_data_success(mock_terminate, tmp_path):
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})

    with mock.patch("etl.load.load.os.makedirs"), \
            mock.patch.object(df, "to_csv") as mock_to_csv:
        load_data(df)
        mock_to_csv.assert_called_once_with(
            "data/processed_data/processed_data.csv", index=False)


@mock.patch("etl.load.load.terminate")
def test_load_data_file_not_found(mock_terminate):
    df = pd.DataFrame()
    with mock.patch("etl.load.load.os.makedirs", side_effect=FileNotFoundError):
        load_data(df)
        mock_terminate.assert_called_once_with("Directory not found.")


@mock.patch("etl.load.load.terminate")
def test_load_data_permission_error(mock_terminate):
    df = pd.DataFrame()
    with mock.patch("etl.load.load.os.makedirs", side_effect=PermissionError):
        load_data(df)
        mock_terminate.assert_called_once_with("Permission denied.")


@mock.patch("etl.load.load.terminate")
def test_load_data_os_error(mock_terminate):
    df = pd.DataFrame()
    with mock.patch("etl.load.load.os.makedirs", side_effect=OSError("Disk full")):
        load_data(df)
        mock_terminate.assert_called_once_with(
            "OS error while saving file: Disk full")


@mock.patch("etl.load.load.terminate")
def test_load_data_type_error(mock_terminate):
    # simulate transformed_data.to_csv raising a TypeError
    df = pd.DataFrame()
    with mock.patch("etl.load.load.os.makedirs"), \
            mock.patch.object(df, "to_csv", side_effect=TypeError("Invalid type")):
        load_data(df)
        mock_terminate.assert_called_once_with(
            "Data contains invalid values or types: Invalid type")


@mock.patch("etl.load.load.terminate")
def test_load_data_unexpected_error(mock_terminate):
    df = pd.DataFrame()
    with mock.patch("etl.load.load.os.makedirs"), \
            mock.patch.object(df, "to_csv", side_effect=Exception("Unexpected!")):
        load_data(df)
        mock_terminate.assert_called_once_with("Unexpected error: Unexpected!")
