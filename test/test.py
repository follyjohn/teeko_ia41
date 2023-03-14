from typing import List, Optional, Dict, Any
from enum import Enum
from abc import ABC, abstractmethod
import math
import re
import copy


"""
    Metadata: 
        author:    follyjohn
        date:      2021-11-21
        purpose:   Teeko Piece category

    Description: Enum class for the game. This class is used to represent the different categories of pieces in the game. 
"""


class TeekoPieceEnum(Enum):
    BLACK_PIECE = "a"  # Black piece for the player a
    RED_PIECE = "b"  # Red piece for the player b
    EMPTY_PIECE = " "  # Empty piece for the empty emplacement of the board


class TeekoColorEnum(Enum):
    BLACK_COLOR = "black"
    RED_COLOR = "red"


"""
    color_to_piece: return the piece corresponding to the color
"""


def color_to_piece(color: TeekoColorEnum) -> TeekoPieceEnum:
    if color == TeekoColorEnum.BLACK_COLOR:
        return TeekoPieceEnum.BLACK_PIECE
    elif color == TeekoColorEnum.RED_COLOR:
        return TeekoPieceEnum.RED_PIECE
    else:
        raise ValueError("Color not found")


"""
    piece_to_color_str: return the color corresponding to the piece
"""


def piece_to_color(piece: TeekoPieceEnum) -> TeekoColorEnum:
    if piece == TeekoPieceEnum.BLACK_PIECE:
        return TeekoColorEnum.BLACK_COLOR
    elif piece == TeekoPieceEnum.RED_PIECE:
        return TeekoColorEnum.RED_COLOR
    else:
        raise ValueError("Piece not found")


class Coordinate:

    def __init__(self, x: int, y: int):
        # Coodinate values must be (-1, -1), or (a,b) where a and b are between 0 and 4
        if(x < -1 or x > 4 or y < -1 or y > 4) or (x == -1 and y != -1) or (x != -1 and y == -1):
            raise ValueError("Invalid coordinate")
        self._x = x
        self._y = y

    def __eq__(self, other) -> bool:
        return self.get_x() == other.get_x() and self.get_y() == other.get_y()

    def __hash__(self):
        return hash((self.get_x(), self.get_y()))

    def __str__(self):
        return "(" + str(self.get_x()) + ", " + str(self.get_y()) + ")"

    def __repr__(self):
        return "(" + str(self.get_x()) + ", " + str(self.get_y()) + ")"

    @staticmethod
    def append_coordinate(coordinate, list: List):
        if coordinate.is_geometric():
            list.append(coordinate)

    @property
    def get_x(self) -> int:
        return self._x

    @property
    def get_y(self) -> int:
        return self._y

    @staticmethod
    def is_valid_coordinate(x: int, y: int) -> bool:
        return x >= 0 and x <= 4 and y >= 0 and y <= 4

    def is_geometric(self) -> bool:
        return self.get_x() >= 0 and self.get_x() <= 4 and self.get_y() >= 0 and self.get_y() <= 4

    @staticmethod
    def append_coordinate(coordinate, coordinates: List) -> List:
        if coordinate.is_geometric():
            coordinates.append(coordinate)
        return coordinates

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def get_next_coordinates(self) -> List:
        next_coordinates = []
        if self.get_x() != -1 and self.get_y() != -1:
            Coordinate.append_coordinate(Coordinate(
                self.get_x() + 1, self.get_y()), next_coordinates)
            Coordinate.append_coordinate(Coordinate(
                self.get_x() - 1, self.get_y()), next_coordinates)
            Coordinate.append_coordinate(Coordinate(
                self.get_x(), self.get_y() + 1), next_coordinates)
            Coordinate.append_coordinate(Coordinate(
                self.get_x(), self.get_y() - 1), next_coordinates)
            Coordinate.append_coordinate(Coordinate(
                self.get_x() + 1, self.get_y() + 1), next_coordinates)
            Coordinate.append_coordinate(Coordinate(
                self.get_x() - 1, self.get_y() - 1), next_coordinates)
            Coordinate.append_coordinate(Coordinate(
                self.get_x() + 1, self.get_y() - 1), next_coordinates)
            Coordinate.append_coordinate(Coordinate(
                self.get_x() + 1, self.get_y() - 1), next_coordinates)

        return next_coordinates


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
        return math.sqrt(math.pow((coord1.get_x() - coord2.get_x()), 2) + math.pow((coord1.get_y() - coord2.get_y()), 2))

    @staticmethod
    def manhattan_distance(coord1: Coordinate, coord2: Coordinate) -> int:
        return abs(coord1.get_x() - coord2.get_x()) + abs(coord1.get_y() - coord2.get_y())

    @staticmethod
    def get_coordinate_from_positions(posistions: list) -> List[Coordinate]:
        return [p.get_coordinate() for p in posistions]

    @staticmethod
    def is_positions_square(positions: list) -> bool:
        if len(positions) < 4:
            return False
        positions_coordinates = Position.get_coordinate_from_positions(positions)
        for a in positions_coordinates:
            for b in positions_coordinates:
                if a.get_x() == b.get_x() or a.get_y() == b.get_y():
                    if Position.eucludian_distance(a, b) > 1:
                        return False
                elif Position.manhattan_distance(a, b) != 2:
                    return False

        return True

    @staticmethod
    def is_positions_straight_line(positions: list) -> bool:
        if len(positions) < 4:
            return False
        positions_coordinates = Position.get_coordinate_from_positions(positions)
        for a in positions_coordinates:
            for b in positions_coordinates:
                if a.get_x() == b.get_x() or a.get_y() == b.get_y():
                    if Position.eucludian_distance(a, b) > 3:
                        return False
                else:
                    return False

        return True

    @staticmethod
    def is_positions_oblique_line(positions: list) -> bool:
        if len(positions) < 4:
            return False
        positions_coordinates = Position.get_coordinate_from_positions(positions)
        for a in positions_coordinates:
            for b in positions_coordinates:
                if (a.get_x() == b.get_x() and a.get_y() != b.get_y()) or (a.get_y() == b.get_y() and a.get_x() != b.get_x()):
                    return False
                elif Position.manhattan_distance(a, b) > 6:
                    print("dd")
                    return False

        return True
                

    def set_piece(self, piece: TeekoPieceEnum):
        self._piece = piece


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
        positions = [p for p in self._positions if p.get_abs == coord.get_x() and p.get_ord == coord.get_y()]
        if len(positions) == 0:
            return None
        return positions[0]

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
      return Position.get_coordinate_from_positions(self.get_empty_positions())

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
                    if p.piece.value == TeekoPieceEnum.EMPTY_PIECE.value:
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
        return self.get_origin_coord.get_x() == -1 and self.get_origin_coord.get_y() == -1

    def __str__(self):
        return "Movement: " + self._origin_coord.__str__() + " -> " + self._destination_coord.__str__()

    def is_legal_movement(self, board: Board) -> bool:
        if self.get_piece_color is None:
            print("Piece color not set")
            return False
        elif self.is_new_piece_movement() and board.get_remaining_pieces_by_color(piece_to_color(self.get_piece_color)) == 0:
            print("No more pieces of this color")
        elif not self.is_new_piece_movement():
            if Position.eucludian_distance(self.get_origin_coord, self.get_destination_coord) != 1:
                print("Movement is not a single step")
                return False
            if board.get_remaining_pieces_by_color(piece_to_color(self.get_piece_color)) > 0:
                print("Piece color not empty")
                return False
            if self.get_origin_coord.get_x() == self.get_destination_coord.get_x() and self.get_origin_coord.get_y() == self.get_destination_coord.get_y():
                print("The movement is not a step")
                return False
            if board.get_piece_at_coordinate(self.get_origin_coord) == TeekoPieceEnum.EMPTY_PIECE:
                print("No piece at position")
                return False
            elif board.get_piece_at_coordinate(self.get_origin_coord) != self.get_piece_color:
                print("The piece at position is not yours")
                return False
        elif not board.get_piece_at_coordinate(self.get_destination_coord) == TeekoPieceEnum.EMPTY_PIECE:
            print("Destination not empty")
            return False

        return True


