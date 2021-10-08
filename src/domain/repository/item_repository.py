from abc import ABC

from src.domain.entity.item import Item


class ItemRepository(ABC):
    def find_by_id(self, id: int) -> Item:
        pass
