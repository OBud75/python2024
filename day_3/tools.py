from itertools import chain


def next_iter():
    li = [1, 2, 3, 4, 5, 6]
    l = iter(li)
    for _ in range(len(li)):
        print(next(l))


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
