from src.freight import Freight
from src.item import Product


def test_freight_calc():
    product1 = Product("Guitarra", "Instrumentos Musicais", 20, 15, 10, 40)
    freihgt = Freight(product1)
    total = freihgt.calc_freight(250)
    assert total == 10000.0
