"""
    Metadata:
        author:    follyjohn
        date:      2021-11-21
        purpose:   IA Player class

    Description: IA Player class for the game. This class is used to represent an IA player in the game.
    The particularity of this class is that it uses the Minimax algorithm to get the next move from the player.

"""
import re
import copy
import pickle
from typing import List
from src.models.teeko_color import color_to_piece
from src.models.position import Position
from src.models.teeko_color import TeekoColorEnum

from src.models.board import Board
from src.models.coordinate import Coordinate
from src.models.movement import Movement
from src.models.player.player import Player


class IAPlayer(Player):

    def __init__(self):
        super().__init__()

    @staticmethod
    def _get_player_info() -> str:
        return str("William")

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
        if board.get_remaining_pieces_by_color(color) >= 1:
            departure_coord = Coordinate(-1, -1)
            for arrival_coord in board.get_empty_positions_coordinate():
                movements.append(
                    Movement(departure_coord, arrival_coord, color_to_piece(color)))
        else:
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
        movements = IAPlayer.generate_next_movements(board, color)
        boards = []
        for movement in movements:
            boards.append(IAPlayer.generate_next_board_state(board, movement))
        return boards

# Alan Noel Leonie Israël