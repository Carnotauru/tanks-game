import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.images = (
            pygame.image.load('img/MediumExplosion1.png'),
            pygame.image.load('img/MediumExplosion2.png'),
            pygame.image.load('img/MediumExplosion3.png'),
        )
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame_update = 3

    def update(self):
        self.frame_update -= 1
        if self.frame_update == 0:
            self.frame_update = 3
            if self.image_index != 2:
                self.image_index += 1
                self.image = self.images[self.image_index]
            else:
                self.kill()