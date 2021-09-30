from typing import List

from src.coupon import Coupon
from src.cpf import Cpf
from src.item import Item
from src.order_item import OrderItem


class Order:
    def __init__(self, cpf: str) -> None:
        self._cpf: Cpf = Cpf(cpf)
        self._order_items: List[OrderItem] = []
        self._coupon: Coupon = None

    def add_item(self, item: Item, quantity: int) -> None:
        self._order_items.append(OrderItem(item.id, item.price, quantity))

    def add_coupon(self, coupon: Coupon) -> None:
        if coupon.is_expired():
            raise Exception("Coupon expired")
        self._coupon = coupon

    def get_total(self) -> float:
        total: float = 0.0
        for order_item in self._order_items:
            total += order_item.get_total()
        if self._coupon:
            total -= (total * self._coupon.percentage) / 100
        return total
