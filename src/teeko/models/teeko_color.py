from enum import Enum

from teeko.models.teeko_piece import TeekoPieceEnum

class TeekoColorEnum(Enum):
    BLACK_COLOR = "black"
    RED_COLOR = "red"


def color_to_piece(color: TeekoColorEnum) -> TeekoPieceEnum:
    if color == TeekoColorEnum.BLACK_COLOR:
        return TeekoPieceEnum.BLACK_PIECE
    elif color == TeekoColorEnum.RED_COLOR:
        return TeekoPieceEnum.RED_PIECE
    else:
        raise Exception("Color not found")

def piece_to_color(piece: TeekoPieceEnum) -> TeekoColorEnum:
    if piece == TeekoPieceEnum.BLACK_PIECE:
        return TeekoColorEnum.BLACK_COLOR
    elif piece == TeekoPieceEnum.RED_PIECE:
        return TeekoColorEnum.RED_COLOR
    else:
        raise Exception("Piece not found")
