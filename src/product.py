class Product:
    def __init__(
        self,
        description: str,
        category: str,
        height: float,
        width: float,
        density: float,
        weight: float,
    ) -> None:
        self.description = description
        self.category = category
        self.height = height
        self.width = width
        self.density = density
        self.weight = weight
