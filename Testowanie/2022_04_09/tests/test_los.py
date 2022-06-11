import pytest
from unittest.mock import patch
from los import losowanie

@patch('random.randint')
@pytest.mark.parametrize("number, result",
                         [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e"), (5, "e"), (6, "e")])
def test_losowanie(fake_randint, number, result):
    fake_randint.return_value = number
    wynik = losowanie()
    assert wynik == result
