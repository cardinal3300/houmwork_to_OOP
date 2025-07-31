from typing import List

from src.product import Product


class Category:
    """Класс, представляющий категорию товаров.
    Атрибуты класса:
        category_count (int): Количество созданных категорий.
        product_count (int): Общее количество товаров во всех категориях.
    Атрибуты экземпляра:
        name (str): Название категории.
        description (str): Описание категории.
        products (List[Product]): Список товаров категории.
    """

    category_count = 0  # количество созданных категорий
    product_count = 0   # Общее количество товаров во всех категориях

    def __init__(self, name: str, description: str, products: List[Product] = None):
        """Инициализация категории.
        Args:
            name (str): Название категории.
            description (str): Описание категории.
            products (List[Product], optional): Список товаров в категории.
        """

        self.name = name
        self.description = description
        self.products: List[Product] = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.products)

    def add_product(self, product: Product):
        """Добавляет товар в категорию.
        Args:
            product (Product): Товар для добавления."""

        self.products.append(product)
        Category.product_count += 1
