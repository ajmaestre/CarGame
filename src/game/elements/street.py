
import pygame
from utilities import colors
from ..settings import SCREEN_WIDTH, SCREEN_HEIGHT


# CLASE PARA DIBUJAR LA PISTA DONDE SE DESPLAZAN LOS CARROS
# ----------------------------------------------------------------------------------------------------
class Street:
    def __init__(self):
        self.color = colors.BLACK
        self.point_x = (SCREEN_WIDTH/2) - 120
        self.point_y = 0
        self.width = 250
        self.height = SCREEN_HEIGHT

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.point_x, self.point_y, self.width, self.height))