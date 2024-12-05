from abc import ABC, abstractmethod
from itertools import chain


def next_iter():
    li = [1, 2, 3, 4, 5, 6]
    l = iter(li)
    for _ in range(len(li)):
        print(next(l))


def animal_init(self):
    print("init animal")

@abstractmethod
def talk(self):
    raise NotImplemented

Animal = type(
    "Animal",
    (ABC,),
    {
        "__init__": animal_init,
        "talk": talk,
        "objects": set()
    }
)

class Dog(Animal):
    def talk(self):
        print("Waf")

class Cat(Animal):
    def talk(self):
        print("Miaou")


class Cursor:
    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if Cursor._instance:
            return Cursor._instance

        Cursor._instance = super().__new__(cls)
        return Cursor._instance


class Human:
    objects = set()

    @classmethod
    def __new__(cls, *args, **kwargs):
        for obj in cls.objects:
            if obj.name == args[1]:
                return obj

        instance = super().__new__(cls)
        cls.objects.add(instance)
        return instance

    def __init__(self, name):
        self.name = name


class Men(Human): ...
class Women(Human): ...


class Category:
    objects = set()

    def __init__(self, name):
        self.name = name
        self.objects.add(self)

    @classmethod
    def get_by_name(cls, name):
        for category in cls.objects:
            if category.name == name:
                return category


class Article:
    def __init__(self, name, category):
        self.name = name
        self.category = category


categories = [Category(name=name) for name in ["Clothes", "IT", "Drinks"]]

coca = Article("Coca", category=Category.get_by_name("Drinks"))
dress = Article("Dress", category=Category.get_by_name("Clothes"))
mac = Article("Mac", category=Category.get_by_name("IT"))
pc = Article("PC", category=Category.get_by_name("IT"))
water = Article("Water", category=Category.get_by_name("Drinks"))
pepsi = Article("Pepsi", category=Category.get_by_name("Drinks"))

articles = [
    pc, mac, dress, water, coca, pepsi
]
"https://docs.python.org/3/library/itertools.html#itertools.groupby"


def chain_lists():
    primary_colors = ["red", "green", "blue"]
    other_colors = ["purple", "yellow"]
    for color in chain(primary_colors, other_colors):
        print(color)


# Ecrire une fonction qui renvoie la date d'il y a 6 jours exactement
# datetime.now(), timedelta
