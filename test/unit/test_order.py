import pytest
from src.domain.entity.coupon import Coupon
from src.domain.entity.item import Item
from src.domain.entity.order import Order


def test_no_order_with_invalid_cpf():
    with pytest.raises(ValueError):
        Order("111.111.111-11")


def test_order():
    order = Order("847.903.332-05")
    order.add_item(Item(1, "Guitarra", "Instrumentos Musicais", 1000), 1)
    order.add_item(Item(2, "Amplificador", "Instrumentos Musicais", 500), 1)
    order.add_item(Item(3, "Cabos", "Instrumentos Musicais", 60), 3)
    total = order.get_total()
    assert total == 1680.00


def test_order_with_coupon():
    order = Order("847.903.332-05", "2021-10-10")
    coupon = Coupon("VALE20", 20, "2021-10-10")
    order.add_item(Item(1, "Guitarra", "Instrumentos Musicais", 1000), 1)
    order.add_item(Item(2, "Amplificador", "Instrumentos Musicais", 500), 1)
    order.add_item(Item(3, "Cabos", "Instrumentos Musicais", 60), 3)
    order.add_coupon(coupon)
    total = order.get_total()
    assert total == 1344.00


def test_no_order_with_expired_coupon():
    order = Order("847.903.332-05", "2021-10-10")
    coupon_expired = Coupon("VALE20", 20, "2021-04-29")
    order.add_item(Item(1, "Guitarra", "Instrumentos Musicais", 1000), 1)
    order.add_item(Item(2, "Amplificador", "Instrumentos Musicais", 500), 1)
    order.add_item(Item(3, "Cabos", "Instrumentos Musicais", 60), 3)
    with pytest.raises(Exception):
        order.add_coupon(coupon_expired)

def test_order_with_order_code():
    order = Order("847.903.332-05", "2021-03-01")
    order.add_item(Item(1, "Guitarra", "Instrumentos Musicais", 1000), 1)
    order.add_item(Item(2, "Amplificador", "Instrumentos Musicais", 500), 1)
    order.add_item(Item(3, "Cabos", "Instrumentos Musicais", 60), 3)
    code = order.order_code
    assert code.code == "2021000000001"
