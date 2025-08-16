from src.product import LawnGrass, Product, Smartphone


def test_product_repr() -> None:
    p = Product("Телефон", "Описание", 1000.0, 5)
    expected = "Product(name='Телефон', description='Описание', price=1000.0, quantity=5)"
    assert repr(p) == expected


def test_smartphone_repr() -> None:
    s = Smartphone("Смартфон", "Флагман", 50000.0, 10, efficiency=9.8, model="X100", memory=256, color="черный")
    expected = (
        "Smartphone(name='Смартфон', description='Флагман', price=50000.0, quantity=10, "
        "efficiency=9.8, model='X100', memory=256, color='черный')"
    )
    assert repr(s) == expected


def test_lawngrass_repr() -> None:
    g = LawnGrass(
        "Газон", "Семена травы", 200.0, 100, country="Россия", germination_period="7-14 дней", color="зеленый"
    )
    expected = (
        "LawnGrass(name='Газон', description='Семена травы', price=200.0, quantity=100, "
        "country='Россия', germination_period='7-14 дней', color='зеленый')"
    )
    assert repr(g) == expected
