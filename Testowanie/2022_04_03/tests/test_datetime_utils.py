import datetime

import datetime_utils
from unittest.mock import patch




def test_is_weekday_on_monday():
    with patch('datetime_utils.datetime') as fake_datetime:
        fake_datetime.today.return_value = datetime.datetime(2022, 4, 4)
        assert datetime_utils.is_weekday() is True

def test_is_weekday_on_saturday():
    with patch('datetime_utils.datetime') as fake_datetime:
        fake_datetime.today.return_value = datetime.datetime(2022, 4, 2)
        assert datetime_utils.is_weekday() is False
