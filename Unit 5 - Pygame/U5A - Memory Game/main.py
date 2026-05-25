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
        cursor_image = pygame.image.load(r"Unit 5 - Pygame\U5A - Memory Game\assets\images\cursor.png")
        cursor_image = pygame.transform.scale(cursor_image, (24, 24))
        pygame.mouse.set_cursor(pygame.Cursor((0, 0), cursor_image))
        self.__flipped_cards = []
        self.__waiting = False
        self.__moves = 0
        self.__timer_start = None
        self.__win_time = None
        self.__game_won = False

        self.__entities()
        self.__load_music()
        self.__loop()

        pygame.quit()

    def __entities(self):
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill((10, 10, 40))

        self.__font = pygame.font.SysFont("Arial", 22)

        image_list = ["person.png", "ocean.png", "beach.png", "diver.png", "cave.png", "shark.png", "jellyfish.png", "pearl.png"]
        tiles = image_list * 2
        random.shuffle(tiles)

        self.all_tiles = pygame.sprite.Group()
        tilesize = 100
        margin = 10
        idx = 0

        for row in range(4):
            for col in range(4):
                x = 100 + col * (tilesize + margin)
                y = 20 + row * (tilesize + margin)
                new_tile = Tile(tiles[idx], x, y)
                self.all_tiles.add(new_tile)
                idx += 1

    def __load_music(self):
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
            self.__update()
            self.__refresh()

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__keep_going = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__keep_going = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.__waiting and not self.__game_won:
                for tile in self.all_tiles:
                    if tile.rect.collidepoint(event.pos) and not tile.is_flip:
                        if self.__timer_start is None:
                            self.__timer_start = pygame.time.get_ticks()
                        tile.flip()
                        self.__flipped_cards.append(tile)
                        if len(self.__flipped_cards) == 2:
                            self.__moves += 1
                            self.__check_match()
                        break

    def __check_match(self):
        card1, card2 = self.__flipped_cards
        if card1.face_up_img == card2.face_up_img:
            self.__flipped_cards = []
            self.__check_win()
        else:
            self.__waiting = True
            self.__wait_timer = pygame.time.get_ticks()

    def __check_win(self):
        if all(tile.is_flip for tile in self.all_tiles):
            self.__game_won = True
            self.__win_time = pygame.time.get_ticks()

    def __update(self):
        if self.__waiting:
            current_time = pygame.time.get_ticks()
            if current_time - self.__wait_timer > 1000:
                for tile in self.__flipped_cards:
                    tile.flip()
                self.__flipped_cards = []
                self.__waiting = False

    def __get_elapsed(self):
        if self.__timer_start is None:
            return 0
        if self.__game_won:
            return (self.__win_time - self.__timer_start) // 1000
        return (pygame.time.get_ticks() - self.__timer_start) // 1000

    def __refresh(self):
        self.screen.blit(self.background, (0, 0))
        self.all_tiles.draw(self.screen)

        elapsed = self.__get_elapsed()
        moves_surf = self.__font.render(f"Moves: {self.__moves}", True, (255, 255, 255))
        time_surf = self.__font.render(f"Time: {elapsed}s", True, (255, 255, 255))
        self.screen.blit(moves_surf, (540, 180))
        self.screen.blit(time_surf, (540, 225))

        if self.__game_won:
            self.__draw_win_screen(elapsed)

        pygame.display.flip()

    def __draw_win_screen(self, elapsed):
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))

        big_font = pygame.font.SysFont("Arial", 48)
        win_surf = big_font.render("You Win!", True, (255, 215, 0))
        stats_surf = self.__font.render(f"Moves: {self.__moves}   Time: {elapsed}s", True, (255, 255, 255))

        self.screen.blit(win_surf, win_surf.get_rect(center=(320, 210)))
        self.screen.blit(stats_surf, stats_surf.get_rect(center=(320, 270)))


class Tile(pygame.sprite.Sprite):
    def __init__(self, face_up, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.face_up_img = face_up
        self.is_flip = False

        raw_back = pygame.image.load(r"Unit 5 - Pygame\U5A - Memory Game\assets\images\back.png").convert_alpha()
        self.image = pygame.transform.scale(raw_back, (100, 100))
        

        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

    def flip(self):
        self.is_flip = not self.is_flip

        if self.is_flip:
            raw_front = pygame.image.load(r"Unit 5 - Pygame\U5A - Memory Game\assets\images\\" + self.face_up_img).convert_alpha()
            self.image = pygame.transform.scale(raw_front, (100, 100))
        else:
            raw_back = pygame.image.load(r"Unit 5 - Pygame\U5A - Memory Game\assets\images\back.png").convert_alpha()
            self.image = pygame.transform.scale(raw_back, (100, 100))

Main()
