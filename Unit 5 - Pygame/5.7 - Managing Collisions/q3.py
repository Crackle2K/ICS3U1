"""
Author: Dinesh Sinnathamby
Date: May 18th, 2026
Description: Demonstrates the Pacman sprite. Use the arrow keys to move Pacman. Pacman wraps around to the opposite side when it exits the screen.
"""

import pygame
from myPacmanSprites import Pacman

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Pacman Demo")
        self.entities()
        self.init_sprites()
        self.loop()
        pygame.quit()

    def entities(self):
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))

    def init_sprites(self):
        boundary = self.screen.get_size()
        self.pacman = Pacman(boundary)
        self.allSprites = pygame.sprite.Group(self.pacman)

    def loop(self):
        clock = pygame.time.Clock()
        keepGoing = True
        while keepGoing:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.pacman.go_right()
                    elif event.key == pygame.K_LEFT:
                        self.pacman.go_left()
                    elif event.key == pygame.K_UP:
                        self.pacman.go_up()
                    elif event.key == pygame.K_DOWN:
                        self.pacman.go_down()
            self.allSprites.clear(self.screen, self.background)
            self.allSprites.update()
            self.allSprites.draw(self.screen)
            pygame.display.flip()

Main()
