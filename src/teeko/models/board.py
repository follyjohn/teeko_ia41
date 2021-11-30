from typing import List, Optional, Dict, Any
from teeko.models.coordinate import Coordinate
from teeko.models.position import Position
from teeko.models.teeko_piece import TeekoPieceEnum
from teeko.models.teeko_color import TeekoColorEnum, color_to_piece, piece_to_color


class Board:

    def __init__(self, size: int = 5, piece_count: int = 4):
        self._size = size
        self._piece_count = piece_count
        self._positions = self.generate()

    @property
    def size(self) -> int:
        return self._size

    @property
    def positions(self) -> List[Position]:
        return self._positions

    def piece_count(self) -> int:
        return self._piece_count

    def generate(self):
        positions: List[Position] = []
        for x in range(self.size):
            for y in range(self.size):
                p = Position(x, y, TeekoPieceEnum.EMPTY_PIECE)
                positions.append(p)
        return positions

    def get_piece_at_coordinate(self, abs: int, obs: int) -> TeekoPieceEnum:
        return self.get_position(abs, obs).get_piece

    def display(self):
        for x in range(self.size):
            print("| ", end="")
            for y in range(self.size):
                p = self.get_position(y, x)
                print(p.get_piece.value, end=" | ")
            print()
        print()

        print("Remaining pieces:")

        print("Black:", self.get_remaining_pieces_by_color(
            TeekoColorEnum.BLACK_COLOR))
        print("Red:", self.get_remaining_pieces_by_color(
            TeekoColorEnum.RED_COLOR))
        print()

    def move_piece(self, movement):  # TODO:type movement
        if not movement.is_new_piece_movement():
            self.get_position_at_coordinate(
                movement.get_origin_coord).set_piece(TeekoPieceEnum.EMPTY_PIECE)

        self.get_position_at_coordinate(
            movement.get_destination_coord).set_piece(movement.get_piece_color)

    def get_position(self, x: int, y: int) -> Position:
        return [p for p in self._positions if p.get_abs == x and p.get_ord == y][0]

    def get_position_at_coordinate(self, coord: Coordinate) -> Position:
        for p in self._positions:
            if p.get_abs == coord.get_x and p.get_ord == coord.get_y:
                return p

    def get_piece_at_coordinate(self, coord: Coordinate) -> TeekoPieceEnum:
        return self.get_position_at_coordinate(coord).get_piece

    def get_pieces_positions(self) -> Dict[TeekoColorEnum, List[Position]]:
        pieces_positions: Dict[TeekoColorEnum, List[Position]] = {}
        for color in [TeekoColorEnum.BLACK_COLOR, TeekoColorEnum.RED_COLOR]:
            pieces_positions[color] = self.get_positions_by_color(color)
        return pieces_positions

    def get_pieces_positions_list(self) -> List[Position]:
        pieces_positions: List[Position] = []
        for p in self._positions:
            if p.get_piece.value != TeekoPieceEnum.EMPTY_PIECE.value:
                pieces_positions.append(p)
        return pieces_positions

    def get_positions_by_color(self, color: TeekoColorEnum) -> List[Position]:
        return [p for p in self._positions if p.get_piece == color_to_piece(color)]

    def get_empty_positions(self) -> List[Position]:
        return [p for p in self._positions if p.get_piece == TeekoPieceEnum.EMPTY_PIECE]

    def get_empty_positions_coordinate(self) -> List[Coordinate]:
      return Position.get_coordinates_from_positions(self.get_empty_positions())

    def get_neighbors(self, x: int, y: int) -> List[Position]:
        neighbors: List[Position] = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if x + i >= 0 and x + i < self.size and y + j >= 0 and y + j < self.size:
                    neighbors.append(self.get_position(x + i, y + j))
        return neighbors

    def get_neighbors_empty(self, x: int, y: int) -> List[Position]:
        neighbors: List[Position] = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if x + i >= 0 and x + i < self.size and y + j >= 0 and y + j < self.size:
                    p = self.get_position(x + i, y + j)
                    if p.get_piece == TeekoPieceEnum.EMPTY_PIECE:
                        neighbors.append(p)
        return neighbors

    def get_neighbors_piece(self, x: int, y: int, color: TeekoColorEnum) -> List[Position]:
        neighbors: List[Position] = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if x + i >= 0 and x + i < self.size and y + j >= 0 and y + j < self.size:
                    p = self.get_position(x + i, y + j)
                    if p.piece.value == color.value:
                        neighbors.append(p)

        return neighbors

    def piece_count_by_color(self, color: TeekoColorEnum) -> int:
        return len(self.get_positions_by_color(color))

    def get_piece_count(self, piece: TeekoPieceEnum) -> int:
        if piece == TeekoPieceEnum.EMPTY_PIECE:
            return len(self.get_empty_positions())
        return self.piece_count_by_color(piece_to_color(piece))

    def get_remaining_pieces_by_color(self, color: TeekoColorEnum) -> int:
        return self._piece_count - self.piece_count_by_color(color)
