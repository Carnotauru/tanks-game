import pygame

class Obstacle2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/abstacle2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lives = 5

    def update(self, *args, **kwargs):
        if self.lives <= 0:
            self.kill()

class Obstacle1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/abstacle1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lives = 10

    def update(self, *args, **kwargs):
        if self.lives <= 0:
            self.kill()
