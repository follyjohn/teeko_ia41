"""
    Metadata: 
        author:    follyjohn
        date:      2021-11-21
        purpose:   Coordinate class

    Description: Simple class to represent a coordinate in the game.
"""

class Coordinate:

    def __init__(self, x: int, y: int):
        if(x < -1 or x > 4 or y < -1 or y > 4) or (x == -1 and y != -1) or (x != -1 and y == -1): # Coodinate values must be (-1, -1), or (a,b) where a and b are between 0 and 4
            raise ValueError("Invalid coordinate")
        self._x = x
        self._y = y

    @property
    def get_x(self) -> int:
        return self._x

    @property
    def get_y(self) -> int:
        return self._y

