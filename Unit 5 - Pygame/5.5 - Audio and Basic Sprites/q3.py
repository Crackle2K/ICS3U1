"""
Author: Dinesh Sinnathamby
Date: May 18th, 2026
Description: Extends q2 with background music and an edge-collision sound effect. Music is started in main(); the sound effect is handled in Box.
"""

import pygame

class Box(pygame.sprite.Sprite):
    def __init__(self, boundary):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Unit 5 - Pygame/5.5 - Audio and Basic Sprites/img/sprite.png")
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 200
        self.direction = 10
        self.boundary = boundary

        self.boing = pygame.mixer.Sound("Unit 5 - Pygame/5.5 - Audio and Basic Sprites/sound/boing.wav")
        self.boing.set_volume(0.8)

    def update(self):
        self.rect.left += self.direction
        if (self.rect.left < 0) or (self.rect.right > self.boundary):
            self.direction = -self.direction
            self.boing.play()


class Main:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Basic Sprite Demo")

        self.entities()
        self.init_box()
        self.loop()

        pygame.quit()

    def entities(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((255, 255, 0))
        self.screen.blit(self.background, (0, 0))

    def init_box(self):
        box = Box(self.screen.get_width())
        self.allSprites = pygame.sprite.Group(box)

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
