"""
Author: Dinesh Sinnathamby
Date: May 18th, 2026
Description: Demonstrates the Cherry sprite at a random location on the screen.
"""

import pygame
from myPacmanSprites import Cherry

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Cherry Demo")
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
        cherry = Cherry(boundary)
        self.allSprites = pygame.sprite.Group(cherry)

    def loop(self):
        clock = pygame.time.Clock()
        keepGoing = True
        while keepGoing:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
            self.allSprites.clear(self.screen, self.background)
            self.allSprites.update()
            self.allSprites.draw(self.screen)
            pygame.display.flip()

Main()
