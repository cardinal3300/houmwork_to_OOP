import pytest

from src.product import Product, Smartphone, LawnGrass


def test_product_str(product_phone: Product) -> None:
    assert str(product_phone) == "Телефон, 10000 руб. Остаток: 2 шт."


def test_product_add_same_type(product_phone: Product) -> None:
    p2 = Product("Телефон", "Смартфон", 10000, 3)
    assert product_phone + p2 == 10000 * 2 + 10000 * 3


def test_product_add_different_type(product_phone: Product, smartphone_iphone: Smartphone) -> None:
    with pytest.raises(TypeError):
        _ = product_phone + smartphone_iphone


def test_price_setter_positive(product_phone: Product) -> None:
    product_phone.price = 15000
    assert product_phone.price == 15000


def test_price_setter_zero_or_negative(product_phone: Product, capsys) -> None:
    product_phone.price = -500
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_price_setter_decrease_confirm(product_phone: Product, monkeypatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product_phone.price = 9000
    assert product_phone.price == 9000


def test_price_setter_decrease_cancel(product_phone: Product, monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product_phone.price = 9000
    assert product_phone.price == 10000
    captured = capsys.readouterr()
    assert "Снижение цены отменено" in captured.out


def test_new_product() -> None:
    data = {"name": "Телефон", "description": "Смартфон", "price": 10000, "quantity": 2}
    p = Product.new_product(data)
    assert isinstance(p, Product)


def test_smartphone_init(smartphone_iphone: Smartphone) -> None:
    assert smartphone_iphone.model == "13 Pro"


def test_lawngrass_init(lawn_grass: LawnGrass) -> None:
    assert lawn_grass.country == "Россия"
