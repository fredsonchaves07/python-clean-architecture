from typing import List


class Person:
    def __init__(self, cpf: str):
        self.cpf = cpf


class Product:
    def __init__(self, description: str, price: float, quantity: int):
        self.description = description
        self.price = price
        self.quantity = quantity


class Order:
    def __init__(self, person: Person, products: List[Product]):
        self.person = person
        self.products = products
        self.amount = 0
        for product in products:
            self.amount += product.price

    def calculate_discount(self, discount: float):
        self.amount -= self.amount * discount
