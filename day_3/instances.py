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
