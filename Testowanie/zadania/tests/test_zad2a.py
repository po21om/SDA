import pytest
from zad2 import odd_indexes

@pytest.mark.parametrize("string,result", [("ZaBaWkA", "aak"), ("",""), ("a",""), (3579, "59")])
def test_odd_indexes(string, result):
    assert odd_indexes(string) == result
