import click
from pizzas import Margherita, Pepperoni, Hawaiian, PizzaBasicClass
from extra_funcs import log, get_extra_ingredients

MENU = {"Margherita": Margherita, "Pepperoni": Pepperoni, "Hawaiian": Hawaiian}


@log("Приготовили за {}с!")
def bake(pizza):
    """Готовит пиццу"""


@log("Доставили за {}с!")
def delivery(pizza):
    """Доставляет пиццу"""
    pass


@log("Забрали за {}с!")
def pickup(pizza):
    """Самовывоз"""
    pass


@click.group()
def cli():
    pass


@cli.command()
@click.argument("pizza", nargs=1)
@click.argument("size", nargs=1)
@click.option("--delivery", "delivery_flag", default=False, is_flag=True)
def order(pizza: str, size: str, delivery_flag: bool):
    """
    Готовит и доставляет пиццу!
    Введите название пиццы из меню и размер (L/XL)
    """

    pizza = pizza.lower().title()
    if pizza not in MENU:
        print("Такой пиццы нет в меню!")
        return

    size = size.upper()
    if size not in ["L", "XL"]:
        print("Неправильно указан размер!")
        return

    ordered_pizza = MENU[pizza](size)
    ordered_pizza.customize()

    bake(ordered_pizza)
    if delivery_flag:
        delivery(ordered_pizza)
    else:
        pickup(ordered_pizza)


@cli.command()
def menu():
    """Показывает меню"""

    print("НАШЕ МЕНЮ:")
    for pizza in MENU.values():
        print("\n", pizza())


if __name__ == "__main__":
    cli()
