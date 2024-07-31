import pygame as p
import tools


class Player(p.sprite.Sprite):
    #   функция констроуктор
    def __init__(self):
        super().__init__()
        self.original_image = p.image.load('img/Tank.png')
        self.image = p.image.load('img/Tank.png')
        self.rect = self.image.get_rect()
        self.rect.x = tools.GAME_W // 3
        self.rect.y = tools.GAME_H - self.image.get_height()
        self.rect.center = (self.rect.x, self.rect.y)
        self.angle  = 0 # текущий угол поворота танка
        self.new_angle = 0 # новый угол поворота танка
        self.speed = 5
        self.lives = 3

    def update(self, *args, **kwargs):
        # поворот танка

        if self.new_angle != self.angle:
            self.angle = self.new_angle
            self.image, self.rect = tools.getRotetedImage(self.original_image, self.rect, self.angle)
