from abc import ABC

from src.domain.entity.order import Order


class OrderRepository(ABC):
    def save(self, order: Order) -> None:
        pass
