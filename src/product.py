from src.base_product import BaseProduct


class Product(BaseProduct):
    """Класс, представляющий товар."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, price, quantity)


class Smartphone(Product):
    """Класс для хранения данных о смартфонах."""

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
    """Класс для хранения данных о газонной траве."""

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
