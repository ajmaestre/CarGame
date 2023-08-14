import pygame, sys
from game.menu import Menu


if __name__ == "__main__":
    pygame.init()
    menu = Menu()
    menu.run()
    pygame.quit()