from typing import Self

class NotInClassException(Exception):
    pass


class Wizzard:
    skill_count = 0
    _students: set[Self] = set()

    def __init__(self, name):
        Wizzard._students.add(self)
        self.name = name
        self.is_in_class = True

    @classmethod
    def print_students_skill_count(cls):
        for student in cls._students:
            print(student.name, student.skill_count)

    def gets_fired(self):
        self.skill_count = self.skill_count
        self.is_in_class = False

    def gets_back_to_class(self):
        self.skill_count = Wizzard.skill_count
        self.is_in_class = True

    def new_skill(self):
        if self.is_in_class:
            Wizzard.skill_count += 1
        else:
            raise NotInClassException(f"{self.name} cannot learn new skill while not in class")


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
