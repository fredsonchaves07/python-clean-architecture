from src.application.usecase.place_order import PlaceOrder
from src.infra.repository.memory.item_repository_memory import ItemRepositoryMemory
from src.infra.repository.memory.order_repository_memory import OrderRepositoryMemory


def test_place_order():
    input = {
        "cpf": "847.903.332-05",
        "order_items": [
            {"id": 1, "quantity": 1},
            {"id": 2, "quantity": 1},
            {"id": 3, "quantity": 3},
        ],
    }
    place_order = PlaceOrder(ItemRepositoryMemory(), OrderRepositoryMemory())
    output = place_order.execute(input)
    assert output.total == 1680.00
