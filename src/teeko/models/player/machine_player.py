import re

from teeko.models.board import Board
from teeko.models.coordinate import Coordinate
from teeko.models.movement import Movement
from teeko.models.player.player import Player


class MachinePlayer(Player):

    def __init__(self):
        super().__init__()

    @staticmethod
    def _get_player_info() -> str:
        return str("William")

    def print_player(self):
        super().print_player()

    def move(self, board: Board) -> Movement:
        return Movement(Coordinate(0, 0), Coordinate(0, 0))

    def get_name(self):
        return super().get_name()
