from src.category import Category
from src.product import Product


def test_category_init_and_counts() -> None:
    # Сбросим счётчики, если они есть
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("iPhone 15", "512GB", 200000, 5)
    p2 = Product("Samsung S23", "256GB", 180000, 3)

    c = Category("Смартфоны", "Современные смартфоны", [p1, p2])

    assert c.name == "Смартфоны"
    assert c.description == "Современные смартфоны"
    assert len(c.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_products_getter() -> None:
    p1 = Product("A", "Desc", 10, 2)
    p2 = Product("B", "Desc", 20, 3)
    category = Category("Cat", "Desc", [p1, p2])

    products_str = category.products
    assert "A, 10 руб. Остаток: 2 шт." in products_str
    assert "B, 20 руб. Остаток: 3 шт." in products_str
