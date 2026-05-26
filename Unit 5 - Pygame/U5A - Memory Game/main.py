"""
Authors: Dinesh Sinnathamby, Dhani Shah
Date: May 21st, 2026
Description: Complex memory game built in Pygame, featuring original sprites, opening screens, and scoring.
"""

import pygame, random

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((680, 480))
        pygame.display.set_caption("Memory Game v1.0.0")
        cursor_image = pygame.image.load(r"Unit 5 - Pygame\U5A - Memory Game\assets\images\cursor.png")
        cursor_image = pygame.transform.scale(cursor_image, (40, 40))
        pygame.mouse.set_cursor(pygame.Cursor((0, 0), cursor_image))
        self.__flipped_cards = []
        self.__waiting = False
        self.__moves = 0
        self.__timer_start = None
        self.__win_time = None
        self.__game_won = False
        self.__game_lost = False
        self.__time_limit = 45
        self.__score = 0

        self.__entities()
        self.__load_music()
        self.__load_sound_effects()

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
    def __load_sound_effects(self):
        self.__snd_flip = None
        self.__snd_match = None
        self.__snd_win = None
        
        self.__snd_flip = pygame.mixer.Sound(r"sounds\\cardflip.mp3")
        self.__snd_match = pygame.mixer.Sound(r"sounds\\matched.mp3")
        self.__snd_win = pygame.mixer.Sound(r"sounds\\winsound.mp3")
    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__keep_going = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__keep_going = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.__waiting and not self.__game_won and not self.__game_lost:
                for tile in self.all_tiles:
                    if tile.rect.collidepoint(event.pos) and not tile.is_flip:
                        if self.__timer_start is None:
                            self.__timer_start = pygame.time.get_ticks()
                        tile.flip()
                        self.__snd_flip.play()

                        self.__flipped_cards.append(tile)
                        if len(self.__flipped_cards) == 2:
                            self.__moves += 1
                            self.__check_match()
                        break

    def __check_match(self):
        card1, card2 = self.__flipped_cards
        if card1.face_up_img == card2.face_up_img:
            self.__snd_match.play()
            self.__flipped_cards = []
            self.__check_win()
        else:
            self.__waiting = True
            self.__wait_timer = pygame.time.get_ticks()

    def __check_win(self):
        if all(tile.is_flip for tile in self.all_tiles):
            self.__game_won = True
            self.__win_time = pygame.time.get_ticks()
            pygame.mixer.music.stop()
            self.__snd_win.play()
            elapsed = (self.__win_time - self.__timer_start)//1000
            remaining_time = max(0, self.__time_limit - elapsed)
            
            extra_moves = max(0, self.__moves - 8)
            accuracy_score = max(0, 10000 - (extra_moves * 250))
            time_bonus = remaining_time * 100
            
            self.__score = accuracy_score + time_bonus
    def __update(self):
        
        if not self.__game_won and not self.__game_lost and self.__get_elapsed == 0:
            self.__game_lost = True
        
        if self.__waiting:
            current_time = pygame.time.get_ticks()
            if current_time - self.__wait_timer > 1000:
                for tile in self.__flipped_cards:
                    tile.flip()
                self.__flipped_cards = []
                self.__waiting = False

    def __get_elapsed(self):
        if self.__timer_start is None:
            return self.__time_limit
        if self.__game_won:
            elapsed = (self.__win_time - self.__timer_start) // 1000
        else:
            elapsed = (pygame.time.get_ticks() - self.__timer_start) // 1000
            
        remaining_time = self.__time_limit - elapsed
        return max(0, remaining_time)
    
    def __refresh(self):
        self.screen.blit(self.background, (0, 0))
        self.all_tiles.draw(self.screen)

        elapsed = self.__get_elapsed()
        moves_surf = self.__font.render(f"Moves: {self.__moves}", True, (255, 255, 255))
        
        time_surf = self.__font.render(f"Remaining: {elapsed}s", True, (255, 255, 255))
        
        self.screen.blit(moves_surf, (530, 180))
        self.screen.blit(time_surf, (530, 225))

        if self.__game_won:
            self.__draw_win_screen(elapsed)
        elif self.__game_lost:
            self.__draw_lose_screen()

        pygame.display.flip()

    def __draw_win_screen(self, elapsed):
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))

        big_font = pygame.font.SysFont("Arial", 48)
        win_surf = big_font.render("You Win!", True, (255, 215, 0))
        stats_surf = self.__font.render(f"Moves: {self.__moves}   Time: {elapsed}s", True, (255, 255, 255))
        score_surf = big_font.render(f"Score: {self.__score}", True, (0, 255, 128))
        self.screen.blit(win_surf, win_surf.get_rect(center=(320, 210)))
        self.screen.blit(stats_surf, stats_surf.get_rect(center=(320, 270)))
        self.screen.blit(score_surf, score_surf.get_rect(center=(320, 300)))
    def __draw_lose_screen(self):
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))

        big_font = pygame.font.SysFont("Arial", 48)
        lose_surf = big_font.render("Game Over!", True, (220, 20, 60))
        stats_surf = self.__font.render("You ran out of time.", True, (255, 255, 255))

        self.screen.blit(lose_surf, lose_surf.get_rect(center=(320, 210)))
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
