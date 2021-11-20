from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, List, Optional
from teeko.models.board import Board

from teeko.models.player.player import HumanPlayer, Player
from teeko.models.position import Position
from teeko.models.teeko_color import TeekoColorEnum, color_to_piece
from teeko.models.teeko_piece import TeekoPieceEnum

class Game:

    def __init__(self):
        self.players = {}
        self._winner: Player = None
        self._introduce_game()
        self._initialise_player()
        self._initilise_board()

    @staticmethod
    @abstractmethod
    def _introduce_game(self):
        ...

    @staticmethod
    @abstractmethod
    def _initialise_player(self):
        ...

    @staticmethod
    @abstractmethod
    def _initilise_board(self):
        ...

class Teeko(Game):

    def __init__(self):
        super().__init__()
        

    def _introduce_game(self):
        print("Welcome to Teeko")

    def _initialise_player(self):
        print("Initialise player")
        player_a = HumanPlayer()
        player_b = HumanPlayer()
        self.set_black_player(player_a)
        self.set_withe_player(player_b)

    def _initilise_board(self):
        print("Initialise board")
        self.board = Board()
        self.board.display()

        
    def is_game_over(self) -> bool:
        black_pieces = self.board.get_positions_by_color(TeekoColorEnum.BLACK_COLOR)
        white_pieces = self.board.get_positions_by_color(TeekoColorEnum.WHITE_COLOR)

        if len(black_pieces) == 4:
            if Position.is_positions_square(black_pieces) or Position.is_positions_straight_line(black_pieces) or Position.is_positions_oblique_line(black_pieces):
                self._winner = self.get_black_player()
                return True
            
        if len(white_pieces) == 4:
            if Position.is_positions_square(white_pieces) or Position.is_positions_straight_line(white_pieces) or Position.is_positions_oblique_line(white_pieces):
                self._winner = self.get_withe_player()
                return True
            
        return False

    def print_winner(self):
        print("Winner is {}".format(self._winner.get_name()))
        
    def play_turn(self, player: Player):
        player.print_player()
        player_piece_color = self.get_player_color(player)
        player_piece = color_to_piece(player_piece_color)
        
        player_movement = player.move()
        player_movement.set_piece_color(player_piece)
        while not player_movement.is_legal_movement(self.board):
            player_movement = player.move()
            player_movement.set_piece_color(player_piece)

        self.board.move_piece(player_movement)

    def play_game(self):
        print("Play game")
        next_player = self.get_black_player()
        while not self.is_game_over():
            self.play_turn(next_player)
            if next_player == self.get_black_player():
                next_player = self.get_withe_player()
            else:
                next_player = self.get_black_player()

            self.board.display()


        self.print_winner()

    def get_black_player(self) -> Player:
        return self.players[TeekoColorEnum.BLACK_COLOR]

    def get_withe_player(self) -> Player:
        return self.players[TeekoColorEnum.WHITE_COLOR]

    def set_black_player(self, player: Player):
        self.set_player(player=player, color=TeekoColorEnum.BLACK_COLOR)

    def set_withe_player(self, player: Player):
        self.set_player(player=player, color=TeekoColorEnum.WHITE_COLOR)

    def set_player(self, player: Player, color:TeekoColorEnum):
        if(color not in self.players.keys()):
            self.players[color] = player
        else:
            print("Player already exist")
        
    def get_player_color(self, player: Player) -> TeekoColorEnum:
        for color, p in self.players.items():
            if p == player:
                return color
        raise Exception("Player not found")

    

