import pygame

from settings import *

class Grass(pygame.sprite.Sprite):
    def __init__(self,pos, groups) -> None:
        super().__init__(groups)
        self.image = pygame.image.load('grass_1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

