from app.entity import Order, Person, Product


def test_order():
    person = Person("15805772027")

    products = [
        Product("Computador", 4500.99, 10),
        Product("Geladeira", 3051.80, 1),
        Product("Televisão", 5600.26, 5),
    ]

    order = Order(person, products)

    assert order.person.cpf == person.cpf
    for index in range(len(products)):
        assert order.products[index].description == products[index].description
        assert order.products[index].quantity == products[index].quantity
        assert order.products[index].price == products[index].price


def test_discount_coupon():
    person = Person("15805772027")
    product = Product("Computador", 1500.99, 2)
    coupon = 10
    order = Order(person, product)

    assert order.calculate_discount(coupon) == product.price - (product * coupon)
