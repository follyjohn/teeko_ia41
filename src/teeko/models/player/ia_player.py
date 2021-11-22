"""
    Metadata: 
        author:    follyjohn
        date:      2021-11-21
        purpose:   IA Player class

    Description: IA Player class for the game. This class is used to represent an IA player in the game.
    The particularity of this class is that it uses the Minimax algorithm to get the next move from the player.
            
"""
import re

from teeko.models.board import Board
from teeko.models.coordinate import Coordinate
from teeko.models.movement import Movement
from teeko.models.player.player import Player


class IAPlayer(Player):

    def __init__(self):
        super().__init__()


    @staticmethod
    def _get_player_info() -> str:
        return str("William")


    def print_player(self):
        super().print_player()


    def move(self, board: Board) -> Movement: #TODO: implement the minimax algorithm
        pass


    def get_name(self):
        return super().get_name()
