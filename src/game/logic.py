import pygame, sys
from utilities import colors
from .elements.street import Street
from .elements.line import Line
from .elements.tree import Tree
from .elements.enemy import Enemy
from .elements.car import Car
from .elements.message import Message


class Logic():

    def __init__(self, screen):

        self.play = True
        self.treeList = []
        self.lineList = []
        self.screen = screen

        for line in range(3):
            self.lineList.append(Line(line*140))

        for tree in range(3):
            self.treeList.append(Tree(180, tree*140))
            self.treeList.append(Tree(-125, tree*140))

        for tree in range(2):
            self.treeList.append(Tree(280, tree*250, "assets/images/treePineSnow.png"))
            self.treeList.append(Tree(-225, tree*250, "assets/images/treePineSnow.png"))

        self.enemy = Enemy()
        self.street = Street()
        self.car = Car()
        self.message = Message()
        self.time_init = round(pygame.time.get_ticks()/1000)
        self.gameOverSound = pygame.mixer.Sound("assets/sounds/GameOver.mp3")
        pygame.mixer.music.load("assets/sounds/GoCart.mp3")
        pygame.mixer.music.play()


    def update(self):
        if self.play:
            pygame.mixer.music.unpause()
            self.car.update()
            for tree in self.treeList:
                tree.update()
            for line in self.lineList:
                line.update()
            self.time_actual = round(pygame.time.get_ticks()/1000)
            if not ((self.time_actual - self.time_init) % 20):
                self.enemy.aceleration = round((self.time_actual - self.time_init)/20)
            self.enemy.update()

            self.screen.fill(colors.GREEN)
            self.street.draw(self.screen)
            for line in self.lineList:
                line.draw(self.screen)
            for tree in self.treeList:
                tree.draw(self.screen)
            self.enemy.draw(self.screen)
            self.car.draw(self.screen)

            if self.enemy.rect.colliderect(self.car.rect):
                self.message.draw(self.screen)
                self.gameOverSound.play()
                pygame.mixer.music.stop()
                self.play = False

        else:
            pygame.mixer.music.pause()


