import pygame
from pygame.draw import circle
from teeko.models.coordinate import Coordinate

from teeko.models.board import Board
from teeko.models.position import Position
from teeko.models.teeko_piece import TeekoPieceEnum

board = Board()


pygame.init()
pygame.display.set_caption("Teeko")
ecran = pygame.display.set_mode((720, 740))

image = pygame.image.load("./teeko/view/teeko_board.png").convert_alpha()
image = pygame.transform.scale(image, (720, 720))

# pygame.draw.circle(image, (0, 0, 0), (127, 127), 35)
# pygame.draw.circle(image, (0, 0, 0), (242, 127), 35)
# pygame.draw.circle(image, (0, 0, 0), (242, 243), 35)
# pygame.draw.circle(image, (0, 0, 0), (357, 358), 35)

# pygame.draw.circle(image, (255,0,0), (472, 358), 35)
# pygame.draw.circle(image, (255,0,0), (472, 243), 35)
# pygame.draw.circle(image, (255,0,0), (472, 473), 35)
# pygame.draw.circle(image, (255,0,0), (357, 473), 35)

positions = []
x = 127
y = 147
for i in range(5):
    positions.append([])
    for j in range(5):
        positions[i].append((x, y, None))
        if board.get_piece_at_coordinate(Coordinate(i, j)) == TeekoPieceEnum.BLACK_PIECE:
            pygame.draw.circle(image, (255, 255, 255), (x, y), 35)
        x += 115
    if i == 1:
        y += 2
    x = 127
    y += 115

print(positions)


def get_square_under_mouse(board):  # gest mouse position #TODO
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())

    x, y = [int(v) for v in mouse_pos]
    print(x, y)
    try:
        if x >= 0 and y >= 0:
            for i in range(5):
                for j in range(5):
                    if x <= board[i][j][0]+30 and x >= board[i][j][0]-30 and y <= board[i][j][1]+30 and y >= board[i][j][1]-30:
                        print(board[i][j])
                        return board[i][j]
    except IndexError:
        pass
    return None, None, None


def update(event_list, board):
    for event in event_list:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
            x, y = [int(v) for v in mouse_pos]
            if x:
                try:
                    if x >= 0 and y >= 0:
                        for i in range(5):
                            for j in range(5):
                                if x <= board[i][j][0]+30 and x >= board[i][j][0]-30 and y <= board[i][j][1]+30 and y >= board[i][j][1]-30:
                                    t,m,_ = board[i][j]
                                    pygame.draw.circle(image, (255, 0, 0), (t,m-20), 40)
                                    
                except IndexError:
                    pass


continuer = True

"""def on click on circle:
      if circle is empty: add nez piece and drow it
      else show arrow to move piece
"""

while continuer:
    ecran.fill((255, 255, 255))
    ecran.blit(image, (0, 20))
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            continuer = False
    
    x, y, piece = get_square_under_mouse(positions)
    update(event_list, positions)
    if x != None:
        pygame.draw.circle(ecran, (255, 0, 0), (x, y), 40, 2)
    pygame.display.flip()


pygame.quit()
