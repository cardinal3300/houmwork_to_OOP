import pytest

from src.base_product import BaseProduct


class DummyProduct(BaseProduct):
    """Простой класс для тестов BaseProduct"""

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)


def test_base_product_str() -> None:
    product = DummyProduct("Test", "Test product", 100.0, 3)
    assert str(product) == "Test, 100.0 руб. Остаток: 3 шт."


def test_base_product_add_same_type() -> None:
    p1 = DummyProduct("Item1", "Desc1", 50.0, 2)  # 100.0
    p2 = DummyProduct("Item2", "Desc2", 25.0, 4)  # 100.0
    assert p1 + p2 == 200.0


def test_base_product_add_different_type_raises() -> None:
    class Other:
        pass

    p1 = DummyProduct("Item1", "Desc1", 50.0, 2)
    with pytest.raises(TypeError):
        _ = p1 + Other()
