import pytest
from unittest.mock import patch
from kid import Kid


@pytest.fixture
def kid_create():
    yield Kid(first_name="Jacek", second_name="Placek")


def test_kid_create(kid_create):
    assert kid_create._first_name == "Jacek"
    assert kid_create._second_name == "Placek"
    assert kid_create._marks == []


def test_kid_str(kid_create):
    string = str(kid_create)
    assert string == "Jacek Placek"


def test_kid_get_mark(kid_create):
    kid_create.get_mark(5)
    assert kid_create._marks == [5]
    kid_create.get_mark(3)
    assert kid_create._marks == [5, 3]