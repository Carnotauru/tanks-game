import time

import pygame as p
import random
from tools import GAME_W, GAME_H

class PowerUp(p.sprite.Sprite):
    def __init__(self ):
        super().__init__()
        self.images = (
            p.transform.scale(p.image.load('img/img_2.png'), (35, 35)),
            p.transform.scale(p.image.load('img/img_3.png'), (35, 35)),
            p.transform.scale(p.image.load('img/img_4.png'), (35, 35))
        )
        self.image_index = random.randint(0, 2)
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, GAME_W - self.image.get_width())
        self.rect.y = random.randint(0, GAME_H - self.image.get_height())
        self.lifetime = 5
        self.createtime = time.time()


    def update(self, *args, **kwargs):
        if time.time() - self.createtime > self.lifetime:
            self.kill()
