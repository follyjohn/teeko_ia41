from typing import List


class Coordinate:
    def __init__(self, x: int, y: int):
        # Coodinate values must be (-1, -1), or (a,b) where a and b are between 0 and 4
        if (x < -1 or x > 4 or y < -1 or y > 4) or (x == -1 and y != -1) or (x != -1 and y == -1):
            raise ValueError("Invalid coordinate")
        self._x = x
        self._y = y

    @staticmethod
    def is_valid_coordinate(x: int, y: int) -> bool:
        return x >= 0 and x <= 4 and y >= 0 and y <= 4

    def is_geometric(self) -> bool:
        return self.get_x >= 0 and self.get_x <= 4 and self.get_y >= 0 and self.get_y <= 4

    def __eq__(self, other) -> bool:
        return self.get_x == other.get_x and self.get_y == other.get_y

    @staticmethod
    def append_coordinate(x: int, y: int, coordinates) -> List:
        if Coordinate.is_valid_coordinate(x, y):
            coordinates.append(Coordinate(x, y))
        return coordinates

    @property
    def get_x(self) -> int:
        return self._x

    @property
    def get_y(self) -> int:
        return self._y

    def get_next_coordinates(self) -> List:
        next_coordinates = []
        if self.get_x != -1 and self.get_y != -1:
            Coordinate.append_coordinate(self.get_x, self.get_y + 1, next_coordinates)
            Coordinate.append_coordinate(self.get_x, self.get_y - 1, next_coordinates)
            Coordinate.append_coordinate(self.get_x + 1, self.get_y, next_coordinates)
            Coordinate.append_coordinate(self.get_x - 1, self.get_y, next_coordinates)
            Coordinate.append_coordinate(self.get_x + 1, self.get_y + 1, next_coordinates)
            Coordinate.append_coordinate(self.get_x - 1, self.get_y - 1, next_coordinates)
            Coordinate.append_coordinate(self.get_x + 1, self.get_y - 1, next_coordinates)
            Coordinate.append_coordinate(self.get_x - 1, self.get_y + 1, next_coordinates)

        return next_coordinates

    def __str__(self) -> str:
        return "(" + str(self.get_x) + "," + str(self.get_y) + ")"
