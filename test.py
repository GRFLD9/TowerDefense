import math
import os
import sys

import pygame
from pygame import image


def choose_map_matrix(number):
    if number == 1:
        return [['g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
                ['g', '2', 't', 'g', 'g', 'g', 'g', 'g', 'h', 'g', 'g', 'g', 'g'],
                ['g', '3', 'g', 'g', 'g', 't', 'g', 'g', '38', 'g', 'g', 'g', 'g'],
                ['t', '4', 'g', 'g', '33', '34', '35', '36', '37', 't', 'g', 'g', 'g'],
                ['g', '5', 'g', 'g', '32', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
                ['g', '6', 'g', 'g', '31', 't', 'g', 'g', 't', 'g', 'g', 'g', 'g'],
                ['g', '7', 't', 'g', '30', '29', '28', '27', '26', '25', '24', '23', 'g'],
                ['t', '8', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 't', '22', 'g'],
                ['g', '9', 't', 'g', 'g', 't', 'g', 'g', 't', 'g', 'g', '21', 'g'],
                ['g', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 'g']]
    elif number == 2:
        return [['g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
                ['g', '2', 'g', 'g', '9', '10', '11', '12', '13', '14', '15', '16', 'g'],
                ['g', '3', 'g', 'g', '8', 'g', 'g', 'g', 'g', 'g', 'g', '17', 'g'],
                ['g', '4', '5', '6', '7', 'g', 'g', 'g', 'g', 'g', 'g', '18', 'g'],
                ['g', 'g', 'g', 'g', 'g', 'g', '30', '29', '28', 'g', 'g', '19', 'g'],
                ['g', 'g', 'g', 'g', '33', '32', '31', 'g', '27', 'g', 'g', '20', 'g'],
                ['g', 'g', 'g', 'g', '34', 'g', 'g', 'g', '26', 'g', 'g', '21', 'g'],
                ['g', 'g', 'g', 'g', '35', 'g', 'g', 'g', '25', '24', '23', '22', 'g'],
                ['g', 'h', '38', '37', '36', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
                ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']]
    elif number == 3:
        return [['g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
                ['g', '2', 't', 'g', 'g', 'g', 'g', 'h', 'g', 'g', 'g', 'g', 'g'],
                ['g', '3', '4', '5', '6', 'g', 'g', '35', 'g', 'g', 't', 'g', 'g'],
                ['g', 't', 'g', 'g', '7', 't', 'g', '34', '33', '32', '31', '30', 'g'],
                ['g', 'g', 't', 'g', '8', 'g', 'g', 'g', 'g', 't', 'g', '29', 't'],
                ['g', '12', '11', '10', '9', 'g', 'g', 'g', '25', '26', '27', '28', 'g'],
                ['g', '13', 't', 'g', 'g', 'g', 'g', 'g', '24', 't', 'g', 'g', 'g'],
                ['t', '14', 'g', 'g', 't', 'g', 'g', 't', '23', 'g', 'g', 'g', 'g'],
                ['g', '15', '16', '17', '18', '19', '20', '21', '22', 'g', 'g', 'g', 'g'],
                ['g', 'g', 'g', 't', 'g', 'g', 't', 'g', 'g', 'g', 'g', 'g', 'g']]
    elif number == 4:
        return [['g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 't', 'g', 'g', 'g', 'g'],
                ['g', '2', 't', 'g', 'g', 'g', '25', '26', '27', '28', '29', 'g', 'g'],
                ['g', '3', '4', '5', 'g', 'g', '24', 't', 'g', 't', '30', 'g', 'g'],
                ['g', 'g', 't', '6', 'g', 't', '23', 'g', 'g', 'g', '31', 't', 'g'],
                ['g', 'g', 'g', '7', 't', 'g', '22', 'g', 'g', 't', '32', 'g', 'g'],
                ['g', '10', '9', '8', 'g', 'g', '21', 'g', 'g', 'g', '33', 't', 'g'],
                ['g', '11', 't', 'g', 'g', 'g', '20', 'g', 'g', 'g', '34', 'g', 'g'],
                ['t', '12', 'g', 'g', 'g', 't', '19', 'g', 'g', 'g', '35', 'g', 'g'],
                ['g', '13', '14', '15', '16', '17', '18', 'g', 'g', 'g', 'h', 'g', 'g'],
                ['g', 'g', 'g', 't', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']]
    elif number == 5:
        return [['g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
                ['t', '2', 't', 'g', 'g', 'g', 't', 'g', 't', 'g', 'g', 'g', 'g'],
                ['g', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'g', 'g'],
                ['g', 'g', 'g', 'g', 't', 'g', 'g', 't', 'g', 't', '13', 'g', 'g'],
                ['g', 'g', 't', 'g', 'g', 'g', 't', 'g', 'g', 'g', '14', 't', 'g'],
                ['g', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', 'g', 'g'],
                ['g', '25', 't', 'g', 't', 'g', 'g', 't', 'g', 't', 'g', 'g', 'g'],
                ['g', '26', 'g', 't', '31', '32', '33', '34', 't', 'g', 'g', 'g', 'g'],
                ['g', '27', '28', '29', '30', 'g', 't', '35', '36', '37', '38', 'h', 'g'],
                ['g', 'g', 't', 'g', 'g', 'g', 'g', 'g', 'g', 't', 'g', 'g', 'g']]


pygame.init()

FPS = 12
WIDTH = 1040
HEIGHT = 800
clock = pygame.time.Clock()

map_sprites = pygame.sprite.Group()
map_photo = pygame.sprite.Sprite()
font = pygame.font.Font(None, 38)

TOWER_Y_OFFSET = 40
RADIUS_Y_OFFSET = 20

upgrade_costs = [0, 10, 30, 50, 80]


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def get_arrow_image(arrow_images, start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    angle = math.degrees(math.atan2(dx, -dy))
    index = abs(int(angle / 7))
    if index >= 13:
        index = 13 - index
    im = arrow_images[index]
    if dx < 0:
        im = pygame.transform.flip(im, True, False)
    if dy > 0:
        im = pygame.transform.flip(im, False, True)
    width, height = im.get_size()
    im = pygame.transform.scale(im, (width + 5, height + 5))
    return im, dx, dy


def load_arrow_images():
    arrow_images = []
    for i in range(1, 14):
        image = load_image(f"Units/Arrow/{i}.png")
        arrow_images.append(image)
    return arrow_images


def load_stone_image():
    im = load_image("Units/Stone.png")
    width, height = im.get_size()
    return pygame.transform.scale(im, (width - 120, height - 120))


def load_lightning_image():
    im = load_image("Units/Lightning.png")
    width, height = im.get_size()
    return pygame.transform.scale(im, (width, height))


def get_cell_center(cell_x, cell_y):
    cell_width = WIDTH // len(map_matrix[0])
    cell_height = HEIGHT // len(map_matrix)

    center_x = cell_x * cell_width + cell_width // 2
    center_y = cell_y * cell_height + cell_height // 2 - TOWER_Y_OFFSET

    return center_x, center_y


class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, arrow_images, tower_type):
        super().__init__()
        self.level = 0
        self.images = self.load_upgrade_images(tower_type)
        self.image = self.images[self.level]
        self.rect = self.image.get_rect(center=(x, y))
        self.radius = radius
        self.placed = False
        self.target = None
        self.arrow_images = arrow_images
        self.tower_type = tower_type
        self.last_shot_time = 0
        self.shoot_delay = 500
        self.shoot_speed = 50

    def load_upgrade_images(self, tower_type):
        images = []
        if tower_type == 'Upgrade_arrow_tower':
            for i in range(1, 6):
                image = pygame.transform.scale(load_image(f"Towers/{tower_type}/{i}.png"), (100, 160))
                images.append(image)
        elif tower_type == 'Upgrade_stone_tower':
            for i in range(1, 4):
                image = load_image(f"Towers/{tower_type}/{i}.png")
                images.append(image)
        elif tower_type == 'Upgrade_electric_tower':
            for i in range(1, 4):
                image = load_image(f"Towers/{tower_type}/{i}.png")
                images.append(image)
        return images

    def upgrade(self, player):
        if self.level < len(self.images) - 1:
            cost = upgrade_costs[self.level + 1]
            if player.coins >= cost:
                player.coins -= cost
                self.level += 1
                self.image = self.images[self.level]
                self.shoot_delay = max(100, self.shoot_delay - 100)
                self.shoot_speed += 2

    def update(self, mobs, bullet_group):
        if self.placed:
            if not self.target:
                for mob in mobs:
                    distance = math.hypot(self.rect.centerx - mob.rect.centerx, self.rect.centery - mob.rect.centery)
                    if distance <= self.radius:
                        self.target = mob
                        break

            if self.target:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_shot_time > self.shoot_delay:
                    self.shoot(bullet_group)
                    self.last_shot_time = current_time
                distance = math.hypot(self.rect.centerx - self.target.rect.centerx,
                                      self.rect.centery - self.target.rect.centery)
                if distance > self.radius:
                    self.target = None

    def shoot(self, bullet_group):
        if self.target:
            if self.tower_type == 'Upgrade_stone_tower':
                bullet = Bullet(self.rect.center, self.target.rect.center, self.arrow_images, is_stone=True)
            elif self.tower_type == 'Upgrade_electric_tower':
                bullet = Bullet(self.rect.center, self.target.rect.center, self.arrow_images, is_lightning=True)
            else:
                bullet = Bullet(self.rect.center, self.target.rect.center, self.arrow_images)
            bullet.speed = self.shoot_speed
            bullet_group.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos, arrow_images, is_stone=False, is_lightning=False):
        super().__init__()
        self.start_pos = start_pos
        self.target_pos = target_pos
        self.arrow_images = arrow_images
        self.is_stone = is_stone
        self.is_lightning = is_lightning

        if self.is_stone:
            self.image = load_stone_image()
        elif self.is_lightning:
            self.image = load_lightning_image()
        else:
            self.image, dx, dy = get_arrow_image(self.arrow_images, start_pos, target_pos)

        self.rect = self.image.get_rect(center=start_pos)
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = 50
        if not self.is_stone and not self.is_lightning:
            self.direction = (dx / math.hypot(dx, dy), dy / math.hypot(dx, dy))
        else:
            dx = target_pos[0] - start_pos[0]
            dy = target_pos[1] - start_pos[1]
            self.direction = (dx / math.hypot(dx, dy), dy / math.hypot(dx, dy))

    def update(self):
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed

        if not pygame.Rect(0, 0, WIDTH, HEIGHT).colliderect(self.rect):
            self.kill()


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(map_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.pos_x = 80
        self.pos_y = -40

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(70, -50, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Mob(AnimatedSprite):
    def __init__(self, image_path, columns, rows, x, y, speed, health):
        super().__init__(load_image(image_path), columns, rows, x, y)
        self.speed = speed
        self.x = 1  # позиция моба в матрице по х
        self.y = 0  # позиция моба в матрице по y
        self.last_y = self.rect.y  # последняя позиция по y на прошлой клетке
        self.last_x = self.rect.x  # последняя позиция по х на прошлой клетке
        self.count = 1  # клетка на которой стоит моб
        self.spawn_time = pygame.time.get_ticks()  # время спавна
        self.spawn_delay = 2000  # задержка спавна в миллисекундах
        self.health = health
        self.killed = False
        self.is_damaged = False
        self.damage_time = 0
        self.damage_duration = 500

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time < self.spawn_delay:
            return

        if self.is_damaged and current_time - self.damage_time < self.damage_duration:
            self.damaged_image.update()
            self.image = self.damaged_image.image
        else:
            self.is_damaged = False
            super().update()

        if not self.killed:
            self.move()

    def move(self):
        if self.y >= 0 and self.y < len(map_matrix) - 1:
            if map_matrix[self.y + 1][self.x].isdigit() and self.count + 1 == int(map_matrix[self.y + 1][self.x]):
                self.rect.y += self.speed
                if self.rect.y == self.last_y + 80:
                    self.y += 1
                    self.last_y = self.rect.y
                    self.count += 1
        if self.y <= len(map_matrix) - 1:
            if map_matrix[self.y - 1][self.x].isdigit() and self.count + 1 == int(map_matrix[self.y - 1][self.x]):
                self.rect.y -= self.speed
                if self.rect.y == self.last_y - 80:
                    self.y -= 1
                    self.last_y = self.rect.y
                    self.count += 1
        if self.x >= 0 and self.x < len(map_matrix[self.y]):
            if map_matrix[self.y][self.x + 1].isdigit() and self.count + 1 == int(map_matrix[self.y][self.x + 1]):
                self.rect.x += self.speed
                if self.rect.x == self.last_x + 80:
                    self.x += 1
                    self.last_x = self.rect.x
                    self.count += 1
            if map_matrix[self.y][self.x - 1].isdigit() and self.count + 1 == int(map_matrix[self.y][self.x - 1]):
                self.rect.x -= self.speed
                if self.rect.x == self.last_x - 80:
                    self.x -= 1
                    self.last_x = self.rect.x
                    self.count += 1

    def take_damage(self, damage):
        self.health -= damage
        self.is_damaged = True
        self.damage_time = pygame.time.get_ticks()

        if self.health <= 0:
            self.killed = True


class Skeleton(Mob):
    def __init__(self):
        super().__init__(
            image_path="mobs/skelets.png",  # Путь к изображению скелета
            columns=6,  # Количество колонок в спрайтшите
            rows=2,  # Количество строк в спрайтшите
            x=37,  # Начальная позиция по x
            y=50,  # Начальная позиция по y
            speed=5,  # Скорость скелета
            health=100  # Здоровье скелета
        )
        self.damaged_image = AnimatedSprite(load_image('mobs/skelets_damaged.png'), 6, 2, 37, 50)


class Ogre(Mob):
    def __init__(self):
        super().__init__(
            image_path="mobs/ogre.png",  # Путь к изображению огра
            columns=6,  # Количество колонок в спрайтшите
            rows=2,  # Количество строк в спрайтшите
            x=37,  # Начальная позиция по x
            y=50,  # Начальная позиция по y
            speed=5,  # Скорость огра (медленнее, чем у скелета)
            health=200  # Здоровье огра (больше, чем у скелета)
        )
        self.damaged_image = AnimatedSprite(load_image('mobs/ogre_damaged.png'), 6, 2, 37, 50)


class Minotaur(Mob):
    def __init__(self):
        super().__init__(
            image_path="mobs/minotaur.png",  # Путь к изображению огра
            columns=6,  # Количество колонок в спрайтшите
            rows=2,  # Количество строк в спрайтшите
            x=37,  # Начальная позиция по x
            y=50,  # Начальная позиция по y
            speed=5,  # Скорость огра (медленнее, чем у скелета)
            health=300  # Здоровье огра (больше, чем у скелета)
        )
        self.damaged_image = AnimatedSprite(load_image('mobs/minotaur_damaged.png'), 6, 2, 37, 50)


class Zombie(Mob):
    def __init__(self):
        super().__init__(
            image_path="mobs/zombies.png",  # Путь к изображению огра
            columns=6,  # Количество колонок в спрайтшите
            rows=2,  # Количество строк в спрайтшите
            x=37,  # Начальная позиция по x
            y=50,  # Начальная позиция по y
            speed=5,  # Скорость огра (медленнее, чем у скелета)
            health=250  # Здоровье огра (больше, чем у скелета)
        )
        self.damaged_image = AnimatedSprite(load_image('mobs/zombies_damaged.png'), 6, 2, 37, 50)


class Golem(Mob):
    def __init__(self):
        super().__init__(
            image_path="mobs/golem.png",  # Путь к изображению огра
            columns=6,  # Количество колонок в спрайтшите
            rows=2,  # Количество строк в спрайтшите
            x=37,  # Начальная позиция по x
            y=50,  # Начальная позиция по y
            speed=5,  # Скорость огра (медленнее, чем у скелета)
            health=400  # Здоровье огра (больше, чем у скелета)
        )
        self.damaged_image = AnimatedSprite(load_image('mobs/golem_damaged.png'), 6, 2, 37, 50)


def start_screen():
    size = 1200, 630
    screen = pygame.display.set_mode(size)

    fon = pygame.transform.scale(load_image('mm.png'), size)
    screen.blit(fon, (0, 0))

    exit_x, exit_y = [i for i in range(272, 482)], [i for i in range(348, 534)]
    play_x, play_y = [i for i in range(701, 900)], [i for i in range(360, 530)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if pos[0] in exit_x and pos[1] in exit_y:
                    terminate()
                if pos[0] in play_x and pos[1] in play_y:
                    return

        pygame.display.flip()


def place_tower(mouse_x, mouse_y):
    cell_width = WIDTH // len(map_matrix[0])
    cell_height = HEIGHT // len(map_matrix)

    cell_x = mouse_x // cell_width
    cell_y = (mouse_y + TOWER_Y_OFFSET) // cell_height

    if 0 <= cell_y < len(map_matrix) and 0 <= cell_x < len(map_matrix[0]):
        if map_matrix[cell_y][cell_x] == 't':
            map_matrix[cell_y][cell_x] = 'T'
            center_x, center_y = get_cell_center(cell_x, cell_y)
            return center_x, center_y
    return None


def draw_pause_menu(screen, font):
    overlay = pygame.Surface((WIDTH + 200, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 170))
    screen.blit(overlay, (0, 0))

    pause_font = pygame.font.Font(None, 150)
    pause_text = pause_font.render("PAUSE", True, (255, 255, 255))
    pause_rect = pause_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(pause_text, pause_rect)

    screen.blit(exit_button_image, (WIDTH // 2 - 210, HEIGHT // 2))
    text = font.render("Main menu", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - 235, HEIGHT // 2 + 90))

    screen.blit(play_button_image, (WIDTH // 2 - 50, HEIGHT // 2))
    text = font.render("Continue", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - 55, HEIGHT // 2 + 110))

    screen.blit(settings_button_image, (WIDTH // 2 + 130, HEIGHT // 2))
    text = font.render("Settings", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 + 120, HEIGHT // 2 + 90))


class LevelSelector:
    def load_image(name):
        size = 1200, 630
        screen = pygame.display.set_mode(size)

        fon = pygame.transform.scale(load_image('Level Selector.png'), size)
        screen.blit(fon, (0, 0))

        level_1_x, level_1_y = [i for i in range(217, 400)], [i for i in range(237, 390)]
        level_2_x, level_2_y = [i for i in range(498, 675)], [i for i in range(237, 388)]
        level_3_x, level_3_y = [i for i in range(781, 965)], [i for i in range(228, 397)]
        level_4_x, level_4_y = [i for i in range(386, 558)], [i for i in range(437, 593)]
        level_5_x, level_5_y = [i for i in range(661, 831)], [i for i in range(431, 592)]

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if pos[0] in level_1_x and pos[1] in level_1_y:
                        return 1
                    if pos[0] in level_2_x and pos[1] in level_2_y:
                        return 2
                    if pos[0] in level_3_x and pos[1] in level_3_y:
                        return 3
                    if pos[0] in level_4_x and pos[1] in level_4_y:
                        return 4
                    if pos[0] in level_5_x and pos[1] in level_5_y:
                        return 5
            pygame.display.flip()


class Player:
    def __init__(self):
        self.coins = 0
        self.last_coin_time = pygame.time.get_ticks()
        self.spawn_time = pygame.time.get_ticks()
        self.spawn_delay = 2000

    def update_coins(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_coin_time >= 5000:
            self.coins += 10
            self.last_coin_time = current_time

    def spawn_mob(self, mob_sprites, type):
        dct = {'ogre': Ogre(), 'skeleton': Skeleton(), 'zombie': Zombie(), 'minotaur': Minotaur(), 'golem': Golem()}
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time >= self.spawn_delay:
            new_mob = dct[type]
            mob_sprites.add(new_mob)
            self.spawn_time = current_time


def game_start():
    start_screen()
    level_selector = LevelSelector()
    current_level = level_selector.load_image()
    return current_level


map_matrix = None
map_photo.image = pygame.transform.scale(load_image("map_photo1.png"), (1040, 800))
map_photo.rect = map_photo.image.get_rect()
map_photo.rect.x = 0
map_photo.rect.y = 0

lst = ['skeleton', 'ogre', 'zombie', 'minotaur', 'golem']

tower_selector_image = pygame.transform.scale(load_image('tower_selector (2).png'), (200, 351))

coin_image = pygame.transform.scale(load_image('coin.png'), (50, 50))
stop_image = pygame.transform.scale(load_image('icons/stop.png'), (90, 90))

play_button_image = pygame.transform.scale(load_image('icons/playbuttonpdn.png'), (100, 100))
settings_button_image = pygame.transform.scale(load_image('icons/settings.png'), (80, 80))
exit_button_image = pygame.transform.scale(load_image('icons/exit.png'), (80, 80))
arrow_images = load_arrow_images()
map_sprites.add(map_photo)


def run_game():
    global map_matrix, map_photo
    cur_lev = game_start()
    map_matrix = choose_map_matrix(cur_lev)
    map_photo.image = pygame.transform.scale(load_image(f"map_photo{cur_lev}.png"), (1040, 800))
    main_screen = pygame.display.set_mode((WIDTH + 200, HEIGHT))
    running = True
    tower_sprites = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    mob_sprites = pygame.sprite.Group()
    map_sprites = pygame.sprite.Group()
    map_sprites.add(map_photo)
    selected_tower = None
    mob_type = lst[cur_lev - 1]
    selected_tower_type = 'arrow'
    player = Player()
    paused = False

    while running:
        main_screen.fill(pygame.Color("black"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if WIDTH + 50 <= mouse_x <= WIDTH + 140 and 420 <= mouse_y <= 510:
                        paused = not paused
                    elif paused:
                        if HEIGHT // 2 <= mouse_y <= HEIGHT // 2 + 60:
                            if WIDTH // 2 - 180 <= mouse_x <= WIDTH // 2 - 100:
                                return "restart"
                            elif WIDTH // 2 - 40 <= mouse_x <= WIDTH // 2 + 40:
                                paused = False
                            elif WIDTH // 2 + 100 <= mouse_x <= WIDTH // 2 + 160:
                                print("Настройки")
                        elif HEIGHT // 2 <= mouse_y <= HEIGHT // 2 + 80:
                            if WIDTH // 2 - 40 <= mouse_x <= WIDTH // 2 + 40:
                                paused = False
                    else:
                        clicked_tower = [tower for tower in tower_sprites if tower.rect.collidepoint(mouse_x, mouse_y)]
                        if clicked_tower:
                            clicked_tower[0].upgrade(player)
                        elif WIDTH <= mouse_x <= WIDTH + 200:
                            if mouse_y <= 117:
                                selected_tower_type = 'arrow'
                            elif mouse_y <= 234:
                                selected_tower_type = 'stone'
                            elif mouse_y <= 351:
                                selected_tower_type = 'electric'
                        else:
                            if selected_tower and not selected_tower.placed:
                                result = place_tower(mouse_x, mouse_y)
                                if result:
                                    center_x, center_y = result
                                    selected_tower.placed = True
                                    selected_tower.rect.center = (center_x, center_y)
                                    tower_sprites.add(selected_tower)
                                    selected_tower = None
                                    pygame.mouse.set_visible(True)
                            else:
                                selected_tower = Tower(mouse_x, mouse_y, 150, arrow_images,
                                                       f"Upgrade_{selected_tower_type}_tower")
                                pygame.mouse.set_visible(False)

        if not paused:
            player.update_coins()
            player.spawn_mob(mob_sprites, mob_type)
            mob_sprites.update()
            bullet_group.update()
            tower_sprites.update(mob_sprites, bullet_group)

            for bullet in bullet_group:
                collisions = pygame.sprite.spritecollide(bullet, mob_sprites, False, pygame.sprite.collide_mask)
                if collisions:
                    for mob in collisions:
                        mob.take_damage(10)
                    bullet.kill()
            for mob in mob_sprites:
                if mob.killed:
                    mob.kill()


        map_sprites.draw(main_screen)
        tower_sprites.draw(main_screen)
        bullet_group.draw(main_screen)
        mob_sprites.draw(main_screen)

        main_screen.blit(tower_selector_image, (WIDTH, 0))
        text = font.render(f'Coins: {player.coins}', True, (255, 255, 255))
        main_screen.blit(text, (WIDTH + 55, 351 + 25))
        main_screen.blit(coin_image, (WIDTH + 5, 361))
        main_screen.blit(stop_image, (WIDTH + 50, 420))

        if selected_tower:
            selected_tower.rect.center = pygame.mouse.get_pos()
            temp_image = selected_tower.image.copy()
            temp_image.set_alpha(128)
            main_screen.blit(temp_image, selected_tower.rect.topleft)
            radius_center = (selected_tower.rect.centerx, selected_tower.rect.centery + RADIUS_Y_OFFSET)
            pygame.draw.circle(main_screen, (255, 0, 0), radius_center, selected_tower.radius, 1)

        if paused:
            draw_pause_menu(main_screen, font)

        pygame.display.flip()
        clock.tick(FPS)
    return "exit"


def main():
    while True:
        result = run_game()
        if result == "exit":
            break

    terminate()


if __name__ == '__main__':
    main()
