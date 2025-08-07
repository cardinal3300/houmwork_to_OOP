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
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: object) -> float:
        if not isinstance(other, Product):
            return NotImplemented
        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self) -> float:
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены с проверкой и подтверждением понижения цены.
        Не допускает установку цены ниже или равной нулю.
        """

        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self.__price:
            answer = input(f"Вы понижаете цену с {self.__price} до {value}. Подтверждаете? (y/n): ").strip().lower()
            if answer != "y":
                print("Снижение цены отменено")
                return
        self.__price = value

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Создаёт новый продукт на основе словаря параметров."""

        return cls(product_data["name"], product_data["description"], product_data["price"], product_data["quantity"])
