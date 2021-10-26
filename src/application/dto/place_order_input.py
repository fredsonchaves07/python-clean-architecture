class PlaceOrderInput:
    def __init__(self, cpf: str, order_items: list, coupon: str = None):
        self.cpf = cpf
        self.order_items = order_items
        self.coupon = coupon