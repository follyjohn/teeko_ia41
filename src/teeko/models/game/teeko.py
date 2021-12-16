from abc import ABC, abstractmethod

from teeko.models.game.game_level import GameLevel
from teeko.models.game.game_mode import GameMode

class TeekoGame(ABC):

    def __init__(self):
        self.players = {}
        self._mode = None
        self._level = None
        self._winner: Player = None
        self._introduce_game()
        self._select_game_mode()
        self._initialise_player()
        self._initilise_board()

    def set_mode(self, mode: GameMode):
        self._mode = mode

    def get_mode(self) -> GameMode:
        return self._mode
    
    def set_level(self, level:GameLevel):
        self._level = level

    def get_level(self) -> GameLevel:
        return self._level

    @abstractmethod
    def _introduce_game(self):
        ...

    @abstractmethod
    def _initialise_player(self):
        ...

    @abstractmethod
    def _initilise_board(self):
        ...

    @abstractmethod
    def _select_game_mode(self):
        ...
