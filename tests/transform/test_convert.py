import pytest
import numpy as np
from etl.transform.helper.convert import convert_credit_history_age


def test_convert_credit_history_age():
    # Valid cases
    assert convert_credit_history_age("2 Years and 6 Months") == 30
    assert convert_credit_history_age("0 Years and 3 Months") == 3
    assert convert_credit_history_age("15 Years and 0 Months") == 180

    # Extra whitespace
    assert convert_credit_history_age("  1 Years and 1 Months ") == 13

    # Invalid formats
    assert np.isnan(convert_credit_history_age("Two Years and Five Months"))
    assert np.isnan(convert_credit_history_age("3 years 4 months"))
    assert np.isnan(convert_credit_history_age("12"))
    assert np.isnan(convert_credit_history_age(None))
    assert np.isnan(convert_credit_history_age(24))
