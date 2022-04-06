import pytest


@pytest.fixture()
def test_starting_info():
    print("\n3\n2\n1\n...\nTest is starting")

@pytest.fixture()
def test_finishing_info():
    yield
    print("\nBye Bye\nB..\nTest died xxx")

@pytest.fixture()
def test_welcome():
    print("\nHello")
    yield
    print("Bye")


@pytest.fixture()
def print_test_starting(test_welcome):
    print("The test is starting")
    yield
    print("\nTest ended")


def test_1(test_starting_info):
    assert True


def test_2(print_test_starting):
    assert True


def test_3(test_finishing_info):

    assert True

