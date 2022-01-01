"""
    Metadata: 
        date:      2021-11-21
        purpose:   IA Player class

    Description: AI Player class for the game. This class is used to represent an AI player in the game.
    The particularity of this class is that it uses the Minimax algorithm to get the next move from the player.

"""
import re
import configparser
import copy
import pickle
from abc import ABC, abstractmethod
from typing import List
from teeko.view.set_human_player import set_human_player
from teeko.view.show_message_utils import yes_or_no
from teeko.models.game.game_level import GameLevel
from teeko.models.teeko_color import color_to_piece
from teeko.models.position import Position
from teeko.models.teeko_color import TeekoColorEnum

from teeko.models.board import Board
from teeko.models.coordinate import Coordinate
from teeko.models.movement import Movement
from teeko.models.player.player import Player


class AIPlayer(Player):

    def __init__(self, label: str, has_level: bool = False):
        self._has_level = has_level
        super().__init__(label)
        

    def has_level(self) -> bool:
        return self._has_level

    def get_color(self) -> TeekoColorEnum:
        return self._color

    def get_label(self) -> str:
        return self._label

    def set_color(self, color: TeekoColorEnum):
        if self._color is None:
            self._color = color

    def set_label(self, label: str):
        self._label = label

    def get_levels(self) -> List[GameLevel]:
        return self.levels

    def set_level(self, level: GameLevel):
        self.level = GameLevel(level)

    def _get_player_info(self) -> str:
        default_name = self._name
        config = configparser.RawConfigParser()
        with open('config.ini', 'r') as configfile:
            config.read_file(configfile)
            if config['DEFAULT']['noui'] == 'no':
                # return default_name
                if yes_or_no() == True:
                    username = set_human_player("Type the new name of the ai :")
                    return username
                else:
                    return default_name
            else:
                awnser = input(
                    "Do you want to change the name of the ai ? (y/n), q to quit: "
                )
                while awnser != "y" and awnser != "n" and awnser != "q":
                    awnser = input(
                        "Do you want to change the name of the ai ? (y/n), q to quit: "
                    )
                if awnser == "y":
                    name = input("Enter the name of the ai : ")
                    while not re.fullmatch(r'[a-zA-Z0-9]+', name):
                        name = input(
                            "Invalid name,use only letters and numbers, please try again : "
                        )
                    return str(name)
                elif awnser == "q":
                    print("Quitting")
                    exit()
                elif awnser == "n":
                    return default_name

    def print_player(self):
        super().print_player()

    # TODO: implement the minimax algorithm
    def move(self, board: Board, color: TeekoColorEnum) -> Movement:
        pass

    def get_name(self):
        return super().get_name()

    # Generate next possible moves form one state (state -> states)
    # Generate next possible moves form one state (state -> states)
    @staticmethod
    def generate_next_movements(board: Board, color: TeekoColorEnum) -> List[Movement]:
        movements = []
        if board.get_remaining_pieces_by_color(color) >= 1: #  laying phase
            departure_coord = Coordinate(-1, -1)
            for arrival_coord in board.get_empty_positions_coordinate():
                movements.append(
                    Movement(departure_coord, arrival_coord, color_to_piece(color)))
        else: # after the laying phase
            departure_positions = board.get_positions_by_color(color)
            departure_coords = Position.get_coordinate_from_positions(
                departure_positions)
            for departure_coord in departure_coords:
                for arrival_coord in departure_coord.get_next_coordinates():
                    if arrival_coord in board.get_empty_positions_coordinate():
                        movements.append(
                            Movement(departure_coord, arrival_coord, color_to_piece(color)))

        return movements

    @staticmethod
    def generate_next_board_state(board: Board, movement: Movement) -> Board:
        if movement.is_legal_movement(board):
            new_board = pickle.loads(pickle.dumps(board))
            new_board.move_piece(movement)
            return new_board

    @staticmethod
    def generate_next_board_states(board: Board, color: TeekoColorEnum) -> List[Board]:
        movements = AIPlayer.generate_next_movements(board, color)
        boards = []
        for movement in movements:
            boards.append(AIPlayer.generate_next_board_state(board, movement))
        return boards

# Alan Noel Leonie Israël
