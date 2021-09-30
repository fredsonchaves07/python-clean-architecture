from src.product import Product


class Freight:
    def __init__(self, product: Product) -> None:
        self._value_minimun = 10
        self.product = product

    def calc_freight(self, distance: float) -> float:
        total = distance * self._calc_cubage() * self._calc_density()
        if total < self._value_minimun:
            return self._value_minimun
        return total

    def _calc_cubage(self) -> float:
        return self.product.height * self.product.width * self.product.density

    def _calc_density(self) -> float:
        return self.product.weight / self._calc_cubage()
