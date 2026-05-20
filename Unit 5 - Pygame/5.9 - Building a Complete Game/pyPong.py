"""
Author: Dinesh Sinnathamby
Date: May 19th, 2026
Description: Main game module for pyPong, a two-player Pong game built with Pygame.
"""
import pygame, pySprites

class Main(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("pyPong! v1.0")

        self.__entities()
        self.__entities_sprite()
        self.__load_music()

        pygame.mouse.set_visible(False)

        self.__loop()

        pygame.mouse.set_visible(True)
        pygame.quit()

    def __entities(self):
        """ENTITIES for self.background"""
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill((10, 10, 40))
        self.screen.blit(self.background, (0, 0))

    def __entities_sprite(self):
        """Sprites for: ScoreKeeper label, End Zones, self.ball, and Players"""
        self.score_keeper = pySprites.ScoreKeeper()
        self.ball = pySprites.Ball(self.screen)
        self.player1 = pySprites.Player(self.screen, 1)
        self.player1_endzone = pySprites.EndZone(self.screen, 1)
        self.player2 = pySprites.Player(self.screen, 2)
        self.player2_endzone = pySprites.EndZone(self.screen, 639)
        self.allSprites = pygame.sprite.Group(self.score_keeper,
                                         self.player1_endzone,
                                         self.player2_endzone,
                                         self.ball, self.player1, self.player2)

    def __load_music(self):
        """Load and loop background music if a file is present"""
        try:
            pygame.mixer.music.load("background.ogg")
            pygame.mixer.music.play(-1)
        except:
            pass

    def __loop(self):
        """GAME LOOP"""
        clock = pygame.time.Clock()
        self.__keep_going = True

        while self.__keep_going:
            clock.tick(30)
            self.__handle_events()
            self.__detect_collision()
            self.__refresh()

    def __handle_events(self):
        """Handle keyboard input for both players"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__keep_going = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player2.change_direction((0, 1))
                elif event.key == pygame.K_DOWN:
                    self.player2.change_direction((0, -1))
                elif event.key == pygame.K_w:
                    self.player1.change_direction((1, 1))
                elif event.key == pygame.K_s:
                    self.player1.change_direction((1, -1))
                elif event.key == pygame.K_ESCAPE:
                    self.__keep_going = False

    def __detect_collision(self):
        """Detect collisions between the ball, end zones, and players"""
        if self.ball.rect.colliderect(self.player2_endzone):
            self.score_keeper.player1_scored()
            self.ball.change_direction()

        if self.ball.rect.colliderect(self.player1_endzone):
            self.score_keeper.player2_scored()
            self.ball.change_direction()

        if self.score_keeper.winner():
            self.__keep_going = False

        if self.ball.rect.colliderect(self.player1.rect) or \
           self.ball.rect.colliderect(self.player2.rect):
            self.ball.change_direction()

    def __refresh(self):
        """Refresh the screen"""
        self.allSprites.clear(self.screen, self.background)
        self.allSprites.update()
        self.allSprites.draw(self.screen)
        pygame.display.flip()

Main()
