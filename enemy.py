import pygame as p

import tools
from tools import getRotetedImage, GAME_H, GAME_W
from random import randint, choice

class Enemy(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = p.image.load('img/Tank2.png')
        self.original_image = p.image.load('img/Tank2.png')
        self.speed = 4
        self.rect = self.image.get_rect()
        self.rect.y = 0
        if randint(1, 2) == 1:
            self.rect.x = 0
            self.angle = choice((180, -90))
        else:
            self.rect.x = GAME_W - self.image.get_width()
            self.angle = choice((180, 90))
        self.image, self.rect = getRotetedImage(self.original_image, self.rect, self.angle)
        self.move_time = randint(60, 150) # время движения
        self.shoot_time = randint(20, 35) # таймер стрельбы
        self.shooting = False # флаг стрельбы







    def update(self):
        # движение танка
        match self.angle:
            case 180:
                self.rect.y += self.speed
            case 90:
                self.rect.x -= self.speed
            case 0:
                self.rect.y -= self.speed
            case -90:
                self.rect.x += self.speed

        # границы игры
        if self.rect.top < 0:
            self.rect.top = 0
            self.rotate()
        if self.rect.left < 0:
            self.rect.left = 0
            self.rotate()
        if self.rect.bottom > GAME_H:
            self.rect.bottom = GAME_H
            self.rotate()
        if self.rect.right > GAME_W:
            self.rect.right = GAME_W
            self.rotate()

        # рандомный поворот танка
        self.move_time -= 1
        if self.move_time <= 0 and self.speed !=  0:
            self.rotate()
            self.move_time = randint(60, 100)

        # таймер стрельбы
        self.shoot_time -= 1
        if self.shoot_time == 0:
            self.shooting = True
            self.shoot_time = randint(20, 35)

    def rotate(self):
        self.angle = choice((-90, 0, 90, 180))
        self.image, self.rect = getRotetedImage(self.original_image, self.rect, self.angle)






















