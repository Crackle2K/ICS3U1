"""
Author: Dinesh Sinnathamby
Date: May 18th, 2026
Description: Spawns 25 Brick sprites that each start at a random position and move in a random diagonal direction, bouncing off all four edges.
"""

import pygame
from newSprites import Brick

NUM_BRICKS = 25


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Brick Sprite Demo")

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
        bricks = [Brick(boundary) for _ in range(NUM_BRICKS)]
        self.allSprites = pygame.sprite.Group(*bricks)

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
