from src.product import Product

from src.category import Category


def test_category_init_and_counts():
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