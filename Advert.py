import json
from keyword import iskeyword


class _ColorMixin:
    """
    This mixin class change the output text color.
    """

    repr_color_code = 32

    def __repr__(self):
        return f"\033[0;{self.repr_color_code};47m{self.title} | {self.price} ₽\033[0m"


class _Dict2Attr:
    """
    This class makes object's attributes from dict.
    """

    def __init__(self, input_dict: dict):

        if not isinstance(input_dict, dict):
            raise TypeError("Input data are not a dict type!")

        for key, value in input_dict.items():
            if iskeyword(key):
                key = key + "_"
            if isinstance(value, dict):
                self.__setattr__(key, _Dict2Attr(value))
            else:
                self.__setattr__(key, value)

    def __repr__(self):
        return f"{self.__dict__}"


class BaseAdvert:
    """
    This is base Advert class with standart __repr__ method. Created for using Mixin class.
    """

    def __init__(self, input_dict: dict):
        self.__dict__ = _Dict2Attr(input_dict).__dict__
        if "title" not in self.__dict__:
            raise ValueError("Object hasn't field 'title'!")
        if "price" in self.__dict__:
            self.price = self.__dict__["price"]

    @property
    def price(self):
        if "price" in self.__dict__:
            return self.__dict__["price"]
        else:
            return 0

    @price.setter
    def price(self, price: float):
        if price < 0:
            raise ValueError("Price must be not negative!")
        else:
            # self.__setattr__('price', price)
            self.__dict__["price"] = price

    def __repr__(self):
        return f"{self.title} | {self.price} ₽"


class Advert(_ColorMixin, BaseAdvert):
    """
    This class converts JSON to object.
    """

    repr_color_code = 32

    def __init__(self, input_dict: dict):
        super().__init__(input_dict)


if __name__ == "__main__":
    json_object = """{
        "title": "python",
        "price": 10,
        "class": "proga",
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
        }"""

    obj = json.loads(json_object)
    obj_ad = Advert(obj)
    obj_ad
    obj_ad.location.address
    obj_ad.price
