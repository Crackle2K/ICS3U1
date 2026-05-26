"""
Authors: Dinesh Sinnathamby, Dhani Shah
Date: May 21st, 2026
Description: Complex memory game built in Pygame, featuring original sprites, opening screens, and scoring.
"""

import pygame, random, math, os

_DIR = os.path.dirname(os.path.abspath(__file__))

SPECIAL_COLORS = {
    "reveal": (255, 215, 0),
    "shuffle": (255, 140, 0),
    "bonus": (0, 220, 100),
}


class Bubble:
    def __init__(self):
        """Initialize a Bubble animation with a random initial position and speed."""
        self.__spawn(anywhere=True)

    def __spawn(self, anywhere=False):
        """Spawn or reset a bubble with a random position, radius, and speed."""
        self.x = random.randint(0, 680)
        self.y = random.randint(0, 480) if anywhere else 492
        self.r = random.randint(3, 12)
        self.speed = random.uniform(0.4, 1.8)

    def update(self):
        """Update the bubble's vertical position and reset it if it moves off-screen."""
        self.y -= self.speed
        if self.y < -self.r:
            self.__spawn()

    def draw(self, surface):
        """Draw the bubble and its inner highlight onto the surface."""
        pygame.draw.circle(surface, (50, 120, 200), (int(self.x), int(self.y)), self.r, 1)
        if self.r >= 6:
            hx = int(self.x) - self.r // 3
            hy = int(self.y) - self.r // 3
            pygame.draw.circle(surface, (100, 170, 230), (hx, hy), max(1, self.r // 4))


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((680, 480))
        pygame.display.set_caption("Ocean Blitz")
        cursor_image = pygame.image.load(os.path.join(_DIR, "assets", "images", "cursor.png"))
        cursor_image = pygame.transform.scale(cursor_image, (40, 40))
        pygame.mouse.set_cursor(pygame.Cursor((0, 0), cursor_image))

        self.__time_limit = 45
        self.__shuffle_button_rect = pygame.Rect(550, 285, 130, 35)
        self.__replay_button_rect = pygame.Rect(550, 335, 130, 35)
        self.__font = pygame.font.SysFont("Arial", 22)
        self.__small_font = pygame.font.SysFont("Arial", 13)

        self.__load_sound_effects()

        if self.__show_title_screen():
            self.__entities()
            self.__load_music()
            self.__loop()

        pygame.quit()

    def __show_title_screen(self):
        clock = pygame.time.Clock()

        bg_raw = pygame.image.load(os.path.join(_DIR, "assets", "images", "title_screen.png")).convert()
        bg_img = pygame.transform.scale(bg_raw, (680, 480))

        play_rect = pygame.Rect(0, 0, 140, 50)
        play_rect.bottomright = (662, 462)

        bubbles = [Bubble() for _ in range(24)]
        head_font = pygame.font.SysFont("Arial", 19, bold=True)
        body_font = pygame.font.SysFont("Arial", 15)

        while True:
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_rect.collidepoint(event.pos):
                        return True

            self.screen.blit(bg_img, (0, 0))

            for b in bubbles:
                b.update()
                b.draw(self.screen)
            
            mouse_pos = pygame.mouse.get_pos()
            btn_color = (60, 180, 80) if play_rect.collidepoint(mouse_pos) else (40, 140, 60)
            pygame.draw.rect(self.screen, btn_color, play_rect, border_radius=8)
            pygame.draw.rect(self.screen, (100, 255, 130), play_rect, width=2, border_radius=8)
            play_lbl = head_font.render("PLAY", True, (255, 255, 255))
            self.screen.blit(play_lbl, play_lbl.get_rect(center=play_rect.center))

            pygame.display.flip()

    def __entities(self):
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill((10, 10, 40))
        self.__reset_game()

    def __reset_game(self):
        self.__flipped_cards = []
        self.__waiting = False
        self.__peeking = False
        self.__peeked_tiles = []
        self.__peek_timer = 0
        self.__moves = 0
        self.__timer_start = None
        self.__win_time = None
        self.__game_won = False
        self.__game_lost = False
        self.__score = 0
        self.__bonus_points = 0
        self.__notification = None

        image_list = [
            "person.png", "ocean.png", "beach.png", "diver.png",
            "cave.png", "shark.png", "jellyfish.png", "pearl.png",
        ]

        special_images = random.sample(image_list, 3)
        special_assign = dict(zip(special_images, ["reveal", "shuffle", "bonus"]))

        tiles = [(img, special_assign.get(img)) for img in image_list] * 2
        random.shuffle(tiles)
        self.__build_grid_from_list(tiles)

    def __build_grid_from_list(self, tile_list):
        self.all_tiles = pygame.sprite.Group()
        tilesize, margin = 100, 10
        for idx, (img, special) in enumerate(tile_list):
            row, col = divmod(idx, 4)
            x = 100 + col * (tilesize + margin)
            y = 20 + row * (tilesize + margin)
            self.all_tiles.add(Tile(img, special, x, y))

    def __shuffle_only(self):
        if self.__game_won or self.__game_lost:
            return
        tiles = [(t.face_up_img, t.special) for t in self.all_tiles]
        random.shuffle(tiles)
        self.__flipped_cards = []
        self.__waiting = False
        self.__peeking = False
        self.__peeked_tiles = []
        self.__build_grid_from_list(tiles)

    def __shuffle_remaining(self):
        if self.__game_won or self.__game_lost:
            return

        all_list = list(self.all_tiles)
        matched_data = [(t.rect.left, t.rect.top, t.face_up_img, t.special)
                        for t in all_list if t.is_matched]
        unmatched_pos = [(t.rect.left, t.rect.top) for t in all_list if not t.is_matched]
        unmatched_data = [(t.face_up_img, t.special) for t in all_list if not t.is_matched]

        random.shuffle(unmatched_data)
        self.all_tiles = pygame.sprite.Group()

        for x, y, img, special in matched_data:
            t = Tile(img, special, x, y)
            t.is_matched = True
            t.flip()
            self.all_tiles.add(t)

        for i, (img, special) in enumerate(unmatched_data):
            x, y = unmatched_pos[i]
            self.all_tiles.add(Tile(img, special, x, y))

        self.__flipped_cards = []
        self.__waiting = False

    def __load_music(self):
        try:
            pygame.mixer.music.load(os.path.join(_DIR, "assets", "sounds", "aria_math.ogg"))
            pygame.mixer.music.play(-1)
        except Exception:
            pass

    def __load_sound_effects(self):
        self.__snd_flip = None
        self.__snd_match = None
        self.__snd_win = None
        try:
            self.__snd_flip = pygame.mixer.Sound(os.path.join(_DIR, "assets", "sounds", "cardflip.mp3"))
        except Exception:
            pass
        try:
            self.__snd_match = pygame.mixer.Sound(os.path.join(_DIR, "assets", "sounds", "matched.mp3"))
        except Exception:
            pass
        try:
            self.__snd_win = pygame.mixer.Sound(os.path.join(_DIR, "assets", "sounds", "winsound.mp3"))
        except Exception:
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
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.__keep_going = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.__shuffle_button_rect.collidepoint(event.pos):
                    self.__shuffle_only()
                    return
                if self.__replay_button_rect.collidepoint(event.pos):
                    self.__reset_game()
                    if not pygame.mixer.music.get_busy():
                        self.__load_music()
                    return

                can_flip = (
                    not self.__waiting
                    and not self.__peeking
                    and not self.__game_won
                    and not self.__game_lost
                )
                if can_flip:
                    for tile in self.all_tiles:
                        if tile.rect.collidepoint(event.pos) and not tile.is_flip:
                            if self.__timer_start is None:
                                self.__timer_start = pygame.time.get_ticks()
                            tile.flip()
                            if self.__snd_flip:
                                self.__snd_flip.play()
                            self.__flipped_cards.append(tile)
                            if len(self.__flipped_cards) == 2:
                                self.__moves += 1
                                self.__check_match()
                            break

    def __check_match(self):
        card1, card2 = self.__flipped_cards
        if card1.face_up_img == card2.face_up_img:
            if self.__snd_match:
                self.__snd_match.play()
            card1.is_matched = True
            card2.is_matched = True
            if card1.special:
                self.__trigger_special(card1.special)
            self.__flipped_cards = []
            self.__check_win()
        else:
            self.__waiting = True
            self.__wait_timer = pygame.time.get_ticks()

    def __trigger_special(self, special_type):
        now = pygame.time.get_ticks()
        if special_type == "reveal":
            self.__peeked_tiles = [
                t for t in self.all_tiles if not t.is_matched and not t.is_flip
            ]
            for t in self.__peeked_tiles:
                t.flip()
            self.__peeking = True
            self.__peek_timer = now
            self.__set_notification("REVEAL! Cards shown for 2s", SPECIAL_COLORS["reveal"], 3000)
        elif special_type == "shuffle":
            self.__shuffle_remaining()
            self.__set_notification("SHUFFLE! Remaining cards mixed", SPECIAL_COLORS["shuffle"], 3000)
        elif special_type == "bonus":
            self.__bonus_points += 500
            self.__moves = max(0, self.__moves - 3)
            self.__set_notification("BONUS! +500 pts, -3 moves", SPECIAL_COLORS["bonus"], 3000)

    def __set_notification(self, text, color, duration_ms):
        self.__notification = (text, color, pygame.time.get_ticks() + duration_ms)

    def __check_win(self):
        if all(t.is_matched for t in self.all_tiles):
            self.__game_won = True
            self.__win_time = pygame.time.get_ticks()
            pygame.mixer.music.stop()
            if self.__snd_win:
                self.__snd_win.play()

            elapsed = (self.__win_time - self.__timer_start) // 1000
            remaining_time = max(0, self.__time_limit - elapsed)
            extra_moves = max(0, self.__moves - 8)
            accuracy_score = max(0, 10000 - extra_moves * 250)
            time_bonus = remaining_time * 100
            self.__score = accuracy_score + time_bonus + self.__bonus_points

    def __update(self):
        if not self.__game_won and not self.__game_lost and self.__get_elapsed() == 0:
            self.__game_lost = True

        if self.__waiting:
            if pygame.time.get_ticks() - self.__wait_timer > 1000:
                for t in self.__flipped_cards:
                    t.flip()
                self.__flipped_cards = []
                self.__waiting = False

        if self.__peeking:
            if pygame.time.get_ticks() - self.__peek_timer > 2000:
                for t in self.__peeked_tiles:
                    if not t.is_matched:
                        t.flip()
                self.__peeked_tiles = []
                self.__peeking = False

    def __get_elapsed(self):
        if self.__timer_start is None:
            return self.__time_limit
        if self.__game_won:
            elapsed = (self.__win_time - self.__timer_start) // 1000
        else:
            elapsed = (pygame.time.get_ticks() - self.__timer_start) // 1000
        return max(0, self.__time_limit - elapsed)

    def __refresh(self):
        self.screen.blit(self.background, (0, 0))
        self.all_tiles.draw(self.screen)

        elapsed = self.__get_elapsed()
        moves_surf = self.__font.render(f"Moves: {self.__moves}", True, (255, 255, 255))
        time_surf = self.__font.render(f"Remaining: {elapsed}s", True, (255, 255, 255))
        self.screen.blit(moves_surf, (560, 180))
        self.screen.blit(time_surf, (560, 225))

        if self.__notification:
            text, color, expire = self.__notification
            if pygame.time.get_ticks() < expire:
                notif_surf = self.__small_font.render(text, True, color)
                self.screen.blit(notif_surf, notif_surf.get_rect(topleft=(522, 258)))
            else:
                self.__notification = None

        legend_y = 390
        for stype, color in SPECIAL_COLORS.items():
            pygame.draw.rect(self.screen, color, (522, legend_y, 12, 12), border_radius=2)
            lbl = self.__small_font.render(stype.capitalize(), True, (200, 200, 200))
            self.screen.blit(lbl, (538, legend_y))
            legend_y += 18
            
        self.__color_refresh()

    
    def __color_refresh(self):
        elapsed = self.__get_elapsed()
        mouse_pos = pygame.mouse.get_pos()
        if self.__shuffle_button_rect.collidepoint(mouse_pos):
            shuf_color = (60, 130, 200)
        else:
            shuf_color = (40, 90, 160)
            
        pygame.draw.rect(self.screen, shuf_color, self.__shuffle_button_rect, border_radius=6)
        shuf_txt = self.__font.render("Shuffle", True, (255, 255, 255))
        self.screen.blit(shuf_txt, shuf_txt.get_rect(center=self.__shuffle_button_rect.center))

        rep_color = (40, 180, 120) if self.__replay_button_rect.collidepoint(mouse_pos) else (30, 140, 90)
        pygame.draw.rect(self.screen, rep_color, self.__replay_button_rect, border_radius=6)
        rep_txt = self.__font.render("Replay", True, (255, 255, 255))
        self.screen.blit(rep_txt, rep_txt.get_rect(center=self.__replay_button_rect.center))

        if self.__game_won:
            self.__draw_win_screen(elapsed)
        elif self.__game_lost:
            self.__draw_lose_screen()

        pygame.display.flip()

    def __draw_win_screen(self, elapsed):
        """Draw win screen with score and time(calculated by 45 - elapsed time)"""
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))

        big_font = pygame.font.SysFont("Arial", 48)
        win_surf = big_font.render("You Win!", True, (255, 215, 0))
        stats_surf = self.__font.render(
            f"Moves: {self.__moves}   Time: {self.__time_limit - elapsed}s", True, (255, 255, 255)
        )
        score_surf = big_font.render(f"Score: {self.__score}", True, (0, 255, 128))
        self.screen.blit(win_surf, win_surf.get_rect(center=(320, 210)))
        self.screen.blit(stats_surf, stats_surf.get_rect(center=(320, 270)))
        self.screen.blit(score_surf, score_surf.get_rect(center=(320, 300)))

    def __draw_lose_screen(self):
        """Draw lose screen if time limit is exceeds"""
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))

        big_font = pygame.font.SysFont("Arial", 48)
        lose_surf = big_font.render("Game Over!", True, (220, 20, 60))
        stats_surf = self.__font.render("You ran out of time.", True, (255, 255, 255))
        self.screen.blit(lose_surf, lose_surf.get_rect(center=(320, 210)))
        self.screen.blit(stats_surf, stats_surf.get_rect(center=(320, 270)))


