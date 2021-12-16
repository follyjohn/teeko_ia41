from teeko.utils_functions import naturalise
from teeko.models.teeko_color import TeekoColorEnum
from teeko.models.movement import Movement
from teeko.models.board import Board
from teeko.models.player.ai_player import AIPlayer
import re
import configparser
import random


class Alan(AIPlayer):

    @staticmethod
    def _get_player_info() -> str:
        default_name = "Alan"
        config = configparser.RawConfigParser()
        with open('config.ini', 'r') as configfile:
            config.read_file(configfile)
            if config['DEFAULT']['noui'] == 'no':
                return default_name
            else:
                awnser = input(
                    "Do you want to change the name of the ai ? (y/n), q to quit: ")
                while awnser != "y" and awnser != "n" and awnser != "q":
                    awnser = input(
                        "Do you want to change the name of the ai ? (y/n), q to quit: ")
                if awnser == "y":
                    name = input("Enter the name of the ai : ")
                    while not re.fullmatch(r'[a-zA-Z0-9]+', name):
                        name = input(
                            "Invalid name,use only letters and numbers, please try again : ")
                    return str(name)
                elif awnser == "q":
                    print("Quitting")
                    exit()
                elif awnser == "n":
                    return default_name

    def move(self, board: Board, color: TeekoColorEnum) -> Movement:
        movements = self.generate_next_movements(board, color)
        mouvement = random.choice(movements)
        return mouvement
