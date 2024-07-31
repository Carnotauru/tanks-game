import pygame

GAME_W = 800
GAME_H = 600

# функция поворота картинки
def getRotetedImage(image, rect,  new_angle):
    new_image = pygame.transform.rotate(image, new_angle)
    new_rect = new_image.get_rect()
    new_rect.center = rect.center
    return new_image, new_rect

