from tictactoe.piece import Piece


class Board:
    def __init__(self):
        self.board: list[list[Piece]] = [[Piece.empty for _ in range(3)] for _ in range(3)]

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def __str__(self):
        return "\n" + "\n-----\n".join("|".join(cell.value for cell in row) for row in self.board)

    def play(self, row: int, col: int, piece: Piece) -> bool:
        """Play a piece to the tic-tac-toe board.  Returns True if a piece is placed, otherwise returns False."""
        if self.board[row][col] == Piece.empty:
            self.board[row][col] = piece
            return True
        return False

    def check_for_winner(self) -> Piece | None:
        if winner := self._check_horizontal_for_winner():
            return winner
        if winner := self._check_verticals_for_winner():
            return winner
        if winner := self._check_diagonals_for_winner():
            return winner

    def _check_horizontal_for_winner(self) -> Piece | None:
        for row in self.board:
            if row[0] != Piece.empty and all(row[0] == i for i in row):
                return row[0]

    def _check_verticals_for_winner(self) -> Piece | None:
        for col in range(len(self.board)):
            if self.board[0][col] != Piece.empty and all(
                    [self.board[0][col] == self.board[1][col], self.board[0][col] == self.board[2][col]]):
                return self.board[0][col]

    def _check_diagonals_for_winner(self) -> Piece | None:
        if self.board[0][0] != Piece.empty and all(
                [self.board[0][0] == self.board[1][1], self.board[0][0] == self.board[2][2]]):
            return self.board[0][0]

        if self.board[2][0] != Piece.empty and all(
                [self.board[2][0] == self.board[1][1], self.board[2][0] == self.board[0][2]]):
            return self.board[2][0]

    def is_full(self) -> bool:
        return all(all(cell != Piece.empty for cell in row) for row in self.board)

    def is_cats_game(self) -> bool:
        return self.is_full() and not self.check_for_winner()
