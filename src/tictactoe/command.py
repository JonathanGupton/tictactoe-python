from dataclasses import dataclass
from typing import Optional

from tictactoe.piece import Piece
from tictactoe.board import Board


class Command:
    pass


@dataclass
class NewGame(Command):
    pass