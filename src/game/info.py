
import pygame, sys
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT
from .elements.option import Option
from .elements.frame import Frame
from utilities import colors
from .states import GameState


class Info(GameState):
    def __init__(self):
        self.text = 'Este es un emocionante juego desarrollado \n en Pygame que ofrece a los jugadores una \n experiencia llena de adrenalina al \n sumergirse en una intensa competencia \n de choques de carros. \n Los jugadores toman el volante de un \n carro en una arena llena de acción, \n donde deben esquivar los automóviles \n que pueden salir de cualquiera \n de los dos carriles presentes.'
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("My Game")
        self.background = Frame(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, colors.GREEN_2)
        self.option_menu = Option("Menu", (SCREEN_WIDTH) - 100, 13, 24, colors.BLACK)
        self.btnMenu = Frame(SCREEN_WIDTH - 120, 7, SCREEN_WIDTH/6, SCREEN_HEIGHT/15, colors.BLUE)
        self.frame = Frame(SCREEN_WIDTH*1/5, SCREEN_HEIGHT*1/5, SCREEN_WIDTH*3/5, SCREEN_HEIGHT*3/5, colors.GREEN_1)


    def menu(self):
        mx, my = pygame.mouse.get_pos()
        if self.btnMenu.presed(mx, my):
            if pygame.mouse.get_pressed()[0]:
                previous_state = self.return_to_previous_state()
                if previous_state:
                    previous_state.run()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
            pygame.display.update()
            self.background.draw(self.screen)
            self.btnMenu.draw(self.screen)
            self.option_menu.draw(self.screen)
            self.frame.draw(self.screen)
            line_index = 30
            for line in self.text.split('\n'):
                self.information = Option(line, (SCREEN_WIDTH*1/5) + 10, (SCREEN_HEIGHT*1/5) + line_index, 24, colors.BLACK)
                line_index += 20
                self.information.draw(self.screen)
            self.menu()
