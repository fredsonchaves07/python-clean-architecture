import pytest
from src.item import Item
from src.order import Order


def test_no_order_with_invalid_cpf():
    with pytest.raises(ValueError):
        Order("111.111.111-11")


def test_order():
    order = Order("847.903.332-05")
    order.add_item(Item(1, "Instrumentos Musicais", "Guitarra", 1000), 1)
    order.add_item(Item(2, "Instrumentos Musicais", "Amplificador", 500), 1)
    order.add_item(Item(3, "Instrumentos Musicais", "Cabos", 60), 3)
    total = order.get_total()
    assert total == 1680.00


def test_order_with_coupon():
    order = Order("847.903.332-05")
    order.add_item(Item(1, "Instrumentos Musicais", "Guitarra", 1000), 1)
    order.add_item(Item(2, "Instrumentos Musicais", "Amplificador", 500), 1)
    order.add_item(Item(3, "Instrumentos Musicais", "Cabos", 60), 3)
    order.add_coupon("VALE20", 20)
    total = order.get_total()
    assert total == 1344.00
