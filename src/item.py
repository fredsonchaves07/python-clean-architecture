from src.product import Product


class Item:
    def __init__(self, id_: int, product: Product, price: float) -> None:
        self.id = id_
        self.product = product
        self.price = price
