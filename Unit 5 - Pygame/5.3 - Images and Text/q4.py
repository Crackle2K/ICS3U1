"""
Author: Dinesh Sinnathamby
Date: May 10th, 2026
Description: Opens portrait.png, adds a name label, and saves the result as new-portrait.png.
"""

import pygame

class Main:
    def __init__(self):
        pygame.init()
        image = pygame.image.load("portrait.png")
        pygame.display.set_mode(image.get_size())

        font = pygame.font.SysFont("Arial", 36)
        label = font.render("Dinesh Sinnathamby", True, (255, 255, 255))
        image.blit(label, (10, 10))

        pygame.image.save(image, "new-portrait.png")
        pygame.quit()


Main()
