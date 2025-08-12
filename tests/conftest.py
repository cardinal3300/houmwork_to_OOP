import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


# ---------- Продукты ----------
@pytest.fixture
def product_phone() -> Product:
    return Product("Телефон", "Смартфон", 10000, 2)


@pytest.fixture
def product_laptop() -> Product:
    return Product("Ноутбук", "Игровой", 50000, 1)


@pytest.fixture
def smartphone_iphone() -> Smartphone:
    return Smartphone("iPhone", "Описание", 50000, 1, 95.0, "13 Pro", 128, "черный")


@pytest.fixture
def lawn_grass() -> LawnGrass:
    return LawnGrass("Газон", "Описание", 1000, 5, "Россия", "7", "зеленый")


# ---------- Категории ----------
@pytest.fixture
def category_electronics(product_phone, product_laptop) -> Category:
    return Category("Электроника", "Описание", [product_phone, product_laptop])


@pytest.fixture
def category_empty() -> Category:
    return Category("Электроника", "Описание")
