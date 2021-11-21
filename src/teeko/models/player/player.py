import re
from abc import ABC, abstractmethod

from teeko.models.board import Board
from teeko.models.movement import Movement


class Player(ABC):

    @staticmethod
    @abstractmethod
    def _get_player_info() -> str:
        pass

    @abstractmethod
    def __init__(self):
        self._name = self._get_player_info()

    @abstractmethod
    def print_player(self):
        print("player : ", self._name)

    @abstractmethod
    def move(self, board: Board) -> Movement:
        pass


    def get_name(self):
        return self._name





