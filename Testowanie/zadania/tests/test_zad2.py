import zad2


def test_odd_indexes_string():
    string = "ZaBaWkA"
    assert zad2.odd_indexes(string) == "aak"

def test_odd_indexes_no_string():
    assert zad2.odd_indexes("") == ""

def test_odd_indexes_one_letter_string():
    assert zad2.odd_indexes("a") == ""

def testt_odd_indexes_int():
    assert zad2.odd_indexes(3579) == "59"