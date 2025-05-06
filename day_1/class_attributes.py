from typing import Self

class NotInClassException(Exception):
    pass


class Wizzard:
    _skill_count = 0
    _students: set[Self] = set()

    def __init__(self, name):
        Wizzard._students.add(self)
        self._name = name
        self._is_in_class = True

    @classmethod
    def print_students_skill_count(cls):
        for student in cls._students:
            print(student._name, student._skill_count)

    def gets_fired(self):
        self._skill_count = self._skill_count
        self._is_in_class = False

    def gets_back_to_class(self):
        self._skill_count = Wizzard._skill_count
        self._is_in_class = True

    def new_skill(self):
        if self._is_in_class:
            Wizzard._skill_count += 1
        else:
            raise NotInClassException(f"{self._name} cannot learn new skill while not in class")


hermione = Wizzard(name="Hermione")
harry = Wizzard(name="Harry")
londubat =  Wizzard(name="Londubat")

hermione.new_skill()
Wizzard.print_students_skill_count()

londubat.gets_fired()
Wizzard.print_students_skill_count()

hermione.new_skill()
Wizzard.print_students_skill_count()

try:
    londubat.new_skill()
except NotInClassException as e:
    print(e)

londubat.gets_back_to_class()
Wizzard.print_students_skill_count()



# Mangling

class Parent:
    def __init__(self):
        self.__name = "parent"


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__name = "child"


c = Child()
print(c._Parent__name)
print(c._Child__name)


