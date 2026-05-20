"""
Author: Dinesh Sinnathamby
Date: May 19th, 2026
Description: Sprite module for pyPong. Contains Ball, Player, EndZone, and ScoreKeeper classes.
"""
import pygame

class Ball(pygame.sprite.Sprite):

  def __init__(self, screen):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((20, 20))
    self.image.fill((0, 0, 0))
    self.image.set_colorkey((0, 0, 0))
    pygame.draw.circle(self.image, (255, 220, 0), (10, 10), 10, 0)
    self.rect = self.image.get_rect()
    self.rect.center = (screen.get_width()/2, screen.get_height()/2)
    self.__screen = screen
    self.__dx = 5
    self.__dy = -3

  def change_direction(self):
    self.__dx = -self.__dx

  def update(self):
    if ((self.rect.left > 0) and (self.__dx < 0)) or ((self.rect.right < self.__screen.get_width())
    and (self.__dx > 0)):
      self.rect.left += self.__dx
    else:
      self.__dx = -self.__dx

    if ((self.rect.top-40 > 0) and (self.__dy > 0)) or  ((self.rect.bottom+40 < self.__screen.get_height())
    and (self.__dy < 0)):
      self.rect.top -= self.__dy
    else:
      self.__dy = -self.__dy


class Player(pygame.sprite.Sprite):
  def __init__(self, screen, player_num):
    pygame.sprite.Sprite.__init__(self)

    if player_num == 1:
      paddle_color = (0, 200, 255)
    else:
      paddle_color = (255, 120, 0)

    self.image = pygame.Surface((40, 100))
    self.image = self.image.convert()
    self.image.fill(paddle_color)
    self.rect = self.image.get_rect()

    if player_num == 1:
      self.rect.left = 10
    else:
      self.rect.right = screen.get_width()-10

    self.rect.top = screen.get_height()/2 + 50
    self.__screen = screen
    self.__dy = 0

  def change_direction(self, xy_change):
    self.__dy = xy_change[1]

  def update(self):
    if ((self.rect.top > 0) and (self.__dy > 0)) or    ((self.rect.bottom < self.__screen.get_height())
      and (self.__dy < 0)):
      self.rect.top -= (self.__dy*5)


class EndZone(pygame.sprite.Sprite):
  def __init__(self, screen, x_position):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.Surface((1, screen.get_height()))
    self.image = self.image.convert()
    self.image.fill((255, 255, 255))

    self.rect = self.image.get_rect()
    self.rect.left = x_position
    self.rect.top = 0


class ScoreKeeper(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.__font = pygame.font.SysFont("Arial", 30)
    self.__player1_score = 0
    self.__player2_score = 0

  def player1_scored(self):
    self.__player1_score += 1

  def player2_scored(self):
    self.__player2_score += 1

  def winner(self):
    if self.__player1_score == 3:
      return 1
    elif self.__player2_score == 3:
      return 2
    else:
      return 0

  def update(self):
    message = "Player 1: %d vs. Player 2: %d" % (self.__player1_score, self.__player2_score)
    self.image = self.__font.render(message, 1, (255, 255, 255))
    self.rect = self.image.get_rect()
    self.rect.center = (320, 15)
