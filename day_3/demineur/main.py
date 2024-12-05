from board import GameBoard
from view import Game


def get_board() -> GameBoard:
    return GameBoard(
        size=int(input("Taille de la grille : ")),
        bombs=int(input("Nombre de bombes : "))
    )

def initialize_game(board) -> Game:
    return Game(board=board)

def main() -> None:
    game: Game = initialize_game(board=get_board())
    game.run()


if __name__ == "__main__":
    main()
