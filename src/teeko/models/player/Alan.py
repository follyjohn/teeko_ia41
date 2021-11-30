from teeko.models.teeko_color import TeekoColorEnum
from teeko.models.movement import Movement
from teeko.models.board import Board
from teeko.models.player.ia_player import IAPlayer

import random


class Alan(IAPlayer):

    @staticmethod
    def _get_player_info() -> str:
        return str("Alan")

    def move(self, board: Board, color: TeekoColorEnum) -> Movement:
        movements = self.generate_next_movements(board, color)
        mouvement = random.choice(movements)
        return mouvement
