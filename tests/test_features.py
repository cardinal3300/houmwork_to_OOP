import pytest

from src.base_product import BaseProduct
from src.category import Category
from src.product import Product


def test_product_with_zero_quantity_raises_error() -> None:
    """Проверяем, что при нулевом количестве выбрасывается ValueError."""

    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен."):
        Product("Тестовый товар", "Описание", 100.0, 0)


def test_average_price_with_products() -> None:
    """Проверяем корректность расчёта средней цены при наличии товаров."""

    p1 = Product("iPhone 15", "512GB", 210000.0, 8)
    p2 = Product("Xiaomi", "128GB", 31000.0, 5)

    category = Category("Смартфоны", "Мобильные устройства", [p1, p2])
    expected = (210000.0 + 31000.0) / 2
    assert category.middle_price() == expected


def test_average_price_with_no_products() -> None:
    """Проверяем, что при отсутствии товаров средняя цена = 0."""

    category = Category("Пустая", "Нет товаров", [])
    assert category.middle_price() == 0.0


def test_product_with_non_positive_price_raises_error() -> None:
    """При цене меньше или равной нулю должен выбрасываться ValueError."""

    with pytest.raises(ValueError, match="Цена должна быть больше нуля, получено: 0"):
        BaseProduct("Test", "Description", 0.0, 5)

    with pytest.raises(ValueError, match="Цена должна быть больше нуля, получено: -50"):
        BaseProduct("Test", "Description", -50.0, 5)


def test_product_with_negative_quantity_raises_error() -> None:
    """При отрицательном количестве должен выбрасываться ValueError."""

    with pytest.raises(ValueError, match="Количество не может быть отрицательным, получено: -3"):
        BaseProduct("Test", "Description", 100.0, -3)
