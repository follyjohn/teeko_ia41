"""
    Metadata:
        author:    follyjohn
        date:      2021-11-21
        purpose:   Teeko Piece category

    Description: Enum class for the game.
        This class is used to represent the different categories of pieces in the game.
"""
from enum import Enum


class TeekoPieceEnum(Enum):
    BLACK_PIECE = "a"  # Black piece for the player a
    RED_PIECE = "b"  # Red piece for the player b
    EMPTY_PIECE = " "  # Empty piece for the empty emplacement of the board
