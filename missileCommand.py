import pygame
import random
import time
import os

pygame.init()

bgIMG = pygame.image.load(os.path.join("imgs", "bg.png"))
winWidth = bgIMG.get_width()
winHeight = bgIMG.get_height()


def drawWindow(win):
    win.blit(bgIMG, (0, 0))

    pygame.display.update()


def main():
    win = pygame.display.set_mode((winWidth, winHeight))
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        drawWindow(win)


if __name__ == '__main__':
    main()
