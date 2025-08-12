import pytest
from src.category import Category, CategoryIterator
from src.product import Product, Smartphone, LawnGrass


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


def test_category_str() -> None:
    p1 = Product("Phone", "desc", 100.0, 2)
    p2 = Product("Tablet", "desc", 200.0, 3)
    category = Category("Электроника", "Гаджеты", [p1, p2])
    assert str(category) == "Электроника, количество продуктов: 5 шт."


@pytest.fixture
def sample_products():
    """Возвращает тестовые объекты продуктов."""
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    return smartphone1, smartphone2, grass


def test_add_product_allows_only_products(sample_products):
    """Проверка, что в категорию можно добавлять только продукты."""
    smartphone1, _, _ = sample_products
    cat = Category("Хиты продаж", "Лучшие товары", [])
    # Добавление продукта — должно работать
    cat.add_product(smartphone1)
    assert str(smartphone1) in cat.products
    # Добавление не-продукта — должно вызывать ошибку
    with pytest.raises(TypeError):
        cat.add_product("не продукт")

def test_add_operator_same_type(sample_products):
    """Проверка, что __add__ работает для одного типа товаров."""
    smartphone1, smartphone2, _ = sample_products
    total = smartphone1 + smartphone2
    assert total == (smartphone1.price * smartphone1.quantity + smartphone2.price * smartphone2.quantity)


def test_add_operator_different_type_raises(sample_products):
    """Проверка, что __add__ запрещает разные типы товаров."""
    smartphone1, _, grass = sample_products
    with pytest.raises(TypeError):
        _ = smartphone1 + grass


def test_category_iterator(sample_products):
    """Проверка работы итератора по категории."""
    smartphone1, smartphone2, grass = sample_products
    cat = Category("Хиты продаж", "Лучшие товары", [smartphone1, smartphone2, grass])#
    iterator = CategoryIterator(cat)
    products = list(iterator)
    assert products == [smartphone1, smartphone2, grass]
    assert len(products) == 3


def test_category_str_counts_total_quantity(sample_products):
    """Проверка, что в строковом представлении категории правильно считается количество."""
    smartphone1, smartphone2, grass = sample_products
    cat = Category("Хиты продаж", "Лучшие товары", [smartphone1, smartphone2, grass])
    assert "количество продуктов: 33" in str(cat)  # 5 + 8 + 20 = 33