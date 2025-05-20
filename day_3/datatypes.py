from abc import ABC, abstractmethod
from dataclasses import dataclass, FrozenInstanceError


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


class Function:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwds):
        return self.func(*args)


say_hello = Function(func=lambda k: print(f"Hello {k}"))
say_hello("Thomas")

do_something = Function(func=lambda k, j: print(f"Called with {k, j}"))
do_something(1, 2)



class StaticPerson:
    # Tuples are immutable
    # Dynamic classes have a __dict__ instead
    __slots__ = ("age", "name")

    def __init__(self, age, name):
        self.age = age
        self.name = name


p1 = StaticPerson(age=33, name="Thomas")
try:
    p1.favorite_color = "blue"
except AttributeError as e:
    print(e)



@dataclass
class Person:
    """Dataclasses abstract the __init__ method."""
    name: str

p1 = Person(name="Thomas")
p1.age = 18

p2 = Person(name="Titi")
print(p1.name, p2.name)
try:
    print(Person.name)
except AttributeError as e:
    print(e)


@dataclass(frozen=True, slots=True)
class FrozenPerson:
    """
    Frozen : Immutability (abstract the definition of __setattr__ ecc)
    Slots : abstract the __slots__ = syntax
    """
    name: str


p1 = FrozenPerson(name="Thomas")
try:
    p1.age = 18
except FrozenInstanceError as e:
    print(e)

try:
    p1.name = "Albert"
except FrozenInstanceError as e:
    print(e)

# https://docs.python.org/3/library/dataclasses.html
