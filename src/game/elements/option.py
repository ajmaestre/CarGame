
import pygame
from ..settings import SCREEN_WIDTH


# ----------------------------------------------------------------------------------------------------
class Option:
    def __init__(self, title, x, y, size, color):
        self.font = pygame.font.Font(None, size)
        self.text = self.font.render(title, 0, color)
        self.point_x = x
        self.point_y = y
    
    def draw(self, screen):
        screen.blit(self.text, (self.point_x, self.point_y))