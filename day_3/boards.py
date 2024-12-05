import math


class Board:
    def __init__(self, position) -> None:
        self.position: list[list[str]] = position

    def __str__(self):
        position = ""
        for row in self.position:
            position += "|"
            for cell in row:
                position += f"{cell}|"
            position += "\n"
        return position

    @classmethod
    def new(cls):
        return cls(position=[
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]])

    @property
    def empty_cells(self) -> list[tuple[int, int]]:
        return [
            (y, x)
            for (y, row) in enumerate(iterable=self.position)
            for (x, cell) in enumerate(iterable=row)
            if cell == " "]

    def is_won(self, player) -> bool:
        row_1: list[str] = self.position[0]
        row_2: list[str] = self.position[1]
        row_3: list[str] = self.position[2]
        return any([all([
            cell == player for cell in row])
            for row in [
                (row_1[0], row_1[1], row_1[2]),
                (row_2[0], row_2[1], row_2[2]),
                (row_3[0], row_3[1], row_3[2]),
                (row_1[0], row_2[0], row_3[0]),
                (row_1[1], row_2[1], row_3[1]),
                (row_1[2], row_2[2], row_3[2]),
                (row_1[0], row_2[1], row_3[2]),
                (row_1[2], row_2[1], row_3[0])]])

    def play_turn(self, player, pos_y, pos_x):
        if self.position[pos_y][pos_x] != " ":
            raise ValueError("Already taken")
        self.position[pos_y][pos_x] = player
        print(self)
        if self.is_won(player=player):
            quit(code=f"{player} won")
        if not self.empty_cells:
            quit(code="Draw")

    def minimax(self, is_maximizing) -> int:
        if self.is_won("O"):
            return 1
        if self.is_won("X"):
            return -1
        if not self.empty_cells:
            return 0

        if is_maximizing:
            best_score = -math.inf
            for (y, x) in self.empty_cells:
                self.position[y][x] = "O"
                score = self.minimax(is_maximizing=False)
                self.position[y][x] = " "
                best_score = max(score, best_score)
            return best_score

        best_score = math.inf
        for (y, x) in self.empty_cells:
            self.position[y][x] = "X"
            score = self.minimax(is_maximizing=True)
            self.position[y][x] = " "
            best_score = min(score, best_score)
        return best_score

    def best_move(self) -> tuple[int, int]:
        best_score = -math.inf
        move = None
        for y, x in self.empty_cells:
            self.position[y][x] = "O"
            score = self.minimax(False)
            self.position[y][x] = " "
            if score > best_score:
                best_score = score
                move = (y, x)
        return move
