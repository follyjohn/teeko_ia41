from enum import Enum
from typing import Any, Dict, List, Optional
from teeko.utils.player_utils import get_player_by_choice
from teeko.models.game.teeko import TeekoGame
from teeko.models.player.jasmine import Jasmine
from teeko.models.player.nada import Nada
from teeko.models.player.justine import Justine
from teeko.models.player.yaw import Yaw
from teeko.view.game import gui_play_turn
from teeko.models.board import Board
from teeko.models.player.alan import Alan
from teeko.models.player.human_player import HumanPlayer
from teeko.models.player.player import Player
from teeko.models.position import Position
from teeko.models.teeko_color import TeekoColorEnum, color_to_piece
from teeko.models.teeko_piece import TeekoPieceEnum


class TeekoNoUI(TeekoGame):
    def __init__(self):
        super().__init__()

    def _introduce_game(self):
        print("Welcome to Teeko\n")

    def _select_game_mode(self):
        print("Select game mode\n")
        print("1. Human vs Human")
        print("2. Human vs Computer")
        print("3. Computer vs Human")
        print("4. Computer vs Computer")
        print("5. Quit")
        print()
        game_mode = input("Enter game mode: ")
        while not game_mode.isdigit() or int(game_mode) < 1 or int(
                game_mode) > 5:
            print("Invalid game mode")
            game_mode = input("Enter game mode: ")

        if int(game_mode) == 5:
            print("Quitting game")
            exit()
        else:
            self.set_mode(int(game_mode))

    def _initialise_player(self):
        print("Setting up players\n")
        print("Set up player a")
        if self.get_mode() == 1 or self.get_mode() == 2:
            player_a = HumanPlayer("Player A")

        else:
            print("Select an IA for player a")
            print("1. Nada")
            print("2. Jasmine")
            print("3. Justine")
            print("4. Yaw")
            print("5. Alan")
            print("6. Quit")
            print()
            player_a_choice = input("Enter player a choice: ")
            while not player_a_choice.isdigit() or int(
                    player_a_choice) < 1 or int(player_a_choice) > 6:
                print("Invalid choice")
                player_a_choice = input("Enter player a choice: ")

            if int(player_a_choice) == 6:
                print("Quitting game")
                exit()
            else:
                player_a = get_player_by_choice(int(player_a_choice), "Player A")
                if player_a.has_level() == True:
                    for level in player_a.get_levels():
                        print("{}. for level {}".format(
                            level.value, level._name_))
                    selected_level = int(input("Enter level: "))
                    while not selected_level in [
                            l.value for l in player_a.get_levels()
                    ]:
                        print("Invalid level")
                        selected_level = int(input("Enter level: "))
                    player_a.set_level(selected_level)

        print("Set up player b")
        if self.get_mode() == 1 or self.get_mode() == 3:
            player_b = HumanPlayer("Player B")
        else:
            print("Select an IA for player b")
            print("1. Nada")
            print("2. Jasmine")
            print("3. Justine")
            print("4. Yaw")
            print("5. Alan")
            print("6. Quit")
            print()
            player_b_choice = input("Enter player b choice: ")
            while not player_b_choice.isdigit() or int(
                    player_b_choice) < 1 or int(player_b_choice) > 6:
                print("Invalid choice")
                player_b_choice = input("Enter player b choice: ")

            if int(player_b_choice) == 6:
                print("Quitting game")
                exit()
            else:
                player_b = get_player_by_choice(int(player_b_choice), "Player B")
                if player_b.has_level() == True:
                    for level in player_b.get_levels():
                        print("{}. for level {}".format(
                            level.value, level._name_))
                    selected_level = int(input("Enter level: "))
                    while not selected_level in [
                            l.value for l in player_b.get_levels()
                    ]:
                        print("Invalid level")
                        selected_level = int(input("Enter level: "))
                    player_b.set_level(selected_level)

        player_a.set_color(TeekoColorEnum.BLACK_COLOR)
        player_b.set_color(TeekoColorEnum.RED_COLOR)

        # print()
        # print("Set up player b")
        # # player_b = Jasmine()
        # while player_a.get_name == player_b.get_name:
        #     print(
        #         "Oops, player a and player b cannot have the same name. Please try again")
        #     player_b = Alan()
        # print()
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
        black_pieces = self.board.get_positions_by_color(
            TeekoColorEnum.BLACK_COLOR)
        red_pieces = self.board.get_positions_by_color(
            TeekoColorEnum.RED_COLOR)

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
        print("Player {} moved {}".format(player.get_name(), player_movement))
        self.board.display()

    def play_game(self):
        gui_play_turn(self.board, self.get_black_player(), self.get_red_player())
        # if not len(self.players) == 2:
        #     print("Players are not set up\n")
        #     self._initialise_player()
        # print("Let's play Teeko\n")
        # next_player = self.get_black_player()
        # while not self.is_game_over():
        #     self.play_turn(next_player)
        #     if next_player == self.get_black_player():
        #         next_player = self.get_red_player()
        #     else:
        #         next_player = self.get_black_player()

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
        if (color not in self.players.keys()):
            if len(self.players) == 2:
                print("Players are already set up\n")
                self.players = {}
                self._initialise_player()
            if len(self.players) == 1:
                if player._name == self.get_players()[0].get_name():
                    print("Player is already set up with the same name\n")
                    self.players = {}
                    self._initialise_player()
            self.players[color] = player
        else:
            print("Player already exist\n")

    def get_player_color(self, player: Player) -> Optional[TeekoColorEnum]:
        for color, p in self.players.items():
            if p == player:
                return color
        print("Player not found\n")
        return None
