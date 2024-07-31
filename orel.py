import pygame
import tools

class Orel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/Orel.png')
        self.rect = self.image.get_rect()
        self.rect.center = (tools.GAME_W - 373, tools.GAME_H - 25)
        self.lives = 1
