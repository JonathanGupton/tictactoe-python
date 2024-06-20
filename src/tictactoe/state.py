from tictactoe.piece import Piece
from tictactoe.board import Board


class State:
    def __init__(self):
        self.current_player = Piece.X
        self.board = Board()
        self.winner = None
        self.game_over = False

    def play(self, row: int, col: int) -> bool | None:
        return self.board.play(row, col, self.current_player)

    def change_current_player(self) -> None:
        self.current_player = Piece.O if self.current_player == Piece.X else Piece.X

    def get_current_player(self) -> Piece:
        return self.current_player

    def set_winner(self, winner: Piece) -> None:
        self.winner = winner

    def get_winner(self) -> Piece | None:
        return self.winner

    def set_game_over(self) -> None:
        self.game_over = True

    def is_game_over(self) -> bool:
        return self.game_over

    def check_for_winner(self) -> Piece | None:
        return self.board.check_for_winner()

    def is_cats_game(self) -> bool:
        return self.board.is_cats_game()

    def get_board(self):
        return self.board
