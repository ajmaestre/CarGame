
import pygame

# ----------------------------------------------------------------------------------------------------
class Frame:
    def __init__(self, x, y, w, h, color):
        self.color = color
        self.point_x = x
        self.point_y = y
        self.width = w
        self.height = h

    def presed(self, mx, my):
        if self.rect.collidepoint((mx, my)):
            return True
        return False

    def draw(self, screen):
        self.rect = pygame.draw.rect(screen, self.color, (self.point_x, self.point_y, self.width, self.height))