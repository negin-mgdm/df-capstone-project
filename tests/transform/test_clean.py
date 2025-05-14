import numpy as np
from etl.transform.helper.clean import (
    clean_special_chars_string,
    clean_special_chars_number,
    clean_credit_history_age_amount,
    clean_payment_of_min_amount,
    clean_payment_behaviour
)


def test_clean_special_chars_string():
    assert clean_special_chars_string("Valid Name") == "Valid Name"
    assert np.isnan(clean_special_chars_string("Name123"))
    assert np.isnan(clean_special_chars_string("Name!@#"))
    assert np.isnan(clean_special_chars_string(12345))


def test_clean_special_chars_number():
    assert clean_special_chars_number("123.456") == 123.46
    assert clean_special_chars_number("$99.99") == 99.99
    assert clean_special_chars_number("") is np.nan
    assert clean_special_chars_number(None) is np.nan
    assert clean_special_chars_number("invalid") is np.nan
    assert clean_special_chars_number(500) == 500.00
    assert clean_special_chars_number(99.994) == 99.99


def test_clean_credit_history_age_amount():
    assert clean_credit_history_age_amount(
        "2 Years and 5 Months") == "2 Years and 5 Months"
    assert np.isnan(clean_credit_history_age_amount(
        "Two Years and Five Months"))
    assert np.isnan(clean_credit_history_age_amount("2 Yrs, 5 Mths"))
    assert np.isnan(clean_credit_history_age_amount(25))


def test_clean_payment_of_min_amount():
    assert np.isnan(clean_payment_of_min_amount("NM"))
    assert clean_payment_of_min_amount("Yes") == "Yes"
    assert clean_payment_of_min_amount(" no ") == "no"
    assert np.isnan(clean_payment_of_min_amount("123"))
    assert np.isnan(clean_payment_of_min_amount(None))


def test_clean_payment_behaviour():
    assert clean_payment_behaviour(
        "High_spent_Small_value_payments") == "High_spent_Small_value_payments"
    assert clean_payment_behaviour(
        "Low_spent_Large_value_payments") == "Low_spent_Large_value_payments"
    assert np.isnan(clean_payment_behaviour(
        "Medium_spent_Large_value_payments"))
    assert np.isnan(clean_payment_behaviour("Invalid Format"))
    assert np.isnan(clean_payment_behaviour(None))
