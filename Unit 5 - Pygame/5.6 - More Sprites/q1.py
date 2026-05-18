"""
Author: Dinesh Sinnathamby
Date: May 18th, 2026
Description: Demonstrates the Circle sprite with four different colours.
"""

import pygame
from newSprites import Circle

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Circle Sprite Demo")

        self.entities()
        self.init_sprites()
        self.loop()

        pygame.quit()

    def entities(self):
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((30, 30, 30))
        self.screen.blit(self.background, (0, 0))

    def init_sprites(self):
        red = Circle((220, 50, 50))
        green = Circle((50, 200, 50))
        blue = Circle((50, 100, 220))
        yellow = Circle((230, 210, 50))

        red.rect.center = (160, 120)
        green.rect.center = (480, 120)
        blue.rect.center = (160, 360)
        yellow.rect.center = (480, 360)

        self.allSprites = pygame.sprite.Group(red, green, blue, yellow)

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
