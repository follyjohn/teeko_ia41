from abc import ABC, abstractmethod

class TeekoGame(ABC):

    def __init__(self):
        self.players = {}
        self._winner: Player = None
        self._introduce_game()
        self._initialise_player()
        self._initilise_board()

    @abstractmethod
    def _introduce_game(self):
        ...

    @abstractmethod
    def _initialise_player(self):
        ...

    @abstractmethod
    def _initilise_board(self):
        ...
