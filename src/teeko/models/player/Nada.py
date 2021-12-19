import configparser
import pickle
import re
from typing import List
from teeko.utils_functions import profile
from teeko.models.coordinate import Coordinate
from teeko.models.position import Position
from teeko.models.teeko_color import get_opponent
from teeko.models.teeko_color import TeekoColorEnum
from teeko.models.movement import Movement
from teeko.models.board import Board
from teeko.models.player.ai_player import AIPlayer
import random
from threading import Thread
from copy import copy
from time import time
import functools


def foo():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args):
             # Some fancy foo stuff
            return await func(*args)
        return wrapped
    return wrapper

def boo():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args):
            # Some fancy boo stuff
            return await func(*args)
        return wrapped
    return wrapper

class Nada(AIPlayer):
    
    def __init__(self):
        super().__init__()
        
    def get_color(self) -> TeekoColorEnum:
        return self._color

    def get_label(self) -> str:
        return self._label

    def set_color(self, color: TeekoColorEnum):
        if self._color is None:
            self._color = color

    def set_label(self, label: str):
        self._label = label

    @staticmethod
    def _get_player_info() -> str:
        default_name = "Nada"
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

    def eval(self, board: Board) -> float:
        if board.is_game_over():
            if board.is_color_winning(self.get_color()):
                return 100000
            else:
                return -100000
            
        my_positions = board.get_coordinates_by_color(self.get_color())
        # opponent_positions = board.get_positions_by_color(get_opponent(self.get_color()))
        # empty_position = board.get_empty_positions_coordinate()
        
        value = 40*Nada.piece_distance_from_center_coef(my_positions) + 60*Nada.piece_distance_togehter_coef(my_positions)

        return value

    @staticmethod
    def eval_coordinate(color: TeekoColorEnum, coordinates: Coordinate, opponent_coordinates) -> float:
        ...

    def minmax(self, board: Board, color: TeekoColorEnum, depth: int, alpha: float, beta: float) -> float:
        if depth == 0 or board.is_game_over():
            return self.eval(board)

        if color == self.get_color():
            best_value = float("-inf")
            for next_bords in self.generate_next_board_states(board, color):
                value = self.minmax(
                    next_bords, get_opponent(color), depth-1, alpha, beta)
                best_value = max(best_value, value)
                alpha = max(alpha, best_value)
                if best_value >= beta:
                    return best_value
                alpha = max(alpha, best_value)
            return best_value
        else:
            best_value = float("inf")
            for next_bords in self.generate_next_board_states(board, color):
                value = self.minmax(
                    next_bords, get_opponent(color), depth-1, alpha, beta)
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
    def piece_distance_togehter_coef(positions: List[Position]) -> float:
        piece_count = len(positions)
        if piece_count < 2:
            return 0
        coef = 0
        for pos_a in positions:
            for pos_b in positions:
                if pos_a != pos_b:
                    coef += Position.eucludian_distance(pos_a, pos_b)

        return 100/(coef/piece_count)
    
    # @foo()
    # @boo()
    @profile
    def move(self, board: Board, color: TeekoColorEnum) -> Movement:
        if len(board.get_empty_positions()) >= 23:
            deep = 2
        # elif len(board.get_empty_positions()) >= 18:
        #     deep = 3
        else :
            deep = 2
        best_value = self.minmax(board, color, deep, float("-inf"), float("inf"))
        print("best value : " + str(best_value))
        movements = self.generate_next_movements(board, color)
        while len(movements) > 0:
            movement = movements.pop()
            next_board = pickle.loads(pickle.dumps(board))
            next_board.move_piece(movement)
            next_value = self.minmax(next_board, get_opponent(color), deep-1, float("-inf"), float("inf"))
            if next_value == best_value:
                return movement

