"""
Authors: Dinesh Sinnathamby, Dhani Shah
Date: May 21st, 2026
Description: Complex memory game built in Pygame, featuring original sprites, opening screens, and scoring.
"""

import pygame

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Memory Game v1.0.0")

        self.__entities()
        self.__load_music()

        self.__loop()
        
        pygame.quit()
        
    def __entities(self):
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill((10, 10, 40))
        self.screen.blit(self.background, (0, 0))
        
    def __load_music(self):
        """Load and loop background music if a file is present"""
        try:
            pygame.mixer.music.load(r"Unit 5 - Pygame\U5A - Memory Game\assets\sounds\aria_math.ogg")
            pygame.mixer.music.play(-1)
        except:
            pass
    
    def __loop(self):
        clock = pygame.time.Clock()
        self.__keep_going = True

        while self.__keep_going:
            clock.tick(30)
            self.__handle_events()
            self.__refresh()
            
    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__keep_going = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__keep_going = False
                    
    def __refresh(self):
        pygame.display.flip()
        
Main()