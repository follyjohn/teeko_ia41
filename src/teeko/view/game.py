import pygame

pygame.init()

ecran = pygame.display.set_mode((700, 700))
image = pygame.image.load("src/teeko/view/teeko_board.png").convert_alpha()

continuer = True

while continuer:
    ecran.fill((255, 255, 255))
    ecran.blit(image, (0, 50))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    pygame.display.flip()

pygame.quit()