from abc import ABC, abstractmethod


def animal_init(self):
    print("init animal")

@abstractmethod
def talk(self):
    NotImplemented

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


class AbstractClass:
    def __init__(self, name, mro, dict):
        self.__name__ = name
        self.__mro__ = mro
        self.__dict__ = dict

    def __call__(self, *args, **kwds):
        raise ValueError(f"Cannot instanciate {self.__class__.__name__}")


Human = AbstractClass("Human", (), {})
try:
    h1 = Human()
except ValueError as e:
    print(e)


class Person(metaclass=AbstractClass):
    ...

try:
    p1 = Person()
except ValueError as e:
    print(e)