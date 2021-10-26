from src.application.dto.place_order_input import PlaceOrderInput
from src.application.dto.place_order_output import PlaceOrderOutput
from src.domain.entity.order import Order
from src.domain.repository.item_repository import ItemRepository
from src.domain.repository.order_repository import OrderRepository


class PlaceOrder:
    def __init__(
        self, item_repository: ItemRepository, order_repository: OrderRepository
    ):
        self._item_repository = item_repository
        self._order_repository = order_repository

    def execute(self, input: PlaceOrderInput) -> PlaceOrderOutput:
        order = Order(input.get("cpf"))
        for order_item in input.get("order_items"):
            item = self._item_repository.find_by_id(order_item.get("id"))
            if not item:
                raise Exception("Item not found!")
            order.add_item(item, order_item.get("quantity"))
        self._order_repository.save(order)
        total = order.get_total()
        return PlaceOrderOutput(total)
