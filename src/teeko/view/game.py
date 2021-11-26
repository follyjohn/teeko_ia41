import pygame

pygame.init()

ecran = pygame.display.set_mode((720, 740))
image = pygame.image.load("src/teeko/view/teeko_board.png").convert_alpha()
image = pygame.transform.scale(image, (720, 720))
pygame.draw.circle(image, (14, 45, 42), (127, 127), 35)
pygame.draw.circle(image, (14, 45, 42), (242, 127), 35)
pygame.draw.circle(image, (14, 45, 42), (242, 242), 35)
continuer = True

while continuer:
    ecran.fill((255, 255, 255))
    ecran.blit(image, (0, 20))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    pygame.display.flip()

pygame.quit()