import pygame, math

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Drawing commands")
        self.entities()
        self.draw_stuff()
        self.clock = pygame.time.Clock()
        self.loop()
        pygame.quit()
        
    def entities(self):
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill((255, 255, 255))
        
    def loop(self):
        keepGoing = True
        while keepGoing:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    print(pygame.mouse.get_pos())
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()
        
    def draw_stuff(self):
        pygame.draw.line(self.background, (255, 0, 0), (5, 100), (100, 100))
        pygame.draw.rect(self.background, (0, 255, 0), ((200, 5), (100, 100)), 3)
        pygame.draw.circle(self.background, (0, 0, 255), (400, 50), 45)
        pygame.draw.ellipse(self.background, (204, 204, 0), ((150, 150), (150, 100)), 0)
        pygame.draw.arc(self.background, (0, 0, 0), ((5, 150), (100, 100)), 0, math.pi/2, 5)
        points = ( (370, 160), (370, 237), (372, 193), (411, 194), (412, 237),
        (412, 160), (412, 237), (432, 227), (436, 196), (433, 230) )
        pygame.draw.lines(self.background, (0xFF, 0x00, 0x00), False, points, 3)
        points = ( (137, 372), (232, 319), (383, 335), (442, 389),
        (347, 432), (259, 379), (220, 439), (132, 392) )
        pygame.draw.polygon(self.background, (0x33, 0xFF, 0x33), points)
        pygame.draw.line(self.background, (0, 0, 0), (480, 425), (550, 325), 1)
        pygame.draw.aaline(self.background, (0, 0, 0), (500, 425), (570, 325), 1)
        
Main()