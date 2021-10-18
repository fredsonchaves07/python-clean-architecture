from src.application.usecase.place_freight import PlaceFreight
from src.infra.repository.memory.item_repository_memory import ItemRepositoryMemory


def test_place_freight():
    input = {
        "items": [
            {"id": 1, "quantity": 1},
            {"id": 2, "quantity": 1},
            {"id": 3, "quantity": 3},
        ]
    }
    freight = PlaceFreight(ItemRepositoryMemory())
    output = freight.execute(input)
    assert output == 50.0
