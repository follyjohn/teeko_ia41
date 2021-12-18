import configparser
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
from threading import Thread
from copy import copy
from time import time


class Yaw(AIPlayer):
    levels = [GameLevel.EASY, GameLevel.MEDIUM, GameLevel.HARD]
    level = GameLevel.EASY

    def _init_(self):
        super().__init__()
        self.level = GameLevel.EASY

    def get_levels(self) -> List[GameLevel]:
        return self.levels

    def set_level(self, level: GameLevel):
        self.level = level

    def has_level(self):
        return True

    @staticmethod
    def _get_player_info() -> str:
        default_name = "Yaw"
        config = configparser.RawConfigParser()
        with open('config.ini', 'r') as configfile:
            config.read_file(configfile)
            if config['DEFAULT']['noui'] == 'no':
                return default_name
            else:
                awnser = input(
                    "Do you want to change the name of the ai ? (y/n), q to quit: ")
                while awnser != "y" and awnser != "n" and awnser != "q":
                    awnser = input(
                        "Do you want to change the name of the ai ? (y/n), q to quit: ")
                if awnser == "y":
                    name = input("Enter the name of the ai : ")
                    while not re.fullmatch(r'[a-zA-Z0-9]+', name):
                        name = input(
                            "Invalid name,use only letters and numbers, please try again : ")
                    return str(name)
                elif awnser == "q":
                    print("Quitting")
                    exit()
                elif awnser == "n":
                    return default_name

    @staticmethod
    def eval(board: Board, color: TeekoColorEnum) -> float:

        if board.is_game_over():
            value = 100000
        else:
            player_position = board.get_coordinates_by_color(color)
            opponent_position = board.get_positions_by_color(get_opponent(color))
            empty_position = board.get_empty_positions_coordinate()
            value = 40*Yaw.piece_distance_from_center_coef(player_position) + 60*Yaw.piece_distance_togehter_coef(player_position)

        return value

    @staticmethod
    def negamax(board: Board, color: TeekoColorEnum, depth: int, alpha: float, beta: float) -> float:
        if depth == 0 or board.is_game_over():
            return -Yaw.eval(board, color)

        best_value = float("-inf")
        for next_bords in Yaw.generate_next_board_states(board, color):
            value = -Yaw.negamax(
                next_bords, get_opponent(color), depth-1, -beta, -alpha)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if best_value >= beta:
                return best_value
            alpha = max(alpha, best_value)
        return best_value

    @staticmethod
    def minmax(board: Board, color: TeekoColorEnum, depth: int, is_max: bool, alpha: float, beta: float) -> float:
        if depth == 0 or board.is_game_over():
            return Yaw.eval(board, color)

        if is_max:
            best_value = float("-inf")
            for next_bords in Yaw.generate_next_board_states(board, color):
                value = Yaw.minmax(
                    next_bords, get_opponent(color), depth-1, False, alpha, beta)
                best_value = max(best_value, value)
                alpha = max(alpha, best_value)
                if best_value >= beta:
                    return best_value
                alpha = max(alpha, best_value)
            return best_value
        else:
            best_value = float("inf")
            for next_bords in Yaw.generate_next_board_states(board, color):
                value = Yaw.minmax(
                    next_bords, get_opponent(color), depth-1, True, alpha, beta)
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
        return 100/((sum([Position.eucludian_distance(pos, Coordinate(2, 2)) for pos in positions])/piece_count)+1)

    @staticmethod
    def piece_distance_togehter_coef(positions: List[Coordinate]) -> float:
        piece_count = len(positions)
        if piece_count < 2:
            return 0
        coef = 0
        for pos_a in positions:
            for pos_b in positions:
                if pos_a != pos_b:
                    coef += Position.eucludian_distance(pos_a, pos_b)

        return 100/(coef/piece_count)

    @profile
    def move(self, board: Board, color: TeekoColorEnum) -> Movement:
        deep = self.level.value

        if len(board.get_empty_positions()) >= 23:
            deep = 2
        best_value = Yaw.minmax(
            board, color, deep, True, float("-inf"), float("inf"), )
        movements = self.generate_next_movements(board, color)
        while len(movements) > 0:
            movement = movements.pop()
            next_board = pickle.loads(pickle.dumps(board))
            next_board.move_piece(movement)
            next_value = Yaw.minmax(next_board, get_opponent(
                color), deep-1, False, float("-inf"), float("inf"))
            if next_value == best_value:
                return movement
