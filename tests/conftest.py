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
def category_electronics(product_phone: Product, product_laptop: Product) -> Category:
    return Category("Электроника", "Описание", [product_phone, product_laptop])


@pytest.fixture
def category_empty() -> Category:
    return Category("Электроника", "Описание")


@pytest.fixture
def sample_products() -> tuple[Smartphone, Smartphone, LawnGrass]:
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    return smartphone1, smartphone2, grass


@pytest.fixture
def smartphone1(sample_products) -> Smartphone:
    return sample_products[0]


@pytest.fixture
def cat(sample_products):
    return Category("Хиты продаж", "Лучшие товары", list(sample_products))
