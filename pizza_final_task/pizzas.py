from extra_funcs import get_extra_ingredients
from typing import Iterable, Callable


class PizzaBasicClass:
    """
    Базовый класс, на основе которого создается любая пицца
    """

    INGREDIENTS = {
        "pineapples": 50,
        "grape": 10,
        "fish": 30,
        "mushrooms": 40,
        "bacon": 20,
        "chicken": 50,
        "tomato sauce": 20,
        "mozzarella": 25,
        "tomatoes": 35,
        "pepperoni": 15,
    }

    SIZE_K = {"L": 1, "XL": 2}

    def __init__(
        self,
        size="L",
        name="Simples pizza",
        ingredients={"tomato sauce", "mozzarella"},
    ):
        if size not in self.SIZE_K:
            raise (ValueError)

        self.name = name
        self.ingredients = ingredients
        self.size = size

    def __eq__(self, another_pizza) -> str:
        """
        Для сравнения двух пицц!
        Сравниваем по размеру и ингредиентам.
        """
        result = {True: "Одинаковые пиццы!", False: "Это разные пиццы!"}
        if isinstance(another_pizza, PizzaBasicClass):
            return result[
                self.ingredients == another_pizza.ingredients
                and self.size == another_pizza.size
            ]
        else:
            raise TypeError("Нельзя сравнивать с данным объектом!")

    def __repr__(self):
        """
        Выводим информацию о пицце.
        Имя и ингредиенты.
        """
        return f"Pizza {self.name}:\n--" + "\n--".join(self.dict())

    __str__ = __repr__

    def dict(self) -> dict:
        """
        Выводит рецепт пиццы в виде словаря.
        """
        return {
            key: f"{val*self.SIZE_K[self.size]} grams"
            for key, val in self.INGREDIENTS.items()
            if key in self.ingredients
        }

    @property
    def weight(self) -> int:
        """
        Возвращает суммарный вес ингредиентов пиццы.
        """
        return (
            "В вашей пицце"
            + f" {sum(self.INGREDIENTS[ingr]*self.SIZE_K[self.size] for ingr in self.ingredients)} "
            + "грамм ингридиентов!"
        )

    def customize(self):
        """
        Добавить собственные ингредиенты по желанию
        """
        print(
            """
        Можете выбрать дополнительные ингредиенты,
        указав их через запятую или пропустить шаг ('ENTER')
        """
        )
        print("\n".join([f"-- {ingr}" for ingr in self.INGREDIENTS]))
        extra_ingredients = get_extra_ingredients()

        if len(extra_ingredients) == 0:
            print("Ингредиенты для добавки не выбраны")
            return
        else:
            correct_ingrs = {
                ingr for ingr in extra_ingredients if ingr in self.INGREDIENTS
            }
            incorrect_ingrs = {
                ingr
                for ingr in extra_ingredients
                if ingr not in self.INGREDIENTS
            }

        if len(incorrect_ingrs) > 0:
            print(
                "У нас нет ингредиентов: \n--" + "\n--".join(incorrect_ingrs)
            )

        if len(correct_ingrs) > 0:
            print("Добавлены ингредиенты: \n--" + "\n--".join(correct_ingrs))
            self.ingredients = self.ingredients.union(correct_ingrs)
            self.name = self.name + " customized"

        print(f"Ваша пицца: \n {self}")
        return


class Margherita(PizzaBasicClass):
    """
    Pizza Margherita
    """

    NAME = "Margherita"
    RECIPE = {"tomato sauce", "mozzarella", "tomatoes"}

    def __init__(self, size="L", name=NAME, ingredients=RECIPE):
        super().__init__(size, name, ingredients)


class Pepperoni(PizzaBasicClass):
    """
    Pizza Pepperoni
    """

    NAME = "Pepperoni"
    RECIPE = {"tomato sauce", "mozzarella", "pepperoni"}

    def __init__(self, size="L", name=NAME, ingredients=RECIPE):
        super().__init__(size, name, ingredients)


class Hawaiian(PizzaBasicClass):
    """
    Pizza Hawaiian
    """

    NAME = "Hawaiian"
    RECIPE = {"tomato sauce", "mozzarella", "chicken", "pineapples"}

    def __init__(self, size="L", name=NAME, ingredients=RECIPE):
        super().__init__(size, name, ingredients)