class Tile(pygame.sprite.Sprite):
    def __init__(self, face_up, special, x, y):
        """Initialize an individual game Tile sprite, face_up:image loaded when flipped face-up, and x,y coordinates of the tile"""
        pygame.sprite.Sprite.__init__(self)
        self.face_up_img = face_up
        self.special = special
        self.is_flip = False
        self.is_matched = False

        self.image = self.__make_back()
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

    def __make_back(self):
        """Create the generic face-down back image surface for a tile, applying colored borders for special tiles."""
        raw = pygame.image.load(os.path.join(_DIR, "assets", "images", "back.png")).convert_alpha()
        surf = pygame.transform.scale(raw, (100, 100))
        if self.special:
            pygame.draw.rect(surf, SPECIAL_COLORS[self.special],
                             surf.get_rect(), width=5, border_radius=5)
        return surf

    def flip(self):
        """Change tile's orientation between face-up and face-down, loading and adjusting the corresponding sprite assets."""
        self.is_flip = not self.is_flip
        if self.is_flip:
            raw = pygame.image.load(os.path.join(_DIR, "assets", "images", self.face_up_img)).convert_alpha()
            surf = pygame.transform.scale(raw, (100, 100))
            if self.special:
                pygame.draw.rect(surf, SPECIAL_COLORS[self.special],
                                 surf.get_rect(), width=5, border_radius=5)
            self.image = surf
        else:
            self.image = self.__make_back()


Main()
