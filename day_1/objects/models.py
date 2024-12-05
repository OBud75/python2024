from objects import logger


class Name:
    def __get__(self, instance, owner):
        if not instance:
            return
        return instance.__dict__.get('_name')

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be an empty string.")
        instance.__dict__['_name'] = value

    def __delete__(self, instance):
        raise AttributeError("Cannot delete the name attribute")


class BirthYear(property):
    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise ValueError("Name must be an integer.")
        if value <= 1900:
            raise ValueError("Must be > 1900.")
        obj.__dict__[self.fset.__name__] = value

    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.fset.__name__)

    @logger.log()
    def __delete__(self, obj) -> None:
        return


class Person:
    name = Name()

    @logger.log()
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __repr__(self):
        return f"{self.name}: {self.age} years old."

    def __eq__(self, value):
        return self.birth_year == value.birth_year

    def __gt__(self, value):
        return self.birth_year < value.birth_year

    def __call__(self, *args, **kwds):
        return f"{self.name} called with args {args}."

    def __add__(self, value):
        # TODO P1 + P3 -> P4
        # P6 + P10 -> P16
        name = "toto"
        birth_year = 2024
        return self.__class__(name, birth_year)

    @BirthYear
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, value):
        self._birth_year = value

    @property
    def age(self):
        return 2024 - self.birth_year
