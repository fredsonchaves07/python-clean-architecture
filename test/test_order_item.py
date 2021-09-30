from src.order_item import OrderItem


def test_order_item():
    order_item = OrderItem(1, 1000, 2)
    total = order_item.get_total()
    assert total == 2000
