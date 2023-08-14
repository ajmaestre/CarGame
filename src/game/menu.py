
import pygame, sys
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT
from .elements.option import Option
from .elements.frame import Frame
from game.screens import Game
from game.info import Info
from utilities import colors
from .states import GameState


class Menu(GameState):
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("My Game")
        self.background = Frame(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, colors.GREEN_2)
        self.frame = Frame(SCREEN_WIDTH/4, SCREEN_HEIGHT/4, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, colors.GREEN_1)

        self.option_1 = Option("Play Game", (SCREEN_WIDTH/3) + 10, (SCREEN_HEIGHT/3) + 15, 30, colors.BLACK)
        self.rect_1 = Frame(SCREEN_WIDTH/3, SCREEN_HEIGHT/3, SCREEN_WIDTH/3, SCREEN_HEIGHT/10, colors.BLUE)

        self.option_2 = Option("Info", (SCREEN_WIDTH/3) + 10, (SCREEN_HEIGHT/3) + 65, 30, colors.BLACK)
        self.rect_2 = Frame(SCREEN_WIDTH/3, (SCREEN_HEIGHT/3) + 50, SCREEN_WIDTH/3, SCREEN_HEIGHT/10, colors.BLUE)

        self.option_3 = Option("Exit", (SCREEN_WIDTH/3) + 10, (SCREEN_HEIGHT/3) + 115, 30, colors.BLACK)
        self.rect_3 = Frame(SCREEN_WIDTH/3, (SCREEN_HEIGHT/3) + 100, SCREEN_WIDTH/3, SCREEN_HEIGHT/10, colors.BLUE)


    def update(self):
        mx, my = pygame.mouse.get_pos()
        if self.rect_1.presed(mx, my):
            if pygame.mouse.get_pressed()[0]:
                self.game = Game()
                self.game.set_previous_state(self)
                self.game.run()
        if self.rect_2.presed(mx, my):
            if pygame.mouse.get_pressed()[0]:
                self.info = Info()
                self.info.set_previous_state(self)
                self.info.run()
        if self.rect_3.presed(mx, my):
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
            pygame.display.update()
            self.background.draw(self.screen)
            self.frame.draw(self.screen)
            self.rect_1.draw(self.screen)
            self.rect_2.draw(self.screen)
            self.rect_3.draw(self.screen)
            self.option_1.draw(self.screen)
            self.option_2.draw(self.screen)
            self.option_3.draw(self.screen)
            self.update()
