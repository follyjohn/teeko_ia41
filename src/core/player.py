"""
    Metadata:
        author:    follyjohn
        date:      2021-11-21
        purpose:   Player class

    Description: Player class for the game. This class is used to represent a player in the game.
    It's the base class for the HumanPlayer and the AIPlayer classes.
    It contains abstract methods that must be implemented by the subclasses for
        methods to get the next move from the player.

"""
from abc import ABC, abstractmethod
from .teeko_color import TeekoColorEnum
from .board import Board
from .movement import Movement


class Player(ABC):
    @staticmethod
    @abstractmethod
    def _get_player_info() -> str:
        """Abstract method that must be implemented by the subclasses for methods to get player information;
        actually the name of the player.
        Returns:
            str: String containing the name of the player.
        """
        pass

    @abstractmethod
    def __init__(self):
        self._name = self._get_player_info()

    @abstractmethod
    def print_player(self):
        # Abstract method that must be implemented by subclass to pretty print the player.
        print("Player : ", self._name)

    @abstractmethod
    def move(self, board: Board, color: TeekoColorEnum) -> Movement:
        """Abstract method that must be implemented by the subclasses for methods to get the next move from the player.
        We pass the board to the method so that the player can make a decision based on
        the current state of the board in the case of IA player.
        Returns:
            Movement: Movement object containing the coordinates of the movement.
        """
        pass

    def get_name(self):
        return self._name
