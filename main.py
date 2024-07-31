import pygame as p
import time
import tools
from player import Player
from bullet import Bullet
from enemy import Enemy
from explosion import Explosion
from maps import Obstacle2, Obstacle1
from orel import Orel
from  powerUp import PowerUp

p.init()
p.mixer.init()

def menu():
    image = p.transform.scale(p.image.load('img/img_6.png'), (800, 600))
    image_rect = image.get_rect()

    btn_img = p.image.load('img/img_7.png')
    btn_rect = btn_img.get_rect()
    btn_rect.x = tools.GAME_W / 2 - btn_img.get_width() / 2
    btn_rect.y = tools.GAME_H / 2 - btn_img.get_height() / 2

    while True:
        screen.blit(image, image_rect)
        for event in p.event.get():
            if event.type == p.QUIT:
                quit()

        mouse_x, mouse_y = p.mouse.get_pos()
        mouse_click = p.mouse.get_pressed()


        if btn_rect.collidepoint(mouse_x, mouse_y):
            btn_scale = p.transform.scale(btn_img, (btn_img.get_width() + 10, btn_img.get_height() + 10))

        else:
            btn_scale = btn_img
        btn_rect = btn_scale.get_rect()
        btn_rect.x = tools.GAME_W / 2 - btn_scale.get_width() / 2
        btn_rect.y = tools.GAME_H / 2 - btn_scale.get_height() / 2

        #НАЖАТИЕ По кнопке
        if btn_rect.collidepoint(mouse_x, mouse_y) and mouse_click[0]:
            return



        screen.blit(btn_scale, btn_rect)
        p.display.update()




sound1 = p.mixer.Sound('img/sfx/break.wav')
sound1.set_volume(0.2)
sound2 = p.mixer.Sound('img/sfx/shot.wav')

sound3 = p.mixer.Sound('img/sfx/splash.wav')

sound4 = p.mixer.Sound('img/sfx/splash-heavy.wav')

sound5 = p.mixer.Sound('img/sfx/explosion-small.wav')

sound6 = p.mixer.Sound('img/sfx/powerup.wav')

fps = p.time.Clock()
screen = p.display.set_mode((tools.GAME_W, tools.GAME_H))
p.display.set_caption('Fighting tanks')

menu()

# создаем группы для спрайтов
all_group = p.sprite.Group()
enemy_group = p.sprite.Group()
plr_bullet_group = p.sprite.Group()
obstacle_group = p.sprite.Group()
bots_bullet_group = p.sprite.Group()
plr_group = p.sprite.Group()
powerUp_group = p.sprite.Group()




# рисуем жизни
def drawLives(count):
    img = p.transform.scale(p.image.load('img/img_2.png'), (35, 35))
    img_rect = img.get_rect()
    img_rect.y = 20
    img_rect.x = 20

    for i in range(count):
        img_rect.x += img.get_width() + 2
        screen.blit(img, img_rect)


def clearMap():
    all_group.empty()
    enemy_group.empty()
    plr_bullet_group.empty()
    obstacle_group.empty()
    bots_bullet_group.empty()


# рисуем карты
def base():
    block = Obstacle2(0, 0)
    block.rect.x = tools.GAME_W // 2 - block.image.get_width()
    block.rect.y = tools.GAME_H - block.image.get_height()
    obstacle_group.add(block)
    all_group.add(block)

    block = Obstacle2(0, 0)
    block.rect.x = tools.GAME_W // 2 - block.image.get_width()
    block.rect.y = tools.GAME_H - 88
    obstacle_group.add(block)
    all_group.add(block)

    block = Obstacle2(0, 0)
    block.rect.x = tools.GAME_W // 2
    block.rect.y = tools.GAME_H - 88
    obstacle_group.add(block)
    all_group.add(block)

    block = Obstacle2(0, 0)
    block.rect.x = tools.GAME_W // 2 + 55
    block.rect.y = tools.GAME_H - 88
    obstacle_group.add(block)
    all_group.add(block)

    block = Obstacle2(0, 0)
    block.rect.x = tools.GAME_W // 2 + 55
    block.rect.y = tools.GAME_H - 44
    obstacle_group.add(block)
    all_group.add(block)

    # орел
    orel = Orel()
    all_group.add(orel)


