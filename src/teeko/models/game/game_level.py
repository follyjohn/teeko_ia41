from enum import Enum

class GameLevel(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    IMPOSSIBLE = 4

if __name__ == "__main__":
    levels = [GameLevel.EASY, GameLevel.MEDIUM, GameLevel.HARD, GameLevel.IMPOSSIBLE]
    for level in levels:
        print("{}. for level {}".format(level.value, level._name_))