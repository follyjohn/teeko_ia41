import pickle
from typing import List
from src.utils import profile
from src.models.coordinate import Coordinate
from src.models.position import Position
from src.models.teeko_color import get_opponent
from src.models.teeko_color import TeekoColorEnum
from src.models.movement import Movement
from src.models.board import Board
from src.models.player.ia_player import IAPlayer

import random
from copy import copy
from time import time

class Nada(IAPlayer):

    @staticmethod
    def _get_player_info() -> str:
        return str("Nada")

    @staticmethod
    def eval(board: Board, color: TeekoColorEnum) -> float:

        if board.is_game_over():
            value = 100000
        else:
            player_position = board.get_positions_by_color(color)
            opponent_position = board.get_positions_by_color(get_opponent(color))

            value = 40*Nada.piece_distance_from_center_coef(player_position) + 60*Nada.piece_distance_togehter_coef(opponent_position)

        # board.display()
        #   print("value: ", value)

        # if color == TeekoColorEnum.RED_COLOR:
        #   value = -value

        return value

    @staticmethod
    def minmax(board: Board, color: TeekoColorEnum, depth: int, alpha: float, beta: float) -> float:
        if depth == 0 or board.is_game_over():
            return Nada.eval(board, color)

        if color == TeekoColorEnum.BLACK_COLOR:
            best_value = float("-inf")
            for next_bords in Nada.generate_next_board_states(board, color):
                value = Nada.minmax(
                    next_bords, get_opponent(color), depth-1, alpha, beta)
                best_value = max(best_value, value)
                alpha = max(alpha, best_value)
                if best_value >= beta:
                    return best_value
                alpha = max(alpha, best_value)
            return best_value
        else:
            best_value = float("inf")
            for next_bords in Nada.generate_next_board_states(board, color):
                value = Nada.minmax(
                    next_bords, get_opponent(color), depth-1, alpha, beta)
                best_value = min(best_value, value)
                beta = min(beta, best_value)
                if best_value <= alpha:
                    return best_value
                beta = min(beta, best_value)
            return best_value

    @staticmethod
    def piece_distance_from_center_coef(positions: List[Position]) -> float:
        piece_count = len(positions)
        if piece_count == 0:
            return 0
        return 100/((sum([Position.eucludian_distance(pos.get_coordinate(), Coordinate(2, 2)) for pos in positions])/piece_count)+1)

    @staticmethod
    def piece_distance_togehter_coef(positions: List[Position]) -> float:
        piece_count = len(positions)
        if piece_count < 2:
            return 0
        coef = 0
        for pos_a in positions:
            for pos_b in positions:
                if pos_a != pos_b:
                    coef += Position.eucludian_distance(pos_a.get_coordinate(), pos_b.get_coordinate())

        return 100/(coef/piece_count)

    @profile
    def move(self, board: Board, color: TeekoColorEnum) -> Movement:
        deep = 4
        if len(board.get_empty_positions()) >= 23:
            deep = 2

        start_time = time()
        best_value = Nada.minmax(board, color, deep, float("-inf"), float("inf"))
        print("best value in ", time()-start_time)
        start_time = time()
        movements = self.generate_next_movements(board, color)
        print("movements in ", time()-start_time)
        print("nb movements: ", len(movements))
        while len(movements) > 0:
            movement = movements.pop()
            next_board = pickle.loads(pickle.dumps(board))
            next_board.move_piece(movement)
            next_value = Nada.minmax(next_board, get_opponent(color), deep-1, float("-inf"), float("inf"))
            if next_value == best_value:
                return movement
