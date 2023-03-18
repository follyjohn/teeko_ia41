from core.teeko_color import TeekoColorEnum
from core.movement import Movement
from core.board import Board
from core.ia_player import IAPlayer

import random


class Alan(IAPlayer):
    @staticmethod
    def _get_player_info() -> str:
        return str("Alan")

    def move(self, board: Board, color: TeekoColorEnum) -> Movement:
        movements = self.generate_next_movements(board, color)
        mouvement = random.choice(movements)
        return mouvement
