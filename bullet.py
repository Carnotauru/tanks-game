import pygame as p
from tools import getRotetedImage, GAME_W, GAME_H

class Bullet(p.sprite.Sprite):
    def __init__(self, center, angle):
        super().__init__()
        self.speed = 15
        self.angle = angle
        self.image = p.image.load('img/img.png')
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.image, self.rect = getRotetedImage(self.image, self.rect, angle)

    def update(self, *args, **kwargs):
        # движение снаряда
        if self.angle == 0:
            self.rect.y -= self.speed
            self.rect.x -= 0
        elif self.angle == 180:
            self.rect.y += self.speed
            self.rect.x += 0
        elif self.angle == 90:
            self.rect.x -= self.speed
            self.rect.y -= 0
        elif self.angle == -90:
            self.rect.x += self.speed
            self.rect.y += 0

        # уничтожаем пулю
        if self.rect.x < 0 or self.rect.x > GAME_W or \
            self.rect.y < 0 or self.rect.y > GAME_H:
            self.kill()
