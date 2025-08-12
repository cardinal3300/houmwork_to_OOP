import pytest

from src.category import CategoryIterator
from src.product import Product


def test_category_str(category_electronics):
    assert str(category_electronics) == "Электроника, количество продуктов: 3 шт."


def test_add_product_valid(category_empty, product_laptop):
    category_empty.add_product(product_laptop)
    assert len(category_empty.products) == 1


def test_add_product_invalid_class(category_empty):
    with pytest.raises(TypeError):
        category_empty.add_product(Product)


def test_add_product_invalid_type(category_empty):
    with pytest.raises(TypeError):
        category_empty.add_product("не продукт")


def test_products_property_format(category_electronics):
    assert all(isinstance(item, str) for item in category_electronics.products)


def test_product_objects_property(category_electronics):
    assert isinstance(category_electronics.product_objects[0], Product)


def test_category_iterator(category_electronics):
    iterator = CategoryIterator(category_electronics)
    products = list(iterator)
    assert products == category_electronics.product_objects
