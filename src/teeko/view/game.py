from typing import List
import pygame
from pygame.draw import circle
from teeko.models.movement import Movement
from teeko.models.teeko_color import TeekoColorEnum
from teeko.models.coordinate import Coordinate

from teeko.models.board import Board
from teeko.models.position import Position
from teeko.models.teeko_piece import TeekoPieceEnum


TEEKO_BOARD_WIDTH = 720
TEEKO_BOARD_HEIGHT = 720
TEEKO_PIECE_CENTER_AXIS_ORIRGIN = 120
TEEKO_PIECE_CENTER_AXIS_DISTANCE = 120
TEEKO_PIECE_CENTER_ORDINATE_ORIRGIN = 120
TEEKO_PIECE_CENTER_ORDINATE_DISTANCE = 120
TEEKO_BOARD_SIZE = 5


class TeekooPiece:
    def __init__(self, abs_pos, ord_pos, color: TeekoPieceEnum):
        self._abs_pos = abs_pos
        self._ord_pos = ord_pos
        self._color: TeekoPieceEnum = color

    def __init__(self, abs_pos, ord_pos):
        self._abs_pos = abs_pos
        self._ord_pos = ord_pos
        self._color: TeekoPieceEnum = TeekoPieceEnum.EMPTY_PIECE

    def to_tuple(self):
        return self._abs_pos, self._ord_pos, self.color

    @property
    def abs_pos(self):
        return self._abs_pos

    @property
    def ord_pos(self):
        return self._ord_pos

    @property
    def color(self):
        if self._color == TeekoPieceEnum.EMPTY_PIECE:
            return None
        return self._color

    def set_color(self, color: TeekoColorEnum):
        self._color = color


def generate_pieces():
    pieces = []
    x = TEEKO_PIECE_CENTER_AXIS_ORIRGIN
    y = TEEKO_PIECE_CENTER_ORDINATE_ORIRGIN
    for i in range(TEEKO_BOARD_SIZE):
        pieces.append([])
        for j in range(TEEKO_BOARD_SIZE):
            pieces[i].append(TeekooPiece(x, y))
            x += TEEKO_PIECE_CENTER_AXIS_DISTANCE
        x = TEEKO_PIECE_CENTER_AXIS_ORIRGIN
        y += TEEKO_PIECE_CENTER_ORDINATE_DISTANCE

    return pieces


def create_board_surf():  # create board surface with image background
    teeko_board = pygame.image.load(
        "./src/teeko/view/1x/Artboard 1.png").convert_alpha()
    teeko_board = pygame.transform.scale(
        teeko_board, (TEEKO_BOARD_WIDTH, TEEKO_BOARD_HEIGHT))
    return teeko_board


def update_board(surface, positions, board: Board):
    for i in range(TEEKO_BOARD_SIZE):
        for j in range(TEEKO_BOARD_SIZE):
            try:
                positions[j][i].set_color(board.get_position_at_coordinate(Coordinate(i, j)).get_piece.value)
                if positions[j][i].color == TeekoPieceEnum.BLACK_PIECE.value:
                    pygame.draw.circle(
                        surface, 'black', (positions[j][i].abs_pos, positions[j][i].ord_pos), 40)
                elif positions[j][i].color == TeekoPieceEnum.RED_PIECE.value:
                    pygame.draw.circle(
                        surface, 'red', (positions[j][i].abs_pos, positions[j][i].ord_pos), 40)
            except IndexError:
                pass

    return positions


def get_piece_under_mouse(positions: List[TeekooPiece]):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    x, y = [int(v) for v in mouse_pos]
    try:
        if x >= 0 and y >= 0:
            for i in range(TEEKO_BOARD_SIZE):
                for j in range(TEEKO_BOARD_SIZE):
                    if x <= positions[j][i].abs_pos + 30 and x >= positions[j][i].abs_pos-30 and y <= positions[j][i].ord_pos + 30 and y >= positions[j][i].ord_pos - 30:
                        if positions[j][i].color is not None:
                            return positions[j][i]
    except IndexError:
        pass
    return None


def get_piece_clicked(positions: List[TeekooPiece], board: Board):
    board.display()
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    x, y = [int(v) for v in mouse_pos]
    if x:
        try:
            if x >= 0 and y >= 0:
                for i in range(TEEKO_BOARD_SIZE):
                    for j in range(TEEKO_BOARD_SIZE):
                        if x <= positions[j][i].abs_pos + 30 and x >= positions[j][i].abs_pos-30 and y <= positions[j][i].ord_pos + 30 and y >= positions[j][i].ord_pos - 30:
                            return board.get_position_at_coordinate(Coordinate(i, j))
        except IndexError:
            pass
        return None

# pygame.draw.circle(image, (0, 0, 0), (127, 127), 35)
# pygame.draw.circle(image, (0, 0, 0), (242, 127), 35)
# pygame.draw.circle(image, (0, 0, 0), (242, 243), 35)
# pygame.draw.circle(image, (0, 0, 0), (357, 358), 35)

# pygame.draw.circle(image, (255,0,0), (472, 358), 35)
# pygame.draw.circle(image, (255,0,0), (472, 243), 35)
# pygame.draw.circle(image, (255,0,0), (472, 473), 35)
# pygame.draw.circle(image, (255,0,0), (357, 473), 35)


"""def on click on circle:
      if circle is empty: add nez piece and drow it
      else show arrow to move piece
"""

pygame.init()
pygame.display.set_caption("Teeko")
ecran = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()

board = Board()
positions = generate_pieces()

backgroung_image = create_board_surf()


selected_piece = None
drop_pos = None

continuer = True
while continuer:
    ecran.fill((255, 255, 255))
    ecran.blit(backgroung_image, (0, 0))
    positions =  update_board(ecran, positions, board)
    event_list = pygame.event.get()

    # board.display()

    piece = get_piece_under_mouse(positions)
    if piece != None:
        x,y, _ = piece.to_tuple()
        pygame.draw.circle(ecran, 'red', (x, y), 40, 2)
    pygame.display.flip()


    for event in event_list:
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            selected_piece = get_piece_clicked(positions, board)
            if selected_piece != None:
                if selected_piece.get_piece == TeekoPieceEnum.EMPTY_PIECE:
                    board.move_piece(Movement(Coordinate(-1,-1), selected_piece.get_coordinate(), TeekoPieceEnum.RED_PIECE))
        # if event.type == pygame.MOUSEBUTTONUP:
        #     if drop_pos:
        #         piece, old_x, old_y = selected_piece
        #         board[old_y][old_x] = (
        #             board[old_y][old_x][0], board[old_y][old_x][1], None)
        #         new_x, new_y = drop_pos
        #         board[new_y][new_x] = (
        #             board[new_y][new_x][0], board[new_y][new_x][1], TeekoPieceEnum.BLACK_PIECE)
        #     selected_piece = None
        #     drop_pos = None
    

pygame.quit()
