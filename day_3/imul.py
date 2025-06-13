"""When using +=, *= ecc, Python will check if the object implements the "in-place" version of the operator.

https://docs.python.org/3/library/operator.html#in-place-operators
"For mutable targets such as lists and dictionaries, the in-place method will perform the update, so no subsequent assignment is necessary"

Because the operation on the list is in-place, Python updates the list directly without creating a new one.
Then, when Python attempts to reassign t[0] to the updated list, it raises an exception (but the list has been updated already).
"""


class list(list):
    def __imul__(self, other):
        print(f"Self: {self}")
        print(f"Other: {other}")
        super().__imul__(other)
        print(f"Updated list: {self}")


t = (list([1, 2]), 5)
try:
    t[0] *= 2
except TypeError as e:
    print(f"TypeError: {e}")
print(t)



# Output
# Self: [1, 2]
# Other: 2
# Updated list: [1, 2, 1, 2]
# TypeError: 'tuple' object does not support item assignment
# ([1, 2, 1, 2], 5)
