import pygame
import random
import time
import os

pygame.init()

turIMG = [pygame.image.load(os.path.join("imgs", "turretFull.png")), pygame.image.load(os.path.join("imgs", "turretOne.png")), pygame.image.load(os.path.join("imgs", "turretTwo.png")), pygame.image.load(
    os.path.join("imgs", "turretThree.png")), pygame.image.load(os.path.join("imgs", "turretFour.png")), pygame.image.load(os.path.join("imgs", "turretEmpty.png"))]

bgIMG = pygame.image.load(os.path.join("imgs", "bg.png"))
winWidth = bgIMG.get_width()
winHeight = bgIMG.get_height()


def drawWindow(win, ammo):
    win.blit(bgIMG, (0, 0))

    if ammo == 5:
        win.blit(turIMG[0], (400-(turIMG[0].get_width()) + 30, 400))
    elif ammo == 4:
        win.blit(turIMG[1], (400-(turIMG[0].get_width()) + 30, 400))
    elif ammo == 3:
        win.blit(turIMG[2], (400-(turIMG[0].get_width()) + 30, 400))
    elif ammo == 2:
        win.blit(turIMG[3], (400-(turIMG[0].get_width()) + 30, 400))
    elif ammo == 1:
        win.blit(turIMG[4], (400-(turIMG[0].get_width()) + 30, 400))
    elif ammo == 0:
        win.blit(turIMG[5], (400-(turIMG[0].get_width()) + 30, 400))

    pygame.display.update()


class launcher:
    def __init__(self, ammo):
        self.ammo = ammo

    def replenish(self, frame):
        if frame == 210:
            if self.ammo < 5:
                self.ammo += 1


def main():
    win = pygame.display.set_mode((winWidth, winHeight))
    launch = launcher(5)
    clock = pygame.time.Clock()
    frameCount = 0

    run = True
    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if launch.ammo > 0:
                        launch.ammo -= 1

        frameCount += 1
        launch.replenish(frameCount)
        drawWindow(win, launch.ammo)

        if frameCount == 211:
            frameCount = 0


if __name__ == '__main__':
    main()
