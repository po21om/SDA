from unittest.mock import patch
import pytest
from zad4 import _get_data
from zad4 import get_avg


@pytest.mark.parametrize("number, result",
                         [(1, 1.0), (2, 1.5), (3, 2.0), (4, 2.5), (5, 3.0), (6, 3.5), (7, 4.0), (8, 4.5), (9, 5.0)])
def test_get_avg(number, result):
    assert get_avg(number) == result

@patch('zad4._get_data')
@pytest.mark.parametrize("number, result",
                         [("24", 3.0), ("576", 6.0), ("1030", 1.0), ("1000", 0.25)])
def test_get_avg_with_mock(fake_data, number, result):
    fake_data.return_value = number
    wynik = get_avg(1)
    assert wynik == result

