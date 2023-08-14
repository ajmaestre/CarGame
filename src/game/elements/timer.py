
import pygame
from utilities import colors


# ----------------------------------------------------------------------------------------------------
class Timer:
    def __init__(self):
        self.time_init = round(pygame.time.get_ticks()/1000)
        self.lv = 0
        self.font = pygame.font.Font(None, 30)
        self.timer = self.font.render("Timer: " + str(self.time_init), 0, colors.BLACK)
        self.level = self.font.render("Level: " + str(self.lv), 0, colors.RED)
        self.point_x = 10
        self.point_y = 14
        self.soundTimer = pygame.mixer.Sound("assets/sounds/Next.mp3")

    def update(self):
        self.time_actual = round(pygame.time.get_ticks()/1000)
        if not ((self.time_actual - self.time_init) % 20):
            self.soundTimer.play()
            self.lv = round((self.time_actual - self.time_init)/20)
        self.timer = self.font.render("Timer: " + str(self.time_actual - self.time_init), 0, colors.BLACK)
        self.level = self.font.render("Lv: " + str(self.lv), 0, colors.RED)
    
    def draw(self, screen):
        screen.blit(self.timer, (self.point_x, self.point_y))
        screen.blit(self.level, (self.point_x + 120, self.point_y))