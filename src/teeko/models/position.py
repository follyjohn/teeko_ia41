from typing import List
from teeko.models.coordinate import Coordinate
from teeko.models.teeko_piece import TeekoPieceEnum
import math


class Position:

    def __init__(self, abs: int, ord: int, piece: TeekoPieceEnum):
        self._abs = abs
        self._ord = ord
        self._piece = piece

    @property
    def get_abs(self) -> int:
        return self._abs

    @property
    def get_ord(self) -> int:
        return self._ord

    @property
    def get_piece(self) -> TeekoPieceEnum:
        return self._piece


    def get_coordinate(self) -> Coordinate:
        return Coordinate(self._abs, self._ord)

    @staticmethod
    def eucludian_distance(coord1: Coordinate, coord2: Coordinate) -> float:
        return math.sqrt(math.pow((coord1.get_x - coord2.get_x), 2) + math.pow((coord1.get_y - coord2.get_y), 2))

    @staticmethod
    def manhattan_distance(coord1: Coordinate, coord2: Coordinate) -> int:
        return abs(coord1.get_x - coord2.get_x) + abs(coord1.get_y - coord2.get_y)

    @staticmethod
    def get_coordinate_from_positions(posistions: list) -> List[Coordinate]:
        return [p.get_coordinate() for p in posistions]

    @staticmethod
    def is_positions_square(positions: list) -> bool:
        if len(positions) != 4:
            return False
        positions_coordinates = Position.get_coordinate_from_positions(
            positions)
        for a in positions_coordinates:
            for b in positions_coordinates:
                if a.get_x == b.get_x or a.get_y == b.get_y:
                    if Position.eucludian_distance(a, b) > 1:
                        return False
                elif Position.manhattan_distance(a, b) != 2:
                    return False

        return True

    @staticmethod
    def is_positions_straight_line(positions: list) -> bool:
        if len(positions) < 4:
            return False
        positions_coordinates = Position.get_coordinate_from_positions(
            positions)
        for a in positions_coordinates:
            for b in positions_coordinates:
                if a.get_x == b.get_x or a.get_y == b.get_y:
                    if Position.eucludian_distance(a, b) > 3:
                        return False
                else:
                    return False

        return True

    @staticmethod
    def is_positions_oblique_line(positions: list) -> bool:
        if len(positions) < 4:
            return False
        positions_coordinates = Position.get_coordinate_from_positions(
            positions)
        c = 0
        for a in positions_coordinates:
            for b in positions_coordinates:
                if a != b:
                    if a.get_x == b.get_x  or a.get_y == b.get_y:
                        return False
                    elif Position.manhattan_distance(a, b) > 2:
                        c+=1
                        if c > 4:
                            return False

        return True

    @staticmethod
    def position_is_winning_position(positions: list) -> bool:
        return Position.is_positions_square(positions) or Position.is_positions_straight_line(positions) or Position.is_positions_oblique_line(positions)

    def set_piece(self, piece: TeekoPieceEnum):
        self._piece = piece