base()


def map1():
    x = 60
    for i in range(6):
        y = 100
        for i in range(6):
            block = Obstacle2(x, y)
            all_group.add(block)
            obstacle_group.add(block)
            y += block.image.get_height()
        x += 125


def map2():
    x = 60
    for i in range(6):
        y = 100
        for i in range(3):
            block = Obstacle2(x, y)
            all_group.add(block)
            obstacle_group.add(block)
            y += 110
        x += 125

        block = Obstacle2(0, 0)
        block.rect.x = 100
        block.rect.y = tools.GAME_H - 160
        obstacle_group.add(block)
        all_group.add(block)

        block = Obstacle2(0, 0)
        block.rect.x = 155
        block.rect.y = tools.GAME_H - 160
        obstacle_group.add(block)
        all_group.add(block)


def map3():
    block = Obstacle2(0, 0)
    block.rect.x = tools.GAME_W // 2 - block.image.get_width()
    block.rect.y = tools.GAME_H - 1
    obstacle_group.add(block)
    all_group.add(block)

    x = 60
    for i in range(4):
        y = 100
        for i in range(3):
            block = Obstacle2(x, y)
            all_group.add(block)
            obstacle_group.add(block)
            y += block.image.get_height()
        x += 125

        block = Obstacle2(0, 0)
        block.rect.x = 100
        block.rect.y = tools.GAME_H - 160
        obstacle_group.add(block)
        all_group.add(block)

        block = Obstacle2(0, 0)
        block.rect.x = 155
        block.rect.y = tools.GAME_H - 160
        obstacle_group.add(block)
        all_group.add(block)

        block = Obstacle2(0, 0)
        block.rect.x = 600
        block.rect.y = tools.GAME_H - 160
        obstacle_group.add(block)
        all_group.add(block)

        block = Obstacle2(0, 0)
        block.rect.x = 655
        block.rect.y = tools.GAME_H - 160
        obstacle_group.add(block)
        all_group.add(block)

        block = Obstacle2(0, 0)
        block.rect.x = 600
        block.rect.y = tools.GAME_H - 500
        obstacle_group.add(block)
        all_group.add(block)

        block = Obstacle2(0, 0)
        block.rect.x = 655
        block.rect.y = tools.GAME_H - 500
        obstacle_group.add(block)
        all_group.add(block)

        block = Obstacle2(0, 0)
        block.rect.x = 400
        block.rect.y = tools.GAME_H - 260
        obstacle_group.add(block)
        all_group.add(block)

        block = Obstacle2(0, 0)
        block.rect.x = 455
        block.rect.y = tools.GAME_H - 260
        obstacle_group.add(block)
        all_group.add(block)

        block = Obstacle2(0, 0)
        block.rect.x = 300
        block.rect.y = tools.GAME_H - 260
        obstacle_group.add(block)
        all_group.add(block)

        block = Obstacle2(0, 0)
        block.rect.x = 355
        block.rect.y = tools.GAME_H - 260
        obstacle_group.add(block)
        all_group.add(block)


