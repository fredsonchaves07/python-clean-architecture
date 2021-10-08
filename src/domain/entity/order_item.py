class OrderItem:
    def __init__(self, id_item: int, price: float, quantity: int) -> None:
        self.id_item = id_item
        self.price = price
        self.quantity = quantity

    def get_total(self) -> float:
        return self.price * self.quantity
