
import pygame
from ..settings import SCREEN_WIDTH, SCREEN_HEIGHT, CAR_WIDTH, CAR_HEIGHT


# ----------------------------------------------------------------------------------------------------
class Car:
    def __init__(self):
        self.image = pygame.image.load("assets/images/car-red-1.png")
        self.image = pygame.transform.scale(self.image, (CAR_WIDTH, CAR_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH/2) - 80
        self.rect.y = SCREEN_HEIGHT - 120

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > (SCREEN_WIDTH/2) - 90:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.x < (SCREEN_WIDTH/2) + 50:
            self.rect.x += 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)

