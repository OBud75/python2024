from boards import Board


class BoardTest:
    def test_winning(self, board: Board, player: str):
        assert board.is_won(player)


x_win = Board([
    ["X", " ", " "],
    [" ", "X", "O"],
    [" ", "O", "X"]])
board_test = BoardTest()
board_test.test_winning(x_win, "O")
