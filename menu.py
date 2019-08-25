import pygame
from pygame.locals import *


class Menu:
    def __init__(self):
        #self.start = pygame.image.load('racecar.png')
        pass

    def update(self, dt):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, (0,0,255), (200,150,100,50))