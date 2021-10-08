class Item:
    def __init__(
        self,
        id_: int,
        description: str,
        category: str,
        price: float,
        height: float = 0,
        width: float = 0,
        length: float = 0,
        weight: float = 0,
    ) -> None:
        self.id = id_
        self.description = description
        self.category = category
        self.price = price
        self.height = height
        self.width = width
        self.length = length
        self.weight = weight

    def get_volume(self):
        return self.width / 100 * self.height / 100 * self.length / 100

    def get_density(self):
        return self.weight / self.get_volume()

    def get_freight(self):
        freight = 1000 * self.get_volume() * self.get_density() / 100
        return 10 if freight < 10 else freight
