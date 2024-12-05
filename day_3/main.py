from boards import Board


def play():
    board = Board.new()
    while True:
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))
        try:
            board.play_turn("X", row, col)
        except ValueError:
            continue

        board.play_turn("O", *board.best_move())


play()
