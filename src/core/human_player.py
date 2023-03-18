import re
from .teeko_color import color_to_piece
from .teeko_color import TeekoColorEnum
from .board import Board
from .coordinate import Coordinate
from .movement import Movement
from core.player import Player


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    @staticmethod
    def _get_player_info() -> str:
        """This fuunction is use to ask the user for the name of the player

        Returns:str -- The name of the player as string
        """
        username = input("Enter username : ")
        while not re.fullmatch(r"[a-zA-Z0-9]+", username):
            username = input("Invalid username, please try again : ")
        return str(username)

    def print_player(self):
        super().print_player()

    def get_name(self):
        return super().get_name()

    def move_from_coordinate(self) -> Coordinate:
        """move_from_coordinate(self) -> Coordinate
        This function is used to ask the user for the coordinate of the piece he wants to move.
        There is two cases :
            - The user wants to move a new piece between available pieces to the board.
                In this case the coorddinate shoud be xEyE. The value of the generated coordinate will be -1,-1
            - The user wants to move an existing piece on the board.
                In this case the coordinate should be between x0y0 and x4y4.
                0 to 4 beacause the board is 5x5. The value of the generated coordinate will be between 0 and 4.
        Returns: Coordinate -- The coordinate of the piece he wants to move
        """

        raw_coordinate = input("Enter the coordinate of the piece you want to move, eg = xEyE : ")
        # We verify that the coordinate is valid with the regex
        while not (
            re.fullmatch(r"[x]+[0,1,2,3,4]+[y]+[0,1,2,3,4]", raw_coordinate)
            or re.fullmatch(r"[x]+[E]+[y]+[E]", raw_coordinate)
        ):
            raw_coordinate = input("Invalid coordinate, please try again : ")

        if raw_coordinate == "xEyE":
            # We return a coordinate with the value -1,-1 because in teeko piece can't be removed from the board.
            from_coordinate = Coordinate(-1, -1)
        else:
            from_coordinate = Coordinate(
                # We return a coordinate with the value of the coordinate. eg = x4y2 -> 4,2
                int(raw_coordinate[1]),
                int(raw_coordinate[3]),
            )

        return from_coordinate

    def move_to_coordinate(self) -> Coordinate:
        """move_from_coordinate(self) -> Coordinate
        This function is used to ask the user for the coordinate of the piece he wants to move.
        In this case the coordinate should be between x0y0 and x4y4.
        The coordinate in this cas can't be -1,-1 because in teeko piece can't be removed from the board.
        """
        raw_coordinate = input("Enter the coordinate you want to move the piece to, eg = x4y2 : ")
        while not re.fullmatch(r"[x]+[0,1,2,3,4]+[y]+[0,1,2,3,4]", raw_coordinate):
            raw_coordinate = input("Invalid coordinate, please try again : ")

        from_coordinate = Coordinate(int(raw_coordinate[1]), int(raw_coordinate[3]))

        return from_coordinate

    def move(self, board: Board, color: TeekoColorEnum) -> Movement:
        """move(self, board: Board) -> Movement
        We ask the user for the coordinate of the piece he wants to move.
        And then ask the user for the coordinate of the piece he wants to move to.
        """
        from_coordinate = self.move_from_coordinate()
        to_coordinate = self.move_to_coordinate()
        print()
        return Movement(from_coordinate, to_coordinate, color_to_piece(color))
