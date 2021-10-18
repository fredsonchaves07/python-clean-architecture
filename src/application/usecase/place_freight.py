from src.application.dto.place_freight_input import PlaceFreightInput
from src.domain.repository.item_repository import ItemRepository


class PlaceFreight:
    def __init__(self, item_repository: ItemRepository):
        self._item_repository = item_repository

    def execute(self, input: PlaceFreightInput):
        freight = 0
        for order_item in input.get("items"):
            item = self._item_repository.find_by_id(order_item.get("id"))
            if not item:
                raise Exception("Item not found!")
            freight += item.get_freight()
        return freight
