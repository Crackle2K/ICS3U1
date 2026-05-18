"""
Author: Dinesh Sinnathamby
Date: May 18th, 2026
Description: Extends q4 with a chomp sound effect each time Pacman eats a Cherry.
"""

import pygame
from myPacmanSprites import Cherry, Pacman

class Main:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Pacman")
        self.chomp = pygame.mixer.Sound("Unit 5 - Pygame/5.7 - Managing Collisions/sound/chomp.wav")
        self.chomp.set_volume(0.8)
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
        cherries = [Cherry(boundary) for _ in range(10)]
        self.cherries = pygame.sprite.Group(*cherries)
        self.pacman = Pacman(boundary, self.cherries, self.chomp)
        self.allSprites = pygame.sprite.Group(self.pacman, *cherries)

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
