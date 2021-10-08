from src.domain.entity.order import Order
from src.domain.repository.order_repository import OrderRepository


class OrderRepositoryMemory(OrderRepository):
    def __init__(self) -> None:
        self.orders = []

    def save(self, order: Order) -> None:
        self.orders.append(order)
