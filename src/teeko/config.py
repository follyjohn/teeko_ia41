from enum import Enum

class TeekoConfig(Enum):
    BOARD_DEFAULT_AXIS_SIZE = 5
    BOARD_DEFAULT_ORDINATE_SIZE = 5
    BOARD_DEFAULT_SIZE = 5
    BOARD_DEFAULT_PIECE_COUNT_PER_PLAYER = 4
    
    COORDINATE_REGEX_PATTERN = r'[x]+[0,1,2,3,4]+[y]+[0,1,2,3,4]'
    REGEX_PATTERN = r'[x]+[E]+[y]+[E]'
