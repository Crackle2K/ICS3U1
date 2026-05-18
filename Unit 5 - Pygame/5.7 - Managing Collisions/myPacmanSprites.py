"""
Author: Dinesh Sinnathamby
Date: May 18th, 2026
Description: Sprite module for the Pacman game. Contains the Cherry and Pacman classes.
"""

import random
import pygame

class Cherry(pygame.sprite.Sprite):
    def __init__(self, boundary):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Unit 5 - Pygame/5.7 - Managing Collisions/img/cherry.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, boundary[0]), random.randint(0, boundary[1]))

class Pacman(pygame.sprite.Sprite):
    def __init__(self, boundary, cherries=None, chomp=None):
        pygame.sprite.Sprite.__init__(self)
        self.__images = {
            "right": pygame.image.load("Unit 5 - Pygame/5.7 - Managing Collisions/img/right.png"),
            "left": pygame.image.load("Unit 5 - Pygame/5.7 - Managing Collisions/img/left.png"),
            "up": pygame.image.load("Unit 5 - Pygame/5.7 - Managing Collisions/img/up.png"),
            "down": pygame.image.load("Unit 5 - Pygame/5.7 - Managing Collisions/img/down.png"),
        }
        self.image = self.__images["right"]
        self.rect = self.image.get_rect()
        self.rect.center = (boundary[0] // 2, boundary[1] // 2)
        self.dx = 0
        self.dy = 0
        self.__boundary_x = boundary[0]
        self.__boundary_y = boundary[1]
        self.__cherries = cherries
        self.__chomp = chomp

    def go_right(self):
        self.dx = 5
        self.dy = 0
        self.image = self.__images["right"]

    def go_left(self):
        self.dx = -5
        self.dy = 0
        self.image = self.__images["left"]

    def go_up(self):
        self.dx = 0
        self.dy = -5
        self.image = self.__images["up"]

    def go_down(self):
        self.dx = 0
        self.dy = 5
        self.image = self.__images["down"]

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy

        if self.rect.right < 0:
            self.rect.left = self.__boundary_x
        elif self.rect.left > self.__boundary_x:
            self.rect.right = 0

        if self.rect.bottom < 0:
            self.rect.top = self.__boundary_y
        elif self.rect.top > self.__boundary_y:
            self.rect.bottom = 0

        if self.__cherries and pygame.sprite.spritecollide(self, self.__cherries, True):
            if self.__chomp:
                self.__chomp.play()