def map4():
    block = Obstacle2(0, 0)
    block.rect.x = tools.GAME_W // 2 - block.image.get_width()
    block.rect.y = tools.GAME_H - 1
    obstacle_group.add(block)
    all_group.add(block)

    block = Obstacle1(0, 0)
    block.rect.x = tools.GAME_W - 500
    block.rect.y = tools.GAME_H - 200
    obstacle_group.add(block)
    all_group.add(block)

    block = Obstacle1(0, 0)
    block.rect.x = tools.GAME_W - 450
    block.rect.y = tools.GAME_H - 200
    obstacle_group.add(block)
    all_group.add(block)

    block = Obstacle1(0, 0)
    block.rect.x = tools.GAME_W - 400
    block.rect.y = tools.GAME_H - 200
    obstacle_group.add(block)
    all_group.add(block)

    block = Obstacle1(0, 0)
    block.rect.x = tools.GAME_W - 350
    block.rect.y = tools.GAME_H - 200
    obstacle_group.add(block)
    all_group.add(block)

    block = Obstacle1(0, 0)
    block.rect.x = tools.GAME_W - 350
    block.rect.y = tools.GAME_H - 244
    obstacle_group.add(block)
    all_group.add(block)

    block = Obstacle1(0, 0)
    block.rect.x = tools.GAME_W - 500
    block.rect.y = tools.GAME_H - 244
    obstacle_group.add(block)
    all_group.add(block)

    block = Obstacle1(0, 0)
    block.rect.x = tools.GAME_W - 425
    block.rect.y = tools.GAME_H - 400
    obstacle_group.add(block)
    all_group.add(block)

    block = Obstacle2(0, 0)
    block.rect.x = tools.GAME_W - 425
    block.rect.y = tools.GAME_H - 600
    obstacle_group.add(block)
    all_group.add(block)

    block = Obstacle2(0, 0)
    block.rect.x = tools.GAME_W - 475
    block.rect.y = tools.GAME_H - 600
    obstacle_group.add(block)
    all_group.add(block)

    block = Obstacle2(0, 0)
    block.rect.x = tools.GAME_W - 375
    block.rect.y = tools.GAME_H - 600
    obstacle_group.add(block)
    all_group.add(block)

    x = 60
    for i in range(2):
        y = 100
        for i in range(3):
            block = Obstacle2(x, y)
            all_group.add(block)
            obstacle_group.add(block)
            y += block.image.get_height()
        x += 125

    x = 550
    for i in range(2):
        y = 100
        for i in range(3):
            block = Obstacle2(x, y)
            all_group.add(block)
            obstacle_group.add(block)
            y += block.image.get_height()
        x += 125

def clearGame():
    current_map = 0
    clearMap()
    maps[current_map]()
    base()
    plr.lives = 3
    plr.rect.x = 200
    plr.rect.y = 500
    plr.new_angle = 0
    all_group.add(plr)


# список карт
maps = [map1, map2, map3, map4]
current_map = 0
maps[current_map]()
base()
start_time = time.time()  # запоминаем время старта карты



plr = Player()
plr_group.add(plr)

all_group.add(plr)

# орел
orel = Orel()
all_group.add(orel)

