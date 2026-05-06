"""
Author: Dinesh Sinnathamby
Date: May 6th, 2026
Description: Four differently coloured boxes each moving in a different direction. When a box reaches an edge it wraps to the opposite edge.
"""

import pygame

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("four boxes")

        self.entities()
        self.create_boxes()
        self.alter()

        pygame.quit()

    def entities(self):
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill((255, 255, 255))

    def create_boxes(self):
        colours = [(255, 0, 0), (0, 200, 0), (0, 0, 255), (255, 192, 203)]
        directions = [(5, 0), (-5, 0), (0, 5), (0, -5)]
        starts = [(0, 200), (615, 100), (300, 0), (400, 455)]

        self.boxes = []
        for (colour, (dx, dy), (x, y)) in zip(colours, directions, starts):
            surface = pygame.Surface((25, 25)).convert()
            surface.fill(colour)
            self.boxes.append([surface, x, y, dx, dy])

    def update(self):
        w, h = self.screen.get_size()
        for box in self.boxes:
            box[1] += box[3]
            box[2] += box[4]

            if box[1] > w:
                box[1] = -25
            elif box[1] < -25:
                box[1] = w

            if box[2] > h:
                box[2] = -25
            elif box[2] < -25:
                box[2] = h

    def alter(self):
        self.clock = pygame.time.Clock()
        keepGoing = True
        while keepGoing:
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False

            self.update()

            self.screen.blit(self.background, (0, 0))
            for box in self.boxes:
                self.screen.blit(box[0], (box[1], box[2]))
            pygame.display.flip()

Main()
