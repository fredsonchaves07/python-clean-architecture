from src.domain.entity.item import Item


def test_item():
    item = Item(1, "Guitarra", "Instrumentos musicais", 1000)
    assert item.id == 1


def test_calc_item_volum():
    item = Item(1, "Guitarra", "Instrumentos musicais", 1000, 100, 30, 10)
    assert item.get_volume() == 0.03


def test_calc_item_density():
    item = Item(1, "Guitarra", "Instrumentos musicais", 1000, 100, 30, 10, 3)
    assert item.get_density() == 100


def test_calc_item_freight():
    item = Item(1, "Guitarra", "Instrumentos musicais", 1000, 100, 30, 10, 3)
    assert item.get_freight() == 30


def test_calc_item_minimun_freigth():
    item = Item(2, "Cabo", "Instrumentos musicais", 30, 10, 10, 10, 0.9)
    assert item.get_freight() == 10
