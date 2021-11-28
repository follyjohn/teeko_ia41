import pygame

pygame.init()
pygame.display.set_caption("Teeko")
ecran = pygame.display.set_mode((720, 740))

image = pygame.image.load("src/teeko/view/teeko_board.png").convert_alpha()
image = pygame.transform.scale(image, (720, 720))


def get_square_under_mouse(board): # gest mouse position #TODO
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) - (70,70)
    x, y = [int(v // 70) for v in mouse_pos]
    try:
        if x >= 0 and y >= 0:
            return (board[y][x], x, y)
    except IndexError:
        pass
    return None, None, None

# pygame.draw.circle(image, (0, 0, 0), (127, 127), 35)
# pygame.draw.circle(image, (0, 0, 0), (242, 127), 35)
# pygame.draw.circle(image, (0, 0, 0), (242, 243), 35)
# pygame.draw.circle(image, (0, 0, 0), (357, 358), 35)

# pygame.draw.circle(image, (255,0,0), (472, 358), 35)
# pygame.draw.circle(image, (255,0,0), (472, 243), 35)
# pygame.draw.circle(image, (255,0,0), (472, 473), 35)
# pygame.draw.circle(image, (255,0,0), (357, 473), 35)

x = 127
y = 127
for i in range(5):
    for j in range(5):
        pygame.draw.circle(image, (255, 0, 0), (x,y), 35)
        x+=115
    if i == 1:
        y+=2
    x = 127
    y+=115

continuer = True


while continuer:
    ecran.fill((255, 255, 255))
    ecran.blit(image, (0, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
    pygame.display.flip()

pygame.quit()
