from typing import List
from src.models.position import Position
from src.models.board import Board
import re
from src.models.coordinate import Coordinate
from src.models.teeko_color import piece_to_color
from src.models.teeko_piece import TeekoPieceEnum


class Movement:

    def __init__(self, origin_coord: Coordinate, destination_coord: Coordinate):
        self._origin_coord = origin_coord
        self._destination_coord = destination_coord
        self._piece_color = None

    def __init__(self, origin_coord: Coordinate, destination_coord: Coordinate, piece_color: TeekoPieceEnum):
        self._origin_coord = origin_coord
        self._destination_coord = destination_coord
        self._piece_color = piece_color

    @property
    def get_piece_color(self) -> TeekoPieceEnum:
        return self._piece_color

    @property
    def get_origin_coord(self) -> Coordinate:
        return self._origin_coord

    @property
    def get_destination_coord(self) -> Coordinate:
        return self._destination_coord

    def set_piece_color(self, color: TeekoPieceEnum) -> None:
        if color is TeekoPieceEnum.EMPTY_PIECE:
            raise ValueError("Piece color cannot be empty")
        else:
            self._piece_color = color

    def is_new_piece_movement(self) -> bool:
        return self.get_origin_coord.get_x == -1 and self.get_origin_coord.get_y == -1

    def __str__(self):
        return "Movement: " + self._origin_coord.__str__() + " -> " + self._destination_coord.__str__()

    def is_legal_movement(self, board: Board) -> bool:
        if self.get_piece_color is None:
            print("Piece color not set")
            return False
        elif self.is_new_piece_movement() and board.get_remaining_pieces_by_color(piece_to_color(self.get_piece_color)) == 0:
            print("No more pieces of this color")
            return False
        elif not self.is_new_piece_movement():
            if Position.manhattan_distance(self.get_origin_coord, self.get_destination_coord) > 1:
                if Position.eucludian_distance(self.get_origin_coord, self.get_destination_coord) > 1.5:
                    print("Movement is not a single step")
                    return False
            if board.get_remaining_pieces_by_color(piece_to_color(self.get_piece_color)) > 0:
                print("Piece color not empty")
                return False
            if self.get_origin_coord.get_x == self.get_destination_coord.get_x and self.get_origin_coord.get_y == self.get_destination_coord.get_y:
                print("The movement is not a step")
                return False
            if board.get_piece_at_coordinate(self.get_origin_coord) == TeekoPieceEnum.EMPTY_PIECE:
                print("No piece at position")
                return False
            elif board.get_piece_at_coordinate(self.get_origin_coord) != self.get_piece_color:
                print("The piece at position is not yours")
                return False
        if not board.get_piece_at_coordinate(self.get_destination_coord) == TeekoPieceEnum.EMPTY_PIECE:
            print("Destination not empty")
            return False

        return True
