class PlaceOrderInput:
    def __init__(self, cpf: str, order_items: list):
        self.cpf = cpf
        self.order_items = order_items
