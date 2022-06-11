import pytest
from zad5 import Magazine
from zad5 import Product

@pytest.fixture
def ready_products():
    prod1 = Product(1)
    prod2 = Product(2)
    prod3 = Product(3)
    prod4 = Product(4)
    prod5 = Product(5)

def test_add(ready_products):
    mag = Magazine(12)
    mag.add(prod1)
    mag.add(prod2)
    mag.add(prod3)
    mag.add(prod4)
    assert mag.vol == 2