
import pygame
from random import randint
from ..settings import SCREEN_WIDTH, SCREEN_HEIGHT, VELOCITY, CAR_WIDTH, CAR_HEIGHT


# ----------------------------------------------------------------------------------------------------
class Enemy:
    def __init__(self):
        self.image = pygame.image.load("assets/images/car-yellow-2.png")
        self.image = pygame.transform.scale(self.image, (CAR_WIDTH+10, CAR_HEIGHT+20))
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH/2) - 80
        self.rect.y = 0
        self.aceleration = 0

    def update(self):
        if self.rect.y < SCREEN_HEIGHT:
            self.rect.y += VELOCITY + self.aceleration
        else:
            car_number = randint(0,1)
            if car_number:
                carPosition = 80
            else:
                carPosition = -25
            self.rect.x = (SCREEN_WIDTH/2) - carPosition
            self.rect.y = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