running = True
enemy_timer = 30  # spawn таймер врагов
bullet_time = 20  # перезарядка игрока
powerUp_time = time.time()
stop_time = time.time()
speed_time = time.time()
while running:
    #stop time bots
    if time.time() - stop_time > 10:
        for bot in enemy_group:
            bot.speed = 5

    # speed time player
    if time.time() - speed_time > 10:
        plr.speed = 5

    # powerUp
    if time.time() - powerUp_time > 10:
        pw = PowerUp()
        all_group.add(pw)
        powerUp_group.add(pw)
        powerUp_time = time.time()

    # смена карт
    if time.time() - start_time >= 180:
        current_map = (current_map + 1) % len(maps)
        clearMap()
        maps[current_map]()
        base()
        plr = Player()
        all_group.add(plr)
        enemy_timer = 30
        start_time = time.time()  # запоминаем время старта карты

    for ev in p.event.get():
        if ev.type == p.QUIT:
            running = False
    screen.fill('black')

    # создание врагов
    enemy_timer -= 1
    if enemy_timer <= 0 and len(enemy_group.sprites()) < 1:
        bot = Enemy()
        all_group.add(bot)
        enemy_group.add(bot)
        enemy_timer = 30

    # стрельба врагов
    for current_enemy in enemy_group:
        if current_enemy.shooting and current_enemy.speed != 0:
            enemy_bullet = Bullet(current_enemy.rect.center, current_enemy.angle)
            all_group.add(enemy_bullet)
            bots_bullet_group.add(enemy_bullet)
            current_enemy.shooting = False

    # поворот танка
    keys = p.key.get_pressed()
    if keys[p.K_w]:
        plr.new_angle = 0
        if plr.rect.top > 0:
            plr.rect.y -= plr.speed
    elif keys[p.K_d]:
        plr.new_angle = -90
        if plr.rect.right < tools.GAME_W:
            plr.rect.x += plr.speed
    elif keys[p.K_s]:
        plr.new_angle = 180
        if plr.rect.bottom < tools.GAME_H:
            plr.rect.y += plr.speed
    elif keys[p.K_a]:
        plr.new_angle = 90
        if plr.rect.left > 0:
            plr.rect.x -= plr.speed

    # проверка на столкновение игрока с препятствием
    hit = p.sprite.spritecollide(plr, all_group, False)
    for obstacle in hit:
        if isinstance(obstacle, Obstacle2) or isinstance(obstacle, Obstacle1):
            # откатываем перемещение игрока
            if plr.new_angle == 0:
                plr.rect.y += plr.speed
            elif plr.new_angle == -90:
                plr.rect.x -= plr.speed
            elif plr.new_angle == 90:
                plr.rect.x += plr.speed
            elif plr.new_angle == 180:
                plr.rect.y -= plr.speed
        break

    # проверка на столкновение врага с препятствием
    for b in enemy_group:
        hit = p.sprite.spritecollide(b, all_group, False)
        for obstacle in hit:
            if isinstance(obstacle, Obstacle2):
                # откатываем перемещение игрока
                if b.angle == 0:
                    b.rect.y += b.speed
                elif b.angle == -90:
                    b.rect.x -= b.speed
                elif b.angle == 90:
                    b.rect.x += b.speed
                elif b.angle == 180:
                    b.rect.y -= b.speed
                b.rotate()
            break

    # стрельба игрока
    bullet_time -= 1
    if keys[p.K_SPACE] and bullet_time <= 0:
        sound2.play()
        plr_bullet = Bullet(plr.rect.center, plr.new_angle)
        all_group.add(plr_bullet)
        plr_bullet_group.add(plr_bullet)
        bullet_time = 20

    # столкновение пуль игрока с врагом
    for bull in plr_bullet_group:
        hit = p.sprite.spritecollide(bull, enemy_group, True)
        if hit:
            sound3.play()
            plr_bullet_group.remove(bull)
            all_group.remove(bull)
            for tank in hit:
                expl = Explosion(tank.rect.center)
                all_group.add(expl)
                enemy_group.remove(tank)
                all_group.remove(tank)

    # попадание по игроку
    for bul in bots_bullet_group:
        hit = p.sprite.spritecollide(bul, plr_group, False)
        if hit:
            bots_bullet_group.remove(bul)
            all_group.remove(bul)
            plr.lives -= 1
            sound4.play()
            if plr.lives == 0:
                menu()
                start_time = time.time()
                clearGame()

    # стрельба по блокам
    for bul in plr_bullet_group:
        hit = p.sprite.spritecollide(bul, all_group, False)
        for h in hit:
            if isinstance(h, Obstacle2):
                bul.kill()
                sound1.play()
                h.lives -= 1
            if isinstance(h, Obstacle1):
                bul.kill()
                sound1.play()
                h.lives -= 1

    # стрельба врагов по блокам
    for bul in bots_bullet_group:
        hit = p.sprite.spritecollide(bul, all_group, False)
        for h in hit:
            if isinstance(h, Obstacle2):
                bul.kill()
                sound1.play()
                h.lives -= 1
            if isinstance(h, Obstacle1):
                bul.kill()
                sound1.play()
                h.lives -= 1

    # поподание по орлу
    hit = p.sprite.spritecollide(orel, all_group, False)
    for h in hit:
        if isinstance(h, Bullet):
            sound5.play()
            time.sleep(1)
            menu()
            start_time = time.time()
            clearGame()

    # столкновение с powerUp
    hit = p.sprite.spritecollide(plr, powerUp_group, True)
    for h in hit:
        sound6.play()
        if h.image_index == 0:
            plr.lives = 3
        elif h.image_index == 1:
            for bot in enemy_group:
                bot.speed = 0
                stop_time = time.time()
        elif h.image_index == 2:
            plr.speed = 10
            speed_time = time.time()


    all_group.update()
    all_group.draw(screen)
    drawLives(plr.lives)

    p.display.flip()
    fps.tick(35)
