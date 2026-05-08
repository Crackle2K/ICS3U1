"""
Author: Dinesh Sinnathamby
Date: May 8th, 2026
Description: Uses pygame.draw functions to create a self-portrait.
"""

import pygame

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Self-Portrait - Dinesh Sinnathamby")
        self.entities()
        self.draw_portrait()
        self.clock = pygame.time.Clock()
        self.loop()
        pygame.quit()

    def entities(self):
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((135, 185, 230))

    def loop(self):
        keepGoing = True
        while keepGoing:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()

    def draw_portrait(self):
        SKIN = (210, 165, 120)
        DARK_BROWN = (50, 28, 8)
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        SHIRT_BLUE = (20, 65, 145)
        
        pygame.draw.rect(self.background, SHIRT_BLUE, (185, 370, 270, 110))
        pygame.draw.rect(self.background, SKIN, (295, 320, 50, 55))
        pygame.draw.circle(self.background, SKIN, (320, 240), 100)
        pygame.draw.ellipse(self.background, DARK_BROWN, (220, 130, 200, 130))
        pygame.draw.circle(self.background, WHITE, (285, 220), 18)
        pygame.draw.circle(self.background, WHITE, (355, 220), 18)
        pygame.draw.circle(self.background, BLACK, (285, 220), 8)
        pygame.draw.circle(self.background, BLACK, (355, 220), 8)
        pygame.draw.arc(self.background, BLACK, (285, 265, 70, 35), 3.14, 2 * 3.14, 3)

Main()
