"""
    Metadata: 
        date:      2021-11-21
        purpose:   TeeKo Color type Enum
        
    Description: Enum class for the game. This class is used to represent the different colors of pieces in the game.
"""
from enum import Enum

from teeko.models.teeko_piece import TeekoPieceEnum

class TeekoColorEnum(Enum):
    BLACK_COLOR = "black"
    RED_COLOR = "red"


"""
    color_to_piece: return the piece corresponding to the color
"""
def color_to_piece(color: TeekoColorEnum) -> TeekoPieceEnum:
    if color == TeekoColorEnum.BLACK_COLOR:
        return TeekoPieceEnum.BLACK_PIECE
    elif color == TeekoColorEnum.RED_COLOR:
        return TeekoPieceEnum.RED_PIECE
    else:
        raise ValueError("Color not found")


def get_opponent(color: TeekoColorEnum) -> TeekoColorEnum:
    if color == TeekoColorEnum.BLACK_COLOR:
        return TeekoColorEnum.RED_COLOR
    elif color == TeekoColorEnum.RED_COLOR:
        return TeekoColorEnum.BLACK_COLOR
    else:
        raise ValueError("Color not found")


"""
    piece_to_color_str: return the color corresponding to the piece
"""
def piece_to_color(piece: TeekoPieceEnum) -> TeekoColorEnum:
    if piece == TeekoPieceEnum.BLACK_PIECE:
        return TeekoColorEnum.BLACK_COLOR
    elif piece == TeekoPieceEnum.RED_PIECE:
        return TeekoColorEnum.RED_COLOR
    else:
        raise ValueError("Piece not found")
