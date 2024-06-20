from tictactoe.game import Game
from tictactoe.piece import Piece


class TestGame:
    def test_game_resulting_in_win_for_x(self):
        g = Game()
        g.play(0, 0)
        g.play(0, 1)
        g.play(1, 0)
        g.play(0, 2)
        g.play(2, 0)
        assert g.game_over is True
        assert g.winner == Piece.X
