from unittest import mock
import pandas as pd

from etl.extract.extract import extract_data


@mock.patch("etl.extract.extract.terminate")
def test_extract_data_success(mock_terminate):
    sample_df = pd.DataFrame({"A": [1], "B": [2]})
    with mock.patch("etl.extract.extract.pd.read_csv", return_value=sample_df):
        df = extract_data()
        pd.testing.assert_frame_equal(df, sample_df)


@mock.patch("etl.extract.extract.terminate")
def test_extract_data_file_not_found(mock_terminate):
    with mock.patch("etl.extract.extract.pd.read_csv", side_effect=FileNotFoundError):
        extract_data()
        mock_terminate.assert_called_once_with("Raw data file not found.")


@mock.patch("etl.extract.extract.terminate")
def test_extract_data_permission_error(mock_terminate):
    with mock.patch("etl.extract.extract.pd.read_csv", side_effect=PermissionError):
        extract_data()
        mock_terminate.assert_called_once_with(
            "Permission denied while reading raw data.")


@mock.patch("etl.extract.extract.terminate")
def test_extract_data_parser_error(mock_terminate):
    with mock.patch("etl.extract.extract.pd.read_csv", side_effect=pd.errors.ParserError("parse issue")):
        extract_data()
        mock_terminate.assert_called_once_with(
            "Error parsing CSV: parse issue")


@mock.patch("etl.extract.extract.terminate")
def test_extract_data_unexpected_error(mock_terminate):
    with mock.patch("etl.extract.extract.pd.read_csv", side_effect=Exception("Boom")):
        extract_data()
        mock_terminate.assert_called_once_with(
            "Unexpected error during extraction: Boom")
