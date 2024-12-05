"""
https://docs.python.org/3/tutorial/classes.html
"""
from objects import logger, values
from objects.models import Person


with logger.log(f"log-{__name__}.txt"):
    print(values.value_1)
    print(values.value_list)


person_1 = Person(name="P1", birth_year=2000)
print(person_1(1, "two", 3))
try:
    person_1.birth_year = 1899
except ValueError as e:
    print(e)
try:
    person_1.name = ""
except ValueError as e:
    print(e)
del person_1.birth_year
print(person_1.age)


person_2 = Person(name="P2", birth_year=2000)
print(person_1 == person_2)
person_3 = Person(name="P3", birth_year=1995)
print(person_3 > person_2)
print(person_1 + person_2)


people = [person_3, person_2, person_1]
print(sorted(people))

for person in filter(lambda k: k.name=="P1", people):
    print(person)
