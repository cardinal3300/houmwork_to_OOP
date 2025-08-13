from typing import Iterator, Optional, Any

from src.product import Product


class Category:
    """Класс, представляющий категорию товаров.
    Атрибуты класса:
        category_count (int): Количество созданных категорий.
        product_count (int): Общее количество товаров во всех категориях.
    Атрибуты экземпляра:
        name (str): Название категории.
        description (str): Описание категории.
        products (list[Product]): Список товаров категории."""

    category_count = 0  # количество созданных категорий
    product_count = 0  # Общее количество товаров во всех категориях

    def __init__(self, name: str, description: str, products: Optional[list[Product]] = None) -> None:
        """Инициализация категории.
        Args:
            name (str): Название категории.
            description (str): Описание категории.
            products (List[Product]): Список товаров в категории."""
        self.name = name
        self.description = description
        self.__products: list[Product] = []
        if products:
            for product in products:
                self.add_product(product)
        Category.category_count += 1

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Any) -> None:
        """Добавляет продукт в категорию с проверкой типа.
        Разрешены только экземпляры Product или его наследников.
        Если передан класс вместо экземпляра, вызывается ошибка."""
        if isinstance(product, type):
            if issubclass(product, Product):
                raise TypeError(f"Нельзя передавать класс {product.__name__}, создайте экземпляр перед добавлением.")
            else:
                raise TypeError(f"{product} не является подклассом Product.")
        # Если передан объект, проверяем что это экземпляр Product или наследника
        if not isinstance(product, Product):
            raise TypeError(f"{product} — это не продукт и не его наследник.")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_string(self) -> list[str]:
        """Возвращает список товаров в виде строк:
        'Название, цена руб. Остаток: N шт.'"""
        return [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products]

    @property
    def products_object(self) -> list[Product]:
        """Возвращает список объектов продуктов в категории."""
        return self.__products


class CategoryIterator:
    """Итератор для перебора товаров в категории.
    Позволяет последовательно перебирать объекты Product, содержащиеся в списке товаров категории."""

    def __init__(self, category: Category) -> None:
        self._category = category
        self._index = 0

    def __iter__(self) -> Iterator[Product]:
        """Возвращает сам итератор (сброс индекса)."""
        self._index = 0
        return self

    def __next__(self) -> Product:
        if self._index < len(self._category.products_object):
            product = self._category.products_object[self._index]
            self._index += 1
            return product
        else:
            raise StopIteration
