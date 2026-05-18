"""
Author: Dinesh Sinnathamby
Date: May 18th, 2026
Description: Extends q4 with three coloured Box sprites. Each Box accepts a colour and starting (x, y) position via __init__ parameters.
"""

import pygame

class Box(pygame.sprite.Sprite):
    def __init__(self, boundary, color, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50, 50))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.dx = 10
        self.dy = 10
        self.boundary_x = boundary[0]
        self.boundary_y = boundary[1]

        self.boing = pygame.mixer.Sound("Unit 5 - Pygame/5.5 - Audio and Basic Sprites/sound/boing.wav")
        self.boing.set_volume(0.8)

    def update(self):
        self.rect.left += self.dx
        self.rect.top += self.dy

        if (self.rect.left < 0) or (self.rect.right > self.boundary_x):
            self.dx = -self.dx
            self.boing.play()

        if (self.rect.top < 0) or (self.rect.bottom > self.boundary_y):
            self.dy = -self.dy
            self.boing.play()


class Main:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Basic Sprite Demo")

        self.entities()
        self.init_boxes()
        self.loop()

        pygame.quit()

    def entities(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))

    def init_boxes(self):
        boundary = self.screen.get_size()
        red_box   = Box(boundary, (255, 0, 0), 0, 100)
        green_box = Box(boundary, (0, 200, 0), 200, 300)
        blue_box  = Box(boundary, (0, 0, 255), 400, 50)
        self.allSprites = pygame.sprite.Group(red_box, green_box, blue_box)

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


def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load("Unit 5 - Pygame/5.5 - Audio and Basic Sprites/sound/boing.wav")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    Main()

    pygame.mixer.music.stop()


main()
