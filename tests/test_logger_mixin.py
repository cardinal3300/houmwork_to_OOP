from src.mixins import LoggerMixin


class Dummy(LoggerMixin):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()

    def __repr__(self):
        return f"Dummy(x={self.x}, y={self.y})"


def test_logger_mixin_prints_creation(capsys) -> None:
    obj = Dummy(1, 2)
    captured = capsys.readouterr()
    assert "Создан объект: Dummy(x=1, y=2)" in captured.out
    assert isinstance(obj, Dummy)
