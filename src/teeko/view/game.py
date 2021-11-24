import pygame


def main():
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
        screen.fill(pygame.Color('grey'))
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
