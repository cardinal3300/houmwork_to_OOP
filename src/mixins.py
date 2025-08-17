from typing import Any


class LoggerMixin:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)  # вызываем конструктор родителя
        print(f"Создан объект: {repr(self)}")  # выводим строковое представление
