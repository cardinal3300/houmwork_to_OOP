class Product:
    """Класс, представляющий товар.
    Атрибуты:
        name (str): Название товара.
        description (str): Описание товара.
        price (float): Цена товара.
        quantity (int): Количество в наличии."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация объекта Product.
        Args:
            name (str): Название товара.
            description (str): Описание товара.
            price (float): Цена.
            quantity (int): Количество на складе."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Возвращает строковое представление товара."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Складывает стоимость товаров одного типа.
        Аргументы:
            other (Product): другой товар.
        Возвращает:
            float: сумма полной стоимости товаров.
        Вызывает:
            TypeError: если товары относятся к разным классам."""
        if type(self) is not type(other):
            raise TypeError("Складывать можно только товары одного типа")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self) -> float:
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены с проверкой и подтверждением понижения цены.
        Не допускает установку цены ниже или равной нулю."""
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
    def new_product(cls, data: dict) -> "Product":
        """Создаёт новый продукт на основе словаря параметров."""
        return cls(
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            quantity=data.get("quantity")
        )


class Smartphone(Product):
    """Класс для хранения данных о смартфонах.
    Атрибуты:
        efficiency (float): рейтинг производительности.
        model (str): модель устройства.
        memory (int): объем памяти в ГБ.
        color (str): цвет устройства."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для хранения данных о газонной траве.
    Атрибуты:
        country (str): страна-производитель.
        germination_period (int): период всхода в днях.
        color (str): цвет травы."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
