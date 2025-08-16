class LoggerMixin:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # вызываем конструктор родителя
        print(f"Создан объект: {repr(self)}")  # выводим строковое представление

