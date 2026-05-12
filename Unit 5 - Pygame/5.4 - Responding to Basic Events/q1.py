"""
Author: Dinesh Sinnathamby
Date: May 11th, 2026
Description: Implements various events into an existing paint program.
"""

import pygame
import os
pygame.init()

def statusSurface(drawColor, lineWidth):
    myFont = pygame.font.SysFont("Courier", 20)
    status_string = "color: %s, width: %d" % (drawColor, lineWidth)
    status = myFont.render(status_string, 1, (drawColor))
    return status

def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint: (w)hite, blac(k), (r)ed, (g)reen, (b)lue, (c)lear, (s)ave, (l)oad, (q)uit")

    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))

    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (0, 0, 0)
    lineWidth = 3

    while keepGoing:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

            elif event.type == pygame.MOUSEMOTION:
                lineEnd = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.line(background, drawColor, lineStart,
                                     lineEnd, lineWidth)
                lineStart = lineEnd

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    keepGoing = False
                elif event.key == pygame.K_c:
                    background.fill((255, 255, 255))
                elif event.key == pygame.K_w:
                    drawColor = (255, 255, 255)
                elif event.key == pygame.K_k:
                    drawColor = (0, 0, 0)
                elif event.key == pygame.K_r:
                    drawColor = (255, 0, 0)
                elif event.key == pygame.K_g:
                    drawColor = (0, 255, 0)
                elif event.key == pygame.K_b:
                    drawColor = (0, 0, 255)
                elif event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9):
                    lineWidth = event.key - pygame.K_0
                elif event.key == pygame.K_s:
                    pygame.image.save(background, "painting.bmp")
                elif event.key == pygame.K_l:
                    if os.path.exists("painting.bmp"):
                        loaded = pygame.image.load("painting.bmp")
                        background.blit(loaded, (0, 0))

        screen.blit(background, (0, 0))
        myLabel = statusSurface(drawColor, lineWidth)
        screen.blit(myLabel, (450, 450))
        pygame.display.flip()

    pygame.quit()

main()
