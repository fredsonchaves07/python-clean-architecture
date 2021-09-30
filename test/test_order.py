import pytest
from src.coupon import Coupon
from src.item import Item
from src.order import Order
from src.product import Product


def test_no_order_with_invalid_cpf():
    with pytest.raises(ValueError):
        Order("111.111.111-11")


def test_order():
    order = Order("847.903.332-05")
    product1 = Product("Guitarra", "Instrumentos Musicais", 20, 15, 10, 40)
    product2 = Product("Amplificador", "Instrumentos Musicais", 100, 30, 10, 3)
    product3 = Product("Cabos", "Instrumentos Musicais", 200, 100, 50, 1)
    order.add_item(Item(1, product1, 1000), 1)
    order.add_item(Item(2, product2, 500), 1)
    order.add_item(Item(3, product3, 60), 3)
    total = order.get_total()
    assert total == 1680.00


def test_order_with_coupon():
    order = Order("847.903.332-05")
    coupon = Coupon("VALE20", 20)
    product1 = Product("Guitarra", "Instrumentos Musicais", 20, 15, 10, 40)
    product2 = Product("Amplificador", "Instrumentos Musicais", 100, 30, 10, 3)
    product3 = Product("Cabos", "Instrumentos Musicais", 200, 100, 50, 1)
    order.add_item(Item(1, product1, 1000), 1)
    order.add_item(Item(2, product2, 500), 1)
    order.add_item(Item(3, product3, 60), 3)
    order.add_coupon(coupon)
    total = order.get_total()
    assert total == 1344.00


def test_no_order_with_expired_coupon():
    order = Order("847.903.332-05")
    coupon_expired = Coupon("VALE20", 20, "29-09-2021")
    product1 = Product("Guitarra", "Instrumentos Musicais", 20, 15, 10, 40)
    product2 = Product("Amplificador", "Instrumentos Musicais", 100, 30, 10, 3)
    product3 = Product("Cabos", "Instrumentos Musicais", 200, 100, 50, 1)
    order.add_item(Item(1, product1, 1000), 1)
    order.add_item(Item(2, product2, 500), 1)
    order.add_item(Item(3, product3, 60), 3)
    with pytest.raises(Exception):
        order.add_coupon(coupon_expired)
