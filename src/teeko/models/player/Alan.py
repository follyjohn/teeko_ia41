from teeko.utils_functions import naturalise
from teeko.models.teeko_color import TeekoColorEnum
from teeko.models.movement import Movement
from teeko.models.board import Board
from teeko.models.player.ai_player import AIPlayer
import re
import configparser
import random


class Alan(AIPlayer):

    def __init__(self, label: str):
        self._name = "Alan"
        super().__init__(label)

    def move(self, board: Board, color: TeekoColorEnum) -> Movement:
        movements = self.generate_next_movements(board, color)
        mouvement = random.choice(movements)
        return mouvement
