# 📦 Магазин товаров (E-commerce)

Проект представляет собой базовую реализацию товарного каталога с использованием объектно-ориентированного программирования (ООП) на Python.
---

## 🚀 **Возможности**
- Создание и хранение информации о **товарах** и **категориях**

- Подсчёт общего количества созданных категорий и товаров

- Работа с **итераторами** для перебора товаров в категории

- Возможность расширения функционала через классы-наследники

- Примеры тестов и фикстур для автоматической проверки

---

## ⚡ Установка и использование

1. Клонировать репозиторий SSH:
```bash
    git clone https://git@github.com:cardinal3300/houmwork_to_OOP.git
```
2. Установить зависимости (если есть pyproject.toml):

```bash
    poetry install
```
или (если используется requirements.txt):
```bash
    pip install -r requirements.txt
```
3. Запустить проект:
```bash
  python main.py
```

---

## 🧩 **Реализованные классы**

### **Абстрактный класс** `BaseProduct` 🏷️
Абстрактный базовый класс для всех продуктов.

- Определяет общую функциональность для всех продуктов:

    - `name`, `description`, `price`, `quantity`

    - Методы `__repr__` и фабричный метод `new_product(data: dict)`

- Позволяет уменьшить дублирование кода в наследниках

### **Классы продуктов** 🛒

- `Product` 📝 — базовый товар

- `Smartphone` 📱 — наследник `Product`, хранит данные о смартфонах
    
    - Атрибуты: `efficiency`, `model`, `memory`, `color`

- `LawnGrass` 🌿 — наследник `Product`, хранит данные о газонной траве

    - Атрибуты: `country`, `germination_period`, `color`

---

###  **Класс** `Category` 📁
Класс, представляющий категорию товаров.

- **Атрибуты:**

    - `name`, `description`

    - `product_strings` — список товаров в виде строк

    - `product_objects` — список объектов продуктов

- **Методы:**

    - `add_product()` — добавление нового продукта с проверкой типа

- **Подсчёт:**

    - `category_count` — количество созданных категорий

    - `product_count` — количество товаров во всех категориях

- **Итератор** `CategoryIterator` для последовательного перебора товаров

---

## 💻 Примеры использования
```python
from src.product import Product, Smartphone, LawnGrass
from src.category import Category, CategoryIterator

# Создаём товары
phone = Smartphone("iPhone 15", "Смартфон Apple", 999.99, 5, 95.5, "Pro Max", 256, "Silver")
grass = LawnGrass("GreenField", "Газонная трава премиум", 25.0, 50, "Netherlands", "7-10", "Green")

# Создаём категорию
electronics = Category("Электроника", "Смартфоны и гаджеты", [phone])
garden = Category("Сад и огород", "Товары для сада", [grass])

# Выводим информацию
print(electronics)
print(garden.products_string)

# Итерация по товарам
for item in CategoryIterator(electronics):
    print(item)

# Вывод списка объектов товаров
print(garden.products_object)
```

## 📚 Документация и ссылки

- Абстрактные классы: `BaseProduct`

- Миксины: `LoggerMixin`

- Основные модули: `src/product.py`, `src/category.py`, `src/mixins.py`

- Тесты: `tests/`

## 🧪 Тестирование
В проекте используется `pytest`.
Фикстуры вынесены в отдельный модуль `tests/conftest.py` для удобства переиспользования.

**Запуск всех тестов:**
```bash
    pytest
```
**Запуск тестов с отображением подробного лога:**
```bash
    pytest -v
```
**Запуск с проверкой покрытия кода:**
```bash
    pytest --cov=src
```
## 📜 Лицензия
Этот проект распространяется под лицензией MIT license

---
