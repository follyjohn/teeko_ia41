from teeko.models.teeko_color import TeekoColorEnum
from teeko.models.player.nada import Nada
from teeko.models.player.jasmine import Jasmine
from teeko.models.board import Board
from teeko.models.player.alan import Alan
from teeko.models.player.human_player import HumanPlayer
from teeko.models.game.teeko_ui import TeekoUI
from teeko.models.game.teeko_no_ui import TeekoNoUI
from teeko.view.game import gui_play_turn
from teeko.models.player.yaw import Yaw
from teeko.models.game.teeko_no_ui import TeekoNoUI
from teeko.utils.player_utils import get_player_by_choice
import configparser
import argparse

if __name__ == "__main__":
    config = configparser.RawConfigParser()
    parser = argparse.ArgumentParser()
    parser.add_argument("--noui", help="Desable ui", action="store_true")
    args = parser.parse_args()
    if args.noui:
        config.set('DEFAULT', 'Noui', 'yes')
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    else:
        config.set('DEFAULT', 'Noui', 'no')
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    with open('config.ini', 'r') as configfile:
            config.read_file(configfile)
            if config['DEFAULT']['noui'] == 'no':
                teeko = TeekoUI()
            else:
                teeko = TeekoNoUI()
    teeko.play_game()
# palyer = get_player_by_choice(5)
# palyer.print_player()
# ai = Nada()
# ai.set_color(TeekoColorEnum.BLACK_COLOR)
# ai2 = Alan()
# ai2.set_color(TeekoColorEnum.RED_COLOR)
# gui_play_turn(Board(), HumanPlayer(), ai)
