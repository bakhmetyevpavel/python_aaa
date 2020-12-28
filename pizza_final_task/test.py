# Запуск в терминале python -m pytest test.py
# Для демонстрации coverage: python -m pytest test.py --cov=

import pytest
from click.testing import CliRunner  # для тестирования click
from pizzas import Margherita, Pepperoni, Hawaiian, PizzaBasicClass
from extra_funcs import log, get_extra_ingredients
from cli import menu, order, bake, delivery, pickup


def test_dict_method():
    """Проверка метода __dict__()"""
    expected = {
        "pineapples": "100 grams",
        "chicken": "100 grams",
        "tomato sauce": "40 grams",
        "mozzarella": "50 grams",
    }

    assert Hawaiian(size="XL").dict() == expected


def test_equal_pizzas():
    """Проверка метода __eq__()"""
    assert (
        (Margherita(size="L") == Margherita(size="L")) == "Одинаковые пиццы!"
        and (Pepperoni(size="XL") == Margherita(size="L")) == "Это разные пиццы!"
        and (Hawaiian(size="XL") == Hawaiian(size="XL")) == "Одинаковые пиццы!"
    )


def test_weight():
    """Провеска свойства weight. XL > L в 2 раза"""
    assert (
        Margherita(size="XL").weight == "В вашей пицце 160 грамм ингридиентов!"
        and Margherita(size="L").weight == "В вашей пицце 80 грамм ингридиентов!"
    )


def test_wrong_size():
    with pytest.raises(ValueError):
        Margherita(size="X")