# def move_piece(board: Board, movement: Movement) -> Board:
#     board_copy = copy.deepcopy(board)
#     if movement.is_new_piece_movement():
#         board.add_piece(movement.get_destination_coord, movement.get_piece_color)
#     else:
#         board.move_piece(movement.get_origin_coord, movement.get_destination_coord)
#     return board


class Player(ABC):

    """
    Abstract method that must be implemented by the subclasses for methods to get player information; actually the name of the player.
    Returns:
        str: String containing the name of the player.
    """
    @staticmethod
    @abstractmethod
    def _get_player_info() -> str:
        pass

    @abstractmethod
    def __init__(self):
        self._name = self._get_player_info()

    # Abstract method that must be implemented by subclass to pretty print the player.

    @abstractmethod
    def print_player(self):
        print("Player : ", self._name)

    """Abstract method that must be implemented by the subclasses for methods to get the next move from the player.
    We pass the board to the method so that the player can make a decision based on the current state of the board in the case of IA player.
    Returns:
        Movement: Movement object containing the coordinates of the movement.
    """
    @abstractmethod
    def move(self, board: Board) -> Movement:
        pass

    def get_name(self):
        return self._name


class IAPlayer(Player):

    def __init__(self):
        super().__init__()

    @staticmethod
    def _get_player_info() -> str:
        return str("William")

    def print_player(self):
        super().print_player()

    def move(self, board: Board) -> Movement:  # TODO: implement the minimax algorithm
        pass

    def get_name(self):
        return super().get_name()

    # Generate next possible moves form one state (state -> states)
    @staticmethod
    def generate_next_movements(board: Board, color: TeekoColorEnum) -> List[Movement]:
        movements = []
        if int(board.get_remaining_pieces_by_color(color)) >= 1:
            print("yes")
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
                            Movement(departure_coord, arrival_coord, color))

        return movements

    @staticmethod
    def generate_next_board_state(board: Board, movement: Movement) -> Board:
        if movement.is_legal_movement(board):
            new_board = copy.deepcopy(board)
            new_board.move_piece(movement)
            return new_board

    @staticmethod
    def generate_next_board_states(board: Board, color: TeekoColorEnum) -> List[Board]:
        movements = IAPlayer.generate_next_movements(board, color)
        boards = []
        for movement in movements:
            boards.append(IAPlayer.generate_next_board_state(board, movement))
        return boards


board = Board()
board.display()

next_boards = IAPlayer.generate_next_board_states(
    board, TeekoColorEnum.BLACK_COLOR)
print(len(next_boards))

for board in next_boards:
  board.display()
