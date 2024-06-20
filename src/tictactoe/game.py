from tictactoe.state import State
from tictactoe.notification import GameWon
from tictactoe.notification import CatsGame
from tictactoe.notification import GetPlayerMove
from tictactoe.notification import InvalidMove
from tictactoe.notification import Notification
from tictactoe.command import Command


class Game:
    def __init__(self):
        self.state = None

    def new_game(self) -> GetPlayerMove:
        self.state = State()
        return GetPlayerMove(player=self.get_current_player(), board=self.get_board())

    def play(self, x, y) -> Command | Notification:
        if not self.game_over():
            if self.state.play(x, y):
                if winner := self.check_for_winner():
                    self.set_winner(winner)
                    self.set_game_over()
                    return GameWon(winner=winner, board=self.get_board())
                if self.check_for_cats_game():
                    self.set_game_over()
                    return CatsGame(board=self.get_board())
                self.change_current_player()
                return GetPlayerMove(player=self.get_current_player(), board=self.get_board())
            else:
                return InvalidMove(message="Invalid move", player=self.get_current_player(), board=self.get_board(),
                                   move=(x, y))
        else:
            if self.winner():
                return GameWon(winner=self.winner(), board=self.get_board())
            else:
                return CatsGame(board=self.get_board())

    def game_over(self):
        return self.state.is_game_over()

    def winner(self):
        return self.state.get_winner()

    def set_winner(self, winner):
        self.state.set_winner(winner)

    def set_game_over(self):
        self.state.set_game_over()

    def check_for_winner(self):
        return self.state.check_for_winner()

    def get_board(self):
        return self.state.get_board()

    def change_current_player(self):
        self.state.change_current_player()

    def check_for_cats_game(self):
        return self.state.is_cats_game()

    def get_current_player(self):
        return self.state.get_current_player()
