import configparser
import copy
import pickle
import re
from typing import List
from teeko.models.game.game_level import GameLevel
from teeko.utils_functions import profile
from teeko.models.coordinate import Coordinate
from teeko.models.position import Position
from teeko.models.teeko_color import get_opponent
from teeko.models.teeko_color import TeekoColorEnum
from teeko.models.movement import Movement
from teeko.models.board import Board
from teeko.models.player.ai_player import AIPlayer

import random


class Justine(AIPlayer):

    levels = [
        GameLevel.EASY, GameLevel.MEDIUM, GameLevel.HARD, GameLevel.IMPOSSIBLE
    ]

    def __init__(self, label: str):
        self._name = "Justine"
        self.level = GameLevel.MEDIUM
        super().__init__(label, True)

    def eval(self, board: Board) -> float:
        if board.is_game_over():
            if board.is_color_winning(self.get_color()):
                return 100000
            else:
                return -100000

        my_positions = board.get_coordinates_by_color(self.get_color())

        value = 40 * Justine.piece_distance_from_center_coef(
            my_positions) + 200 * Justine.piece_distance_togehter_coef(
                my_positions)

        return value

    @staticmethod
    def eval_coordinate(color: TeekoColorEnum, coordinates: Coordinate,
                        opponent_coordinates) -> float:
        ...

    def minmax(self, board: Board, color: TeekoColorEnum, depth: int,
               alpha: float, beta: float) -> float:
        if depth == 0 or board.is_game_over():
            return self.eval(board)

        if color == self.get_color():
            best_value = float("-inf")
            for next_bords in self.generate_next_board_states(board, color):
                value = self.minmax(next_bords, get_opponent(color), depth - 1,
                                    alpha, beta)
                best_value = max(best_value, value)
                alpha = max(alpha, best_value)
                if best_value >= beta:
                    return best_value
                alpha = max(alpha, best_value)
            return best_value
        else:
            best_value = float("inf")
            for next_bords in self.generate_next_board_states(board, color):
                value = self.minmax(next_bords, get_opponent(color), depth - 1,
                                    alpha, beta)
                best_value = min(best_value, value)
                beta = min(beta, best_value)
                if best_value <= alpha:
                    return best_value
                beta = min(beta, best_value)
            return best_value

    @staticmethod
    def piece_distance_from_center_coef(positions: List[Coordinate]) -> float:
        piece_count = len(positions)
        if piece_count == 0:
            return 0
        return 100 / ((sum([
            Position.eucludian_distance(pos, Coordinate(2, 2))
            for pos in positions
        ]) / piece_count) + 1)

    @staticmethod
    def piece_distance_togehter_coef(positions: List[Position]) -> float:
        piece_count = len(positions)
        if piece_count < 2:
            return 0
        coef = 0
        for pos_a in positions:
            for pos_b in positions:
                if pos_a != pos_b:
                    coef += Position.eucludian_distance(pos_a, pos_b)

        return 100 / (coef / piece_count)

    @profile
    def move(self, board: Board, color: TeekoColorEnum) -> Movement:
        if len(board.get_empty_positions()) >= 23:
            deep = 2
        else:
            deep = self.level.value
        best_value = 0
        movements = self.generate_next_movements(board, color)
        best_movement = movements[0]
        print("nb movements: ", len(movements))
        while len(movements) > 0:
            movement = movements.pop()
            next_board = pickle.loads(pickle.dumps(board))
            next_board.move_piece(movement)
            next_value = self.minmax(
                next_board, get_opponent(color), deep - 1, float("-inf"),
                float("inf"))
            if next_value > best_value:
                best_value = next_value
                best_movement = pickle.loads(pickle.dumps(movement))
        print("best movement: ", best_movement)
        return best_movement
