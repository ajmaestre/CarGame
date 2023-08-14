
import pygame
from utilities import colors
from ..settings import SCREEN_WIDTH, SCREEN_HEIGHT, VELOCITY


# ----------------------------------------------------------------------------------------------------
class Line:
    def __init__(self, pos_y):
        self.color = colors.WHITE
        self.point_1 = (SCREEN_WIDTH/2)
        self.point_2 = pos_y
        self.point_3 = (SCREEN_WIDTH/2)
        self.point_4 = (SCREEN_HEIGHT/10) + pos_y

    def update(self):
        if self.point_2 < SCREEN_HEIGHT:
            self.point_2 += VELOCITY
            self.point_4 += VELOCITY
        else:
            self.point_2 = 0
            self.point_4 = SCREEN_HEIGHT/10

    def draw(self, screen):
        pygame.draw.line(screen, self.color, (self.point_1, self.point_2), (self.point_3, self.point_4), 10)
