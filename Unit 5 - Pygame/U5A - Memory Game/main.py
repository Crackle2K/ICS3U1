"""
Authors: Dinesh Sinnathamby, Dhani Shah
Date: May 21st, 2026
Description: Complex memory game built in Pygame, featuring original sprites, opening screens, and scoring.
"""

import pygame, random

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Memory Game v1.0.0")
        self.__flipped_cards = []
        self.__waiting = False
        
        self.__entities()
        self.__load_music()

        self.__loop()
        
        pygame.quit()
        
    def __entities(self):
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill((10, 10, 40))
        self.screen.blit(self.background, (0, 0))
        
        image_list = ["person1.png", "ocean.png", "beach.png", "person2.png", "cave.png", "shark.png"]
        tiles = image_list * 2
        random.shuffle(tiles)
        
        self.all_tiles = pygame.sprite.Group()
        tilesize = 100
        margin = 10
        idx = 0
        
        for row in range(4):
            for col in range(3):
                x = 100 + col * (tilesize + margin)
                y = 40 + row * (tilesize + margin)
                
                new_tile = Tile(tiles[idx], x, y)
                self.all_tiles.add(new_tile)
                idx += 1
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
            self.__update()
    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__keep_going = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__keep_going = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.__waiting:
                for tile in self.all_tiles:
                    if tile.rect.collidepoint(event.pos) and not tile.is_flip:
                        tile.flip()
                        self.__flipped_cards.append(tile)
                        
                        if len(self.__flipped_cards) == 2:
                            self.__check_match()

    def __check_match(self):
        card1, card2 = self.__flipped_cards
        if card1.face_up_img == card2.face_up_img:
            # Match! Clear list so player can pick next pair
            self.__flipped_cards = []
        else:
            # No match! Start the "Wait" state
            self.__waiting = True
            self.__wait_timer = pygame.time.get_ticks()

    def __update(self):
        '''Flips cards back down after 1 second if they don't match'''
        if self.__waiting:
            current_time = pygame.time.get_ticks()
            if current_time - self.__wait_timer > 1000:

                for tile in self.__flipped_cards:
                    tile.flip()
                self.__flipped_cards = []
                self.__waiting = False

    def __refresh(self):
        self.all_tiles.clear(self.screen, self.background)
        self.all_tiles.update()
        self.all_tiles.draw(self.screen)
        pygame.display.flip()
        
    
class Tile(pygame.sprite.Sprite):
    def __init__(self, face_up, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.face_up_img = face_up
        self.is_flip = False
        
        raw_back = pygame.image.load("img\\back.png").convert_alpha()
        self.image = pygame.transform.scale(raw_back, (100, 100))
        
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        
    def flip(self):
        self.is_flip = not self.is_flip
        
        if self.is_flip:
            raw_front = pygame.image.load("img\\" + self.face_up_img).convert_alpha()
            self.image = pygame.transform.scale(raw_front, (100, 100))
        else:
            raw_back = pygame.image.load("img\\back.png").convert_alpha()
            self.image = pygame.transform.scale(raw_back, (100, 100))

Main()
        
