from typing import Optional

from src.product import Product


class Category:
    """Класс, представляющий категорию товаров.
    Атрибуты класса:
        category_count (int): Количество созданных категорий.
        product_count (int): Общее количество товаров во всех категориях.
    Атрибуты экземпляра:
        name (str): Название категории.
        description (str): Описание категории.
        products (list[Product]): Список товаров категории.
    """

    category_count = 0  # количество созданных категорий
    product_count = 0  # Общее количество товаров во всех категориях

    def __init__(self, name: str, description: str, products: Optional[list[Product]]) -> None:
        """Инициализация категории.
        Args:
            name (str): Название категории.
            description (str): Описание категории.
            products (List[Product], optional): Список товаров в категории.
        """
        self.name = name
        self.description = description
        self.__products: list[Product] = []
        if products:
            for product in products:
                self.add_product(product)
        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию, если он является экземпляром Product."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его подклассов.")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list[str]:
        """
        Возвращает список товаров в виде строк:
        'Название, цена руб. Остаток: N шт.'
        """
        return [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products]
