class Product:
    """Класс, представляющий товар.
    Атрибуты:
        name (str): Название товара.
        description (str): Описание товара.
        price (float): Цена товара.
        quantity (int): Количество в наличии.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация объекта Product.
        Args:
            name (str): Название товара.
            description (str): Описание товара.
            price (float): Цена.
            quantity (int): Количество на складе.
        """

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
