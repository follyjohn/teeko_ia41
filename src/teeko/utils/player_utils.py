from teeko.models.player.Nada import Nada
from teeko.models.player.Jasmine import Jasmine
from teeko.models.player.Yaw import Yaw
from teeko.models.player.Alan import Alan
from teeko.models.player.Justine import Justine
from teeko.models.player.player import Player
def get_player_by_choice(choice: int) -> Player:
    if choice == 1:
        return Nada()   
    elif choice == 2:
        return Jasmine()
    elif choice == 3:
        return Justine()
    elif choice == 4:
        return Yaw()
    elif choice == 5:
        return Alan()