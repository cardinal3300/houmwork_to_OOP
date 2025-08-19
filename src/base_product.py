from abc import ABC


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен.")
        if price <= 0:
            raise ValueError(f"Цена должна быть больше нуля, получено: {price}")
        if quantity < 0:
            raise ValueError(f"Количество не может быть отрицательным, получено: {quantity}")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Возвращает строковое представление товара."""

        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "BaseProduct") -> float:
        """Складывает стоимость товаров одного типа."""

        if type(self) is not type(other):
            raise TypeError("Складывать можно только товары одного типа")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
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
    def new_product(cls, data: dict) -> "BaseProduct":
        """Создаёт новый продукт на основе словаря параметров."""

        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )
