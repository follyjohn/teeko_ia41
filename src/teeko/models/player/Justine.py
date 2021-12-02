from typing import List
from src.teeko.models.coordinate import Coordinate
from src.teeko.models.position import Position
from src.teeko.models.teeko_color import get_opponent
from teeko.models.teeko_color import TeekoColorEnum
from teeko.models.movement import Movement
from teeko.models.board import Board
from teeko.models.player.ia_player import IAPlayer

import random


class Justine(IAPlayer):

    @staticmethod
    def _get_player_info() -> str:
        return str("Alan")

    @staticmethod
    def eval(board: Board, color: TeekoColorEnum) -> int:
        if board.is_game_over():
            return 1000
        player_position = board.get_positions_by_color(color)
        opponent_position = board.get_positions_by_color(get_opponent(color))

    
    @staticmethod
    def piece_distance_from_center_coef(positions: List[Position]) -> int:
        piece_count = len(positions)
        if piece_count == 0:
            return 0
        return round(sum([Position.eucludian_distance(pos, Coordinate(2,2)) for pos in positions])/piece_count)

    
    @staticmethod
    def piece_distance_togehter_coef(positions: List[Position]) -> int:
        piece_count = len(positions)
        if piece_count == 0:
            return 0
        coef = 0
        for pos_a in positions:
            for pos_b in positions:
                if pos_a != pos_b:
                    coef += Position.eucludian_distance(pos_a, pos_b)

        return round(coef/piece_count)


    

    def move(self, board: Board, color: TeekoColorEnum) -> Movement:
        movements = self.generate_next_movements(board, color)
        mouvement = random.choice(movements)
        return mouvement
