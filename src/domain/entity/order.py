from datetime import datetime
from typing import List

from src.domain.entity.coupon import Coupon
from src.domain.entity.cpf import Cpf
from src.domain.entity.item import Item
from src.domain.entity.order_item import OrderItem


class Order:
    def __init__(self, cpf: str, issue_date: str = None) -> None:
        self._cpf: Cpf = Cpf(cpf)
        self._order_items: List[OrderItem] = []
        self._coupon: Coupon = None
        self._freight = 0
        if not issue_date:
            self._issue_date = datetime.now().strftime("%d-%m-%Y")
        else:
            self._issue_date = issue_date

    def add_item(self, item: Item, quantity: int) -> None:
        self._order_items.append(OrderItem(item.id, item.price, quantity))

    def add_coupon(self, coupon: Coupon) -> None:
        if coupon.is_expired(self._issue_date):
            raise Exception("Coupon expired")
        self._coupon = coupon

    def get_total(self) -> float:
        total: float = 0
        for order_item in self._order_items:
            total += order_item.get_total()
        if self._coupon:
            total -= (total * self._coupon.percentage) / 100
        return total
