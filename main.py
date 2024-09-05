import pygame, sys
pygame.init()
screen = pygame.display.set_mode((480,800))
pygame.display.set_caption('mcat.aamc.org')
pygame.displaycolor(255,255,255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()