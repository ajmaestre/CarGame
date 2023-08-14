
import pygame
from ..settings import SCREEN_WIDTH, SCREEN_HEIGHT, VELOCITY


# CLASE PARA DIBUJAR LOS ARBOLES QUE ADORNAN EL JUEGO
# ----------------------------------------------------------------------------------------------------
class Tree:
    def __init__(self, pos_x, pos_y, image = "assets/images/tree.png"):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH/2) - pos_x
        self.rect.y = pos_y

    def update(self):
        if self.rect.y < SCREEN_HEIGHT:
            self.rect.y += VELOCITY
        else:
            self.rect.y = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
