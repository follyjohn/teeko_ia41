from enum import Enum

from teeko.models.teeko_piece import TeekoPieceEnum

class TeekoColorEnum(Enum):
    WHITE_COLOR = "white"
    BLACK_COLOR = "black"


def color_to_piece(color: TeekoColorEnum) -> TeekoPieceEnum:
    if color == TeekoColorEnum.BLACK_COLOR:
        return TeekoPieceEnum.BLACK_PIECE
    elif color == TeekoColorEnum.WHITE_COLOR:
        return TeekoPieceEnum.WHITE_PIECE
    else:
        raise Exception("Color not found")

def piece_to_color(piece: TeekoPieceEnum) -> TeekoColorEnum:
    if piece == TeekoPieceEnum.BLACK_PIECE:
        return TeekoColorEnum.BLACK_COLOR
    elif piece == TeekoPieceEnum.WHITE_PIECE:
        return TeekoColorEnum.WHITE_COLOR
    else:
        raise Exception("Piece not found")
