import pytest
# -v wyswietli też wyniki dla passed

from working_calculator import add, multiply


class TestAdd:
    @pytest.mark.critical # -m by testowac tylko te ze znacznikami 'critical', a gdy -m 'not critical' to wszystkie poza tym
    def test_add_postive_numbers_gives_correct_result(self):
        assert add(1, 2) == 3

    def test_add_negative_numbers_gives_correct_result(self):
        assert add(1, -2) == -1

class TestMultiply:
    @pytest.mark.critical
    @pytest.mark.diffrent
    def test_multiply_postive_numbers_gives_correct_result(self):
        assert multiply(2,2) == 4

    def test_multiply_one_negative_one_postive_number_gives_correct_result(self):
        assert multiply(2,-2) == -4

    def test_multiply_negative_numbers_gives_correct_result(self):
        assert multiply(-2,-2) == 4

    def test_multiply_float_numbers_gives_correct_result(self):
        assert multiply(2.5, 2) == 5
    @pytest.mark.skip("This test is broken")
    def test_multiply_by_zero_gives_zero(self):
        print("Result should be 0 ", end="") # pytest -s -> wyświetli nam printy
        assert multiply(2,0) == 0