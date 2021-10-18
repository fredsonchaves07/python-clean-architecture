from src.domain.entity.item import Item
from src.domain.repository.item_repository import ItemRepository


class ItemRepositoryMemory(ItemRepository):
    def __init__(self):
        self._items: list[Item] = [
            Item(1, "Guitarra", "Instrumentos Musicais", 1000, 100, 30, 10, 3),
            Item(2, "Amplificador", "Instrumentos Musicais", 500, 20, 10, 2),
            Item(3, "Cabos", "Instrumentos Musicais", 60, 10, 10, 10, 0.9),
        ]

    def find_by_id(self, id: int):
        for item in self._items:
            if item.id == id:
                return item
        raise Exception("Item not found!")
