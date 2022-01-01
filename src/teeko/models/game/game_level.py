from enum import Enum

class GameLevel(Enum):
    EASY = 2
    MEDIUM = 3
    HARD = 4
    IMPOSSIBLE = 5

if __name__ == "__main__":
    levels = [GameLevel.EASY, GameLevel.MEDIUM, GameLevel.HARD, GameLevel.IMPOSSIBLE]
    for level in levels:
        print("{}. for level {}".format(level.value, level._name_))