import random
from typing import Literal


class Node:
    objects = set()

    def __init__(self, row, col, is_bomb, left, top) -> None:
        self.is_bomb = is_bomb
        self.is_flagged = False
        self.row = row
        self.col = col

        self.left: None | Node = left
        self.top: None | Node = top
        self.right: None | Node = None
        self.bot: None | Node = None

        if self.left:
            self.left.right = self
        if self.top:
            self.top.bot = self

        self.objects.add(self)

    @property
    def adjacent_bombs(self) -> str:
        return str(len([
            node for node in self.adjacent_nodes if node.is_bomb]))

    @property
    def top_left(self):
        return self.top.left if self.top else None

    @property
    def top_right(self):
        return self.top.right if self.top else None

    @property
    def bot_left(self):
        return self.bot.left if self.bot else None

    @property
    def bot_right(self):
        return self.bot.right if self.bot else None

    @property
    def adjacent_nodes(self):
        return [node for node in [
            self.left, self.top_left, self.top, self.top_right,
            self.right, self.bot_right, self.bot, self.bot_left
        ] if node]


class GameBoard:
    def __init__(self, size=10, bombs=10) -> None:
        self._rows: int = size
        self._cols: int = size
        self._bombs: int = bombs
        self.start()

    @property
    def is_playing(self) -> bool:
        return not (self.is_win or self._is_lost)

    @property
    def is_won(self) -> bool:
        to_find = self._rows * self._cols - self._bombs
        return len([
            char for row in self._to_print for char
            in row if char not in [" ", "*"]]) >= to_find

    @property
    def nodes(self) -> set[Node]:
        return Node.objects

    @property
    def table(self) -> list[list[Node]]:
        return self._table

    @property
    def to_print(self) -> list[list[int | Literal[" "]]]:
        return self._to_print

    @property
    def width(self) -> int:
        return self._rows

    @property
    def height(self) -> int:
        return self._cols

    def reveal(self, x, y) -> None:
        node: Node = self._table[x][y]
        if node.is_bomb:
            self.is_lost = True

        self._to_print[x][y] = node.adjacent_bombs
        if node.adjacent_bombs == "0":
            to_visit: list[Node] = node.adjacent_nodes[:]
            visited = set()

            while to_visit:
                visiting: Node = to_visit[0]

                if visiting not in visited:
                    visited.add(visiting)
                    self._to_print[visiting.row][visiting.col] = (
                        visiting.adjacent_bombs)

                    if visiting.adjacent_bombs == "0":
                        to_visit += visiting.adjacent_nodes

                to_visit = to_visit[1:]

    def start(self):
        self._table = [
            [" " for _ in range(self._cols)]
            for _ in range(self._rows)]

        self._to_print = [
            [" " for _ in range(self._cols)]
            for _ in range(self._rows)]

        self.is_lost = False
        self._ramdomize_bombs()
        self._load_table_nodes()

    def _load_table_nodes(self) -> None:
        last_row = {}
        for row, line in enumerate(iterable=self._table):
            last_node = None
            for col, node in enumerate(iterable=line):
                is_bomb = True if node == "*" else False
                self._table[row][col] = last_row[col] = last_node = Node(
                    is_bomb=is_bomb, row=row, col=col,
                    left=last_node, top=last_row.get(col))

    def _ramdomize_bombs(self) -> None:
        bombs = 0
        while bombs < self._bombs:
            x: int = random.randint(a=0, b=self._cols - 1)
            y: int = random.randint(a=0, b=self._rows - 1)
            if self._table[x][y] == " ":
                self._table[x][y] = "*"
                self._to_print[x][y] = "*"
                bombs += 1
