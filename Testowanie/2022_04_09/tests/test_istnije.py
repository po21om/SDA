import os
from unittest.mock import patch
from istnieje import istnieje

def test_istnieje():
    wynik = istnieje()
    assert wynik == 200


def test_istnieje_fake_true():
    with patch('istnieje.os.path.exists') as fake_path:
            fake_path.return_value = True
            wynik = istnieje()
            assert wynik == 50


def test_istnieje_fake_false():
    with patch('istnieje.os.path.exists') as fake_path:
            fake_path.return_value = False
            wynik = istnieje()
            assert wynik == 200


@patch('os.path.exists')
def test_ist_true(to_jest_moj_mock):
    # print('---------------------')
    # print(type(to_jest_moj_mock))
    # print('---')
    # print(dir(to_jest_moj_mock))
    to_jest_moj_mock.return_value = True
    wynik = istnieje()
    assert wynik == 50

@patch('os.path.exists')
def test_ist_false(to_jest_moj_mock):
    to_jest_moj_mock.return_value = False
    wynik = istnieje()
    assert wynik == 200