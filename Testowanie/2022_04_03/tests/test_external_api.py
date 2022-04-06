from unittest.mock import patch
import external_api


def test_simple():
    with patch('external_api.ExternalAPI.get_data') as fake_get_data:
        fake_get_data.return_value = ["a", "1", "b"]
        assert external_api.get_only_numbers() == ["1"]

def test_only_letters():
    with patch('external_api.ExternalAPI.get_data') as fake_get_data:
        fake_get_data.return_value = ["g", "r", "t"]
        assert external_api.get_only_numbers() == []