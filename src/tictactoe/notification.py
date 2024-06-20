from dataclasses import dataclass
from typing import Optional

from tictactoe.piece import Piece
from tictactoe.board import Board


class Notification:
    pass


@dataclass
class NewGame(Notification):
    pass


@dataclass
class GameWon(Notification):
    winner: Piece
    board: Board


@dataclass
class CatsGame(Notification):
    board: Board


@dataclass
class GetPlayerMove(Notification):
    player: Piece
    board: Board
    message: Optional[str] = None


@dataclass
class InvalidMove(Notification):
    message: str
    player: Piece
    board: Board
    move: tuple[int, int]
