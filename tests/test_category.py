import pytest

from src.category import Category, CategoryIterator
from src.product import Product


def test_category_str(category_electronics: Category) -> None:
    assert str(category_electronics) == "Электроника, количество продуктов: 3 шт."


def test_add_product_valid(category_empty: Category, product_laptop: Product) -> None:
    category_empty.add_product(product_laptop)
    assert len(category_empty.products_string) == 1


def test_add_product_invalid_class(category_empty: Category) -> None:
    with pytest.raises(TypeError):
        category_empty.add_product(Product)


def test_add_product_invalid_type(category_empty: Category) -> None:
    with pytest.raises(TypeError):
        category_empty.add_product("не продукт")


def test_add_product_raises_for_non_product_class() -> None:
    """Проверка, что передача не-наследника Product вызывает ошибку."""
    cat = Category("Техника", "Описание", [])

    class NotAProduct:
        pass

    with pytest.raises(TypeError) as exc_info:
        cat.add_product(NotAProduct)  # передаём класс, а не экземпляр

    assert "не является подклассом Product" in str(exc_info.value)


def test_products_property_format(category_electronics: Category) -> None:
    assert all(isinstance(item, str) for item in category_electronics.products_string)


def test_product_objects_property(category_electronics: Category) -> None:
    assert isinstance(category_electronics.products_object[0], Product)


def test_category_iterator(category_electronics: Category) -> None:
    iterator = CategoryIterator(category_electronics)
    products = list(iterator)
    assert products == category_electronics.products_object


def test_products_string_and_object(cat, smartphone1) -> None:
    # Проверка строкового списка
    strings = cat.products_string
    assert all(isinstance(s, str) for s in strings)
    assert smartphone1.name in strings[0]

    # Проверка списка объектов
    objs = cat.products_object
    assert smartphone1 in objs
