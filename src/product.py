from src.base_product import BaseProduct


class Product(BaseProduct):
    """Класс, представляющий товар."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"name={self.name!r}, description={self.description!r}, "
            f"price={self.price!r}, quantity={self.quantity!r})"
        )


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

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"name={self.name!r}, description={self.description!r}, "
            f"price={self.price!r}, quantity={self.quantity!r}, "
            f"efficiency={self.efficiency!r}, model={self.model!r}, "
            f"memory={self.memory!r}, color={self.color!r})"
        )


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

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"name={self.name!r}, description={self.description!r}, "
            f"price={self.price!r}, quantity={self.quantity!r}, "
            f"country={self.country!r}, germination_period={self.germination_period!r}, "
            f"color={self.color!r})"
        )
