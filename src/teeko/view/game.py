from os import times
from typing import List
import pygame
import copy
import time
from pygame.draw import circle
from teeko.models.teeko_color import color_to_piece
from teeko.models.teeko_color import get_opponent
from teeko.models.teeko_color import piece_to_color
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
                positions[j][i].set_color(board.get_position_at_coordinate(
                    Coordinate(i, j)).get_piece.value)
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


def blink_positions(neighor_pieces: List[Position], positions: List[TeekooPiece], ecran, color: TeekoColorEnum):
    for ele in neighor_pieces:
        pygame.draw.circle(
            ecran, color.value, (positions[ele.get_abs][ele.get_ord].ord_pos, positions[ele.get_abs][ele.get_ord].abs_pos), 38, 4)
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
neighor_pieces = None
selected_piece = None
drop_pos = None
player_color = TeekoColorEnum.BLACK_COLOR

continuer = True
while continuer:
    if board.is_game_over():
        positions = update_board(ecran, positions, board)
        continuer = False
    ecran.fill((255, 255, 255))
    ecran.blit(backgroung_image, (0, 0))
    positions = update_board(ecran, positions, board)

    event_list = pygame.event.get()

    if neighor_pieces is not None:
        blink_positions(neighor_pieces, positions, ecran, player_color)

    # board.display()

    piece = get_piece_under_mouse(positions)
    if piece != None:
        x, y, _ = piece.to_tuple()
        pygame.draw.circle(ecran, player_color.value, (x, y), 40, 2)
    pygame.display.flip()

    for event in event_list:
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            selected_piece = get_piece_clicked(positions, board)

            if selected_piece != None:
                if selected_piece.get_piece.value != TeekoPieceEnum.EMPTY_PIECE.value and board.get_remaining_pieces_by_color(piece_to_color(selected_piece.get_piece)) > 0:
                    selected_piece = None
                    old_position = None
                    neighor_pieces = None
                elif selected_piece.get_piece == TeekoPieceEnum.EMPTY_PIECE and neighor_pieces is None:
                    mouvement = Movement(
                        Coordinate(-1, -1), selected_piece.get_coordinate(), color_to_piece(player_color))
                    if mouvement.is_legal_movement(board):
                        board.move_piece(mouvement)
                        positions = update_board(ecran, positions, board)
                        player_color = get_opponent(player_color)
                        old_position = copy.deepcopy(selected_piece)
                        selected_piece = None
                else:
                    if neighor_pieces is not None:
                        new_piece = get_piece_clicked(positions, board)
                        if new_piece.get_piece.value == old_position.get_piece.value:
                            selected_piece = None
                            old_position = None
                            neighor_pieces = None
                        else:
                            mouvement = Movement(
                                old_position.get_coordinate(), new_piece.get_coordinate(), color_to_piece(player_color))
                            if mouvement.is_legal_movement(board):
                                board.move_piece(mouvement)
                                positions = update_board(
                                    ecran, positions, board)
                                player_color = get_opponent(player_color)
                                neighor_pieces = None
                                selected_piece = None
                                old_position = None
                    elif player_color == piece_to_color(selected_piece.get_piece):
                        neighor_pieces = board.get_neighbors_empty(
                            selected_piece.get_abs, selected_piece.get_ord)
                        old_position = copy.deepcopy(selected_piece)
                        blink_positions(
                            neighor_pieces, positions, ecran, player_color)
                    else:
                        neighor_pieces = None
                        old_position = None
                        selected_piece = None


if board.is_game_over():
    time.sleep(5)

pygame.quit()
