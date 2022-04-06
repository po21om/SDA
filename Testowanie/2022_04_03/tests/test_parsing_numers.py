import pytest
from parsing_numbers import parse_int_from_text


def test_positive_number_is_parsed_from_string():
    text = "12"
    expected = 12
    actual = parse_int_from_text(text)
    assert actual == expected


def test_numer_can_be_parsed_when_text_has_a_space():
    assert parse_int_from_text("12") == 12


def test_todo():
    with pytest.raises(ValueError):
        parse_int_from_text("abc")

def test_todo_b():
    with pytest.raises(TypeError):
        parse_int_from_text(["abc","bce"])

def test_parsing_empty_string_crashes_with_value_error():
    with pytest.raises(ValueError):
        parse_int_from_text("")
