"""
Author: Dinesh Sinnathamby
Date: May 6th, 2026
Description: Creates a pygame GUI, with a pink box infinitely traveling down diagonally on top of a white background.
"""

# Initialize
import pygame

class Main:
    def __init__(self):
        pygame.init()
        # Display
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("move a box")

        self.entities()
        self.create_box()

        self.alter()

        # Close the game window
        pygame.quit()

    def entities(self):
        # Entities
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill((255, 255, 255))    # white background
    
    def create_box(self):
        """ make a red 25 x 25 box """
        box = pygame.Surface((25, 25))
        self.box = box.convert()
        self.box.fill((255, 192, 203))

        # set up some box variables
        self.box_x, self.box_y = 0, 0
    
    def update(self):
        #modify box value
        self.box_x += 5
        self.box_y += 5  
        #check boundaries
        if (self.box_y > 480) or (self.box_x > 640):
            self.box_x = 0
            self.box_y = 0
            
    def alter(self):
        """ Run infinite loop until user quit"""
        
        # ACTION, Assign 
        self.clock = pygame.time.Clock()
        
        # loop
        keepGoing = True 
        while keepGoing: 

            # T - Timer to set the frame rate 
            self.clock.tick(30)
            
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
            self.update()
            
            # Refresh screen
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.box, (self.box_x, self.box_y))
            pygame.display.flip()

Main()