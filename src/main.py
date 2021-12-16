
# from teeko.models.game.teeko_no_ui import TeekoNoUI
# import teeko.view.game

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

    # with open('config.ini', 'r') as configfile:
    #     config.read_file(configfile)
    
    
    teeko = TeekoNoUI()
    teeko.play_game()
    # palyer = get_player_by_choice(5)
    # palyer.print_player()   