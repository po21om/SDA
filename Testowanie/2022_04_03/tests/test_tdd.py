import pytest
from tdd import oceny


@pytest.mark.parametrize("punkty, ocena",
                         [(0, "ndst"), (24, "ndst"),
                          (25, "dop"), (27, "dop"),
                          (28, "dst"), (37, "dst"),
                          (38, "db"), (46, "db"),
                          (47, "bdb"), (50, "bdb"),
                          (-1, "Punkty poza skalą."), (51, "Punkty poza skalą.")])
def test_oceny(punkty, ocena):
    wynik = oceny(punkty)
    assert wynik == ocena
