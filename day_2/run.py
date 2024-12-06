class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __add__(self, other):
        return Node(
            name=f"{self.name} + {other.name}",
            x=self.x + other.x,
            y=self.y + other.y
        )

if __name__ == "__main__":
    n1 = Node("node1", 0, 0)
    n2 = Node("node2", 1, 0)
    d = {
        n1: n1.name,
        n2: n2.name,
    }
    print(d.get(n1))
    n3 = n1 + n2
    print(n3.name, n3.x, n3.y)
    "toto" + "titi"
