from typing import List, Optional
from .teeko_color import TeekoColorEnum
from .position import Position
from models.Nada import Nada
from models.Alan import Alan
from core.player import Player
from core.human_player import HumanPlayer
from board import Board


class Teeko:
    def __init__(self):
        self.players = {}
        self._winner: Player = None
        self._introduce_game()
        self._initialise_player()
        self._initilise_board()

    def _introduce_game(self):
        print("Welcome to Teeko\n")

    def _initialise_player(self):
        print("Setting up players\n")
        print("Set up player a")
        self.players = {}
        player_a = Nada()
        print()
        print("Set up player b")
        player_b = HumanPlayer()
        while player_a.get_name == player_b.get_name:
            print("Oops, player a and player b cannot have the same name. Please try again")
            player_b = Alan()
        print()
        self.set_black_player(player_a)
        self.set_red_player(player_b)
        print("Awsome! Players are set up")
        print("The game will start with player a\n")

    def _initilise_board(self):
        print("The game board is set up")
        print("The board is empty\n")
        self.board = Board()
        self.board.display()

    def is_game_over(self) -> bool:
        black_pieces = self.board.get_positions_by_color(TeekoColorEnum.BLACK_COLOR)
        red_pieces = self.board.get_positions_by_color(TeekoColorEnum.RED_COLOR)

        if len(black_pieces) == 4:
            if Position.position_is_winning_position(black_pieces):
                self._winner = self.get_black_player()
                print("Game over!")
                return True

        if len(red_pieces) == 4:
            if Position.position_is_winning_position(red_pieces):
                self._winner = self.get_red_player()
                print("Game over!")
                return True

        return False

    def print_winner(self):
        print("Winner is {}".format(self._winner.get_name()))

    def play_turn(self, player: Player):
        print("Your turn player : " + player.get_name())
        player_piece_color = self.get_player_color(player)

        player_movement = player.move(self.board, player_piece_color)
        while not player_movement.is_legal_movement(self.board):
            player_movement = player.move(self.board, player_piece_color)

        self.board.move_piece(player_movement)

    def play_game(self):
        if not len(self.players) == 2:
            print("Players are not set up\n")
            self._initialise_player()
        print("Let's play Teeko\n")
        next_player = self.get_black_player()
        while not self.is_game_over():
            self.play_turn(next_player)
            if next_player == self.get_black_player():
                next_player = self.get_red_player()
            else:
                next_player = self.get_black_player()

            self.board.display()
        self.print_winner()

    def get_players(self) -> List[Player]:
        return list(self.players.values())

    def get_black_player(self) -> Player:
        return self.players[TeekoColorEnum.BLACK_COLOR]

    def get_red_player(self) -> Player:
        return self.players[TeekoColorEnum.RED_COLOR]

    def set_black_player(self, player: Player):
        self.set_player(player=player, color=TeekoColorEnum.BLACK_COLOR)

    def set_red_player(self, player: Player):
        self.set_player(player=player, color=TeekoColorEnum.RED_COLOR)

    def set_player(self, player: Player, color: TeekoColorEnum):
        if color not in self.players.keys():
            if len(self.players) == 2:
                print("Players are already set up\n")
                return
            if len(self.players) == 1:
                if player._name == self.get_players()[0].get_name():
                    print("Player is already set up with the same name\n")
                    return
            self.players[color] = player
        else:
            print("Player already exist\n")

    def get_player_color(self, player: Player) -> Optional[TeekoColorEnum]:
        for color, p in self.players.items():
            if p == player:
                return color
        print("Player not found\n")
        return None
