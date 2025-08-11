from _pytest.monkeypatch import MonkeyPatch

from src.product import Product


def test_product_init() -> None:
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_price_setter(monkeypatch: MonkeyPatch) -> None:
    p = Product("Test", "Desc", 100, 1)

    # Установка корректной цены
    p.price = 150
    assert p.price == 150

    # Попытка установить отрицательную цену — цена не меняется
    p.price = -10
    assert p.price == 150

    # Попытка установить 0 — цена не меняется
    p.price = 0
    assert p.price == 150

    # Понижение цены с подтверждением "y"
    monkeypatch.setattr("builtins.input", lambda _: "y")
    p.price = 100
    assert p.price == 100

    # Понижение цены с отменой "n"
    monkeypatch.setattr("builtins.input", lambda _: "n")
    p.price = 90
    assert p.price == 100  # цена не меняется


def test_product_str() -> None:
    product = Product("Test Product", "Some description", 80.0, 15)
    assert str(product) == "Test Product, 80.0 руб. Остаток: 15 шт."


def test_product_addition() -> None:
    p1 = Product("P1", "desc", 100.0, 2)  # 200
    p2 = Product("P2", "desc", 150.0, 3)  # 450
    assert p1 + p2 == 650.0
