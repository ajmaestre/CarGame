
import pygame, sys
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT
from .logic import Logic
from .states import GameState
from .elements.frame import Frame
from .elements.option import Option
from utilities import colors
from .elements.timer import Timer


class Game(GameState):
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        self.panel = Frame(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT/10, colors.GREEN_1)
        self.option_menu = Option("Menu", (SCREEN_WIDTH) - 100, 13, 24, colors.BLACK)
        self.option_pause = Option("Pause", (SCREEN_WIDTH) - 220, 13, 24, colors.BLACK)
        self.option_reset = Option("Reset", (SCREEN_WIDTH) - 340, 13, 24, colors.BLACK)
        self.btnMenu = Frame(SCREEN_WIDTH - 120, 7, SCREEN_WIDTH/6, SCREEN_HEIGHT/15, colors.BLUE)
        self.btnPaused = Frame(SCREEN_WIDTH - 240, 7, SCREEN_WIDTH/6, SCREEN_HEIGHT/15, colors.BLUE)
        self.btnReset = Frame(SCREEN_WIDTH - 360, 7, SCREEN_WIDTH/6, SCREEN_HEIGHT/15, colors.BLUE)
        self.timer = Timer()
        self.logic = Logic(self.screen)


    def menu(self):
        mx, my = pygame.mouse.get_pos()
        if self.btnMenu.presed(mx, my):
            if pygame.mouse.get_pressed()[0]:
                previous_state = self.return_to_previous_state()
                if previous_state:
                    previous_state.run()
        if self.btnPaused.presed(mx, my):
            if pygame.mouse.get_pressed()[0]:
                self.logic.play = False if self.logic.play else True
        if self.btnReset.presed(mx, my):
            if pygame.mouse.get_pressed()[0]:
                self.reset()

    
    def reset(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        self.panel = Frame(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT/10, colors.GREEN_1)
        self.option_menu = Option("Menu", (SCREEN_WIDTH) - 100, 13, 24, colors.BLACK)
        self.option_pause = Option("Pause", (SCREEN_WIDTH) - 220, 13, 24, colors.BLACK)
        self.option_reset = Option("Reset", (SCREEN_WIDTH) - 340, 13, 24, colors.BLACK)
        self.btnMenu = Frame(SCREEN_WIDTH - 120, 7, SCREEN_WIDTH/6, SCREEN_HEIGHT/15, colors.BLUE)
        self.btnPaused = Frame(SCREEN_WIDTH - 240, 7, SCREEN_WIDTH/6, SCREEN_HEIGHT/15, colors.BLUE)
        self.btnReset = Frame(SCREEN_WIDTH - 360, 7, SCREEN_WIDTH/6, SCREEN_HEIGHT/15, colors.BLUE)
        self.timer = Timer()
        self.logic = Logic(self.screen)


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.logic.update()
            if self.logic.play:
                self.timer.update()
            self.panel.draw(self.screen)
            self.btnMenu.draw(self.screen)
            self.btnPaused.draw(self.screen)
            self.btnReset.draw(self.screen)
            self.option_menu.draw(self.screen)
            self.option_pause.draw(self.screen)
            self.option_reset.draw(self.screen)
            self.timer.draw(self.screen)
            self.menu()
            pygame.display.flip()
            self.clock.tick(1000)
        previous_state = self.return_to_previous_state()
        if previous_state:
            previous_state.run()