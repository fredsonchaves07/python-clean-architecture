from src.domain.entity.item import Item
from src.domain.repository.item_repository import ItemRepository


class ItemRepositoryMemory(ItemRepository):
    def __init__(self):
        self._items: list[Item] = [
            Item(1, "Guitarra", "Instrumentos Musicais", 1000),
            Item(2, "Amplificador", "Instrumentos Musicais", 500),
            Item(3, "Cabos", "Instrumentos Musicais", 60),
        ]

    def find_by_id(self, id: int):
        for item in self._items:
            if item.id == id:
                return item
        raise Exception("Item not found!")
