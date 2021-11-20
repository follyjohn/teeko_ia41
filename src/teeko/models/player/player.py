from abc import ABC, abstractmethod
from teeko.models.coordinate import Coordinate
import re
from teeko.models.movement import Movement

class Player(ABC):

    @staticmethod
    @abstractmethod
    def _get_player_info() -> str:
        pass

    @abstractmethod
    def __init__(self):
        self._name = self._get_player_info()

    @abstractmethod
    def print_player(self):
        print("player : ", self._name)

    @abstractmethod
    def move(self) -> Movement:
        pass

    def get_name(self):
        return self._name


class HumanPlayer(Player):

    def __init__(self):
        super().__init__()

    @staticmethod
    def _get_player_info() -> str:
        username = input("Enter username : ")
        return str(username)

    def print_player(self):
        super().print_player()

    def get_name(self):
        return super().get_name()

    def move_from_coordinate(self) -> Coordinate:
        raw_coordinate = input(
            "Enter the coordinate of the piece you want to move, eg = x4y2 : ")
        while not (re.fullmatch(r'[x]+[0,1,2,3,4]+[y]+[0,1,2,3,4]', raw_coordinate) or re.fullmatch(r'[x]+[E]+[y]+[E]', raw_coordinate)):
            raw_coordinate = input("Invalid coordinate, please try again : ")

        if raw_coordinate == "xEyE":
            from_coordinate = Coordinate(-1, -1)
        else:
            from_coordinate = Coordinate(
                int(raw_coordinate[1]), int(raw_coordinate[3]))

        return from_coordinate

    def move_to_coordinate(self) -> Coordinate:
        raw_coordinate = input(
            "Enter the coordinate of the piece you want to move to, eg = x4y2 : ")
        while not re.fullmatch(r'[x]+[0,1,2,3,4]+[y]+[0,1,2,3,4]', raw_coordinate):
            raw_coordinate = input("Invalid coordinate, please try again : ")

        from_coordinate = Coordinate(
            int(raw_coordinate[1]), int(raw_coordinate[3]))

        return from_coordinate

    def move(self) -> Movement:
        from_coordinate = self.move_from_coordinate()
        to_coordinate = self.move_to_coordinate()
        return Movement(from_coordinate, to_coordinate)


class MachinePlayer(Player):

    def __init__(self):
        super().__init__()

    @staticmethod
    def _get_player_info() -> str:
        return str("William")

    def print_player(self):
        super().print_player()

    def move(self) -> Movement:
        pass

    def get_name(self):
        return super().get_name()
