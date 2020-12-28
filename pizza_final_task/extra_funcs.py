from random import randint
from typing import Iterable


def get_extra_ingredients() -> Iterable:
    """
    Функция парсит введенную строку и возвращает введенные через запятую слова
    """
    string = str(input("Печатайте: "))
    return set(string.strip().replace(" ", "").split(","))


def log(
    template: str,
):
    def decorator(func):
        def decorated(*args, **kwargs):
            result = func(*args, **kwargs)
            print(template.format(randint(10, 30)))
            return result

        return decorated

    return decorator
