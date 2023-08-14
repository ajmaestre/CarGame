
import pygame
from utilities import colors
from ..settings import SCREEN_WIDTH, SCREEN_HEIGHT


# CLASE QUE DIBUJA EL TEXTO DE GAME OVER QUE RESULTA AL PERDER EL JUEGO
# ----------------------------------------------------------------------------------------------------
class Message:
    def __init__(self):
        self.font = pygame.font.Font(None, 96)
        self.text = self.font.render("¡Game Over!", 0, colors.RED)
        self.point_x = (SCREEN_WIDTH/2) - 200
        self.point_y = (SCREEN_HEIGHT/2) - 50
    
    def draw(self, screen):
        screen.blit(self.text, (self.point_x, self.point_y))