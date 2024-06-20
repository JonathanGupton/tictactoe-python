from tictactoe.board import Board
from tictactoe.piece import Piece


class TestBoard:
    def test_player_can_play_to_board(self):
        b = Board()
        response = b.play(0, 0, Piece.X)
        assert response
        assert b.board[0][0] == Piece.X

    def test_player_cannot_play_over_previously_played_position(self):
        b = Board()
        b.play(0, 0, Piece.X)
        response = b.play(0, 0, Piece.O)
        assert response is False

    def test_three_in_a_horizontal_row_is_a_winner(self):
        b = Board()
        b.play(0, 0, Piece.X)
        b.play(0, 1, Piece.X)
        b.play(0, 2, Piece.X)
        assert b.check_for_winner() == Piece.X

    def test_three_in_a_vertical_row_is_a_winner(self):
        b = Board()
        b.play(0, 0, Piece.X)
        b.play(1, 0, Piece.X)
        b.play(2, 0, Piece.X)
        assert b.check_for_winner() == Piece.X

    def test_three_in_a_vertical_row_with_mixed_o_and_x_is_not_a_winner(self):
        b = Board()
        b.play(0, 0, Piece.X)
        b.play(1, 0, Piece.O)
        b.play(2, 0, Piece.X)
        assert b.check_for_winner() is None

    def test_three_in_a_top_left_to_bottom_right_diagonal_is_a_winner(self):
        b = Board()
        b.play(0, 0, Piece.X)
        b.play(1, 1, Piece.X)
        b.play(2, 2, Piece.X)
        assert b.check_for_winner() == Piece.X

    def test_three_in_a_bottom_left_to_top_right_diagonal_is_a_winner(self):
        b = Board()
        b.play(2, 0, Piece.X)
        b.play(1, 1, Piece.X)
        b.play(0, 2, Piece.X)
        assert b.check_for_winner() == Piece.X

    def test_board_is_full_should_return_true_when_all_spaces_are_full(self):
        b = Board()
        b.board = [[Piece.X, Piece.O, Piece.X],
                   [Piece.X, Piece.O, Piece.X],
                   [Piece.O, Piece.X, Piece.O]]
        assert b.is_full()

    def test_board_is_full_should_return_false_when_all_spaces_are_not_full(self):
        b = Board()
        b.board = [[Piece.X, Piece.O, Piece.X],
                   [Piece.X, Piece.empty, Piece.X],
                   [Piece.O, Piece.X, Piece.O]]
        assert not b.is_full()

    def test_board_should_print_nicely(self):
        """No actual assertion.  Just a spot check."""
        b = Board()
        print(b)

        b.play(0, 0, Piece.X)
        print(b)

        b.play(1, 1, Piece.O)
        print(b)

        b.play(0, 1, Piece.X)
        print(b)

        b.play(2, 1, Piece.O)
        print(b)

        b.play(0, 2, Piece.X)
        print(b)

