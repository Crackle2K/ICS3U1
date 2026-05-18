"""
Author: Dinesh Sinnathamby
Date: May 18th, 2026
Description: Reusable sprite module containing Circle, Label, and Brick classes.
"""

import os
import random
import pygame


class Circle(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (50, 50), 50)
        self.rect = self.image.get_rect()


class Label(pygame.sprite.Sprite):
    def __init__(self, message, x_y_center, font_name, size, color):
        pygame.sprite.Sprite.__init__(self)
        self.__message = message
        self.__font_name = font_name
        self.__size = size
        self.__color = color
        font = pygame.font.SysFont(self.__font_name, self.__size)
        self.image = font.render(self.__message, True, self.__color)
        self.rect = self.image.get_rect()
        self.rect.center = x_y_center


class Brick(pygame.sprite.Sprite):
    _IMG_PATH = os.path.join(os.path.dirname(pygame.__file__), "examples", "data", "brick.png")

    def __init__(self, boundary):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Brick._IMG_PATH)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, boundary[0]), random.randint(0, boundary[1]))
        self.dx = random.randint(1, 3) * random.choice([-1, 1])
        self.dy = random.randint(1, 3) * random.choice([-1, 1])
        self.__boundary_x = boundary[0]
        self.__boundary_y = boundary[1]

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy

        if self.rect.left < 0 or self.rect.right > self.__boundary_x:
            self.dx = -self.dx
        if self.rect.top < 0 or self.rect.bottom > self.__boundary_y:
            self.dy = -self.dy
