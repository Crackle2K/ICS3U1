"""
Author: Dinesh Sinnathamby
Date: May 18th, 2026
Description: Demonstrates the Label sprite with different messages, fonts, sizes, and colours.
"""

import pygame
from newSprites import Label

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Label Sprite Demo")

        self.entities()
        self.init_sprites()
        self.loop()

        pygame.quit()

    def entities(self):
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((20, 20, 60))
        self.screen.blit(self.background, (0, 0))

    def init_sprites(self):
        title = Label("Label Sprite Demo", (320, 80), "arial", 48, (255, 255, 255))
        sub = Label("Pygame is fun!", (320, 180), "courier", 32, (100, 220, 100))
        warning = Label("Watch out!", (320, 280), "impact", 40, (230, 80, 80))
        small = Label("tiny text", (320, 370), "arial", 20, (180, 180, 255))

        self.allSprites = pygame.sprite.Group(title, sub, warning, small)

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
