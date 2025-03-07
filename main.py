import math
import os
import sqlite3
import sys
from random import randint

import pygame

volume = 0.5
pygame.mixer.init()
pygame.mixer.music.load("data/music/background_music.mp3")
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play(-1)


def change_volume(action):
    global volume
    if action == 'up':
        volume = min(1.0, volume + 0.1)
    else:
        volume = max(0.0, volume - 0.1)


def choose_map_matrix(number):
    if number == 1:
        map = [['g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
               ['g', '2', 't', 'g', 'g', 'g', 'g', 'g', 'h', 'g', 'g', 'g', 'g'],
               ['g', '3', 'g', 'g', 'g', 't', 'g', 'g', '38', 'g', 'g', 'g', 'g'],
               ['t', '4', 'g', 'g', '33', '34', '35', '36', '37', 't', 'g', 'g', 'g'],
               ['g', '5', 'g', 'g', '32', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
               ['g', '6', 'g', 'g', '31', 't', 'g', 'g', 't', 'g', 'g', 'g', 'g'],
               ['g', '7', 't', 'g', '30', '29', '28', '27', '26', '25', '24', '23', 'g'],
               ['t', '8', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 't', '22', 'g'],
               ['g', '9', 't', 'g', 'g', 't', 'g', 'g', 't', 'g', 'g', '21', 'g'],
               ['g', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 'g']]
        x, y = 600, 30
        return map, x, y
    elif number == 2:
        map = [['g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 't', 'g', 'g', 'g', 'g'],
               ['t', '2', 'g', 'g', '9', '10', '11', '12', '13', '14', '15', '16', 'g'],
               ['g', '3', 't', 'g', '8', 't', 'g', 't', 'g', 'g', 't', '17', 'g'],
               ['g', '4', '5', '6', '7', 'g', 'g', 'g', 'g', 'g', 'g', '18', 'g'],
               ['g', 'g', 't', 'g', 'g', 'g', '30', '29', '28', 'g', 'g', '19', 't'],
               ['g', 'g', 'g', 'g', '33', '32', '31', 't', '27', 'g', 'g', '20', 'g'],
               ['g', 'g', 'g', 'g', '34', 't', 'g', 'g', '26', 'g', 't', '21', 'g'],
               ['g', 'g', 'g', 't', '35', 'g', 'g', 'g', '25', '24', '23', '22', 'g'],
               ['g', 'h', '38', '37', '36', 'g', 'g', 'g', 'g', 't', 'g', 'g', 'g'],
               ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']]
        x, y = 15, HEIGHT - 215
        return map, x, y
    elif number == 3:
        map = [['g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
               ['g', '2', 't', 'g', 'g', 'g', 'g', 'h', 'g', 'g', 'g', 'g', 'g'],
               ['g', '3', '4', '5', '6', 'g', 'g', '35', 'g', 'g', 't', 'g', 'g'],
               ['g', 't', 'g', 'g', '7', 't', 'g', '34', '33', '32', '31', '30', 'g'],
               ['g', 'g', 't', 'g', '8', 'g', 'g', 'g', 'g', 't', 'g', '29', 't'],
               ['g', '12', '11', '10', '9', 'g', 'g', 'g', '25', '26', '27', '28', 'g'],
               ['g', '13', 't', 'g', 'g', 'g', 'g', 'g', '24', 't', 'g', 'g', 'g'],
               ['t', '14', 'g', 'g', 't', 'g', 'g', 't', '23', 'g', 'g', 'g', 'g'],
               ['g', '15', '16', '17', '18', '19', '20', '21', '22', 'g', 'g', 'g', 'g'],
               ['g', 'g', 'g', 't', 'g', 'g', 't', 'g', 'g', 'g', 'g', 'g', 'g']]
        x, y = 520, 30
        return map, x, y
    elif number == 4:
        map = [['g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 't', 'g', 'g', 'g', 'g'],
               ['g', '2', 't', 'g', 'g', 'g', '25', '26', '27', '28', '29', 'g', 'g'],
               ['g', '3', '4', '5', 'g', 'g', '24', 't', 'g', 't', '30', 'g', 'g'],
               ['g', 'g', 't', '6', 'g', 't', '23', 'g', 'g', 'g', '31', 't', 'g'],
               ['g', 'g', 'g', '7', 't', 'g', '22', 'g', 'g', 't', '32', 'g', 'g'],
               ['g', '10', '9', '8', 'g', 'g', '21', 'g', 'g', 'g', '33', 't', 'g'],
               ['g', '11', 't', 'g', 'g', 'g', '20', 'g', 'g', 'g', '34', 'g', 'g'],
               ['t', '12', 'g', 'g', 'g', 't', '19', 'g', 'g', 'g', '35', 'g', 'g'],
               ['g', '13', '14', '15', '16', '17', '18', 'g', 'g', 'g', 'h', 'g', 'g'],
               ['g', 'g', 'g', 't', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']]
        x, y = 750, HEIGHT - 150
        return map, x, y
    elif number == 5:
        map = [['g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
               ['t', '2', 't', 'g', 'g', 'g', 't', 'g', 't', 'g', 'g', 'g', 'g'],
               ['g', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'g', 'g'],
               ['g', 'g', 'g', 'g', 't', 'g', 'g', 't', 'g', 't', '13', 'g', 'g'],
               ['g', 'g', 't', 'g', 'g', 'g', 't', 'g', 'g', 'g', '14', 't', 'g'],
               ['g', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', 'g', 'g'],
               ['g', '25', 't', 'g', 't', 'g', 'g', 't', 'g', 't', 'g', 'g', 'g'],
               ['g', '26', 'g', 't', '31', '32', '33', '34', 't', 'g', 'g', 'g', 'g'],
               ['g', '27', '28', '29', '30', 'g', 't', '35', '36', '37', '38', 'h', 'g'],
               ['g', 'g', 't', 'g', 'g', 'g', 'g', 'g', 'g', 't', 'g', 'g', 'g']]
        x, y = WIDTH - 220, HEIGHT - 250
        return map, x, y


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

tower_costs = {
    'Upgrade_arrow_tower': 100,
    'Upgrade_stone_tower': 500,
    'Upgrade_electric_tower': 900
}


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


def get_tower_cost(tower_type):
    if tower_type == 'Upgrade_arrow_tower':
        return 100
    elif tower_type == 'Upgrade_stone_tower':
        return 500
    elif tower_type == 'Upgrade_electric_tower':
        return 900
    return 0


def show_end_screen(screen, game_snapshot, image_name):
    end_image = load_image(image_name)
    image_y = -HEIGHT
    target_y = 0
    speed = 5
    screen.blit(end_image, (0, 0))

    exit_button_rect = pygame.Rect(490, 430, 260, 260)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if exit_button_rect.collidepoint(mouse_pos):
                    return "main_menu"

        if image_y < target_y:
            image_y += speed

        screen.blit(game_snapshot, (0, 0))
        screen.blit(end_image, (0, image_y))

        pygame.display.flip()


def load_upgrade_images(tower_type):
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


class DataBase:
    def __init__(self):
        self.con = sqlite3.connect('identifier.sqlite')
        self.cur = self.con.cursor()

    def add_level(self, count, name):
        self.cur.execute(f"""
        INSERT INTO user_level (user, level) VALUES ('{name}', '{count}')
        """)
        self.con.commit()

    def get_level(self, name):
        self.cur.execute("""
        SELECT level FROM user_level WHERE user = ?
        """, (name,))
        result = self.cur.fetchone()
        if result:
            return int(result[0])
        return None

    def update_level(self, name):
        self.cur.execute(f"""
                        UPDATE user_level SET level = '{self.get_level(name) + 1}' WHERE user = '{name}';
                        """)
        self.con.commit()


def draw_tower_stats(screen, mouse_x, mouse_y):
    font = pygame.font.Font(None, 24)
    text_color = (255, 255, 255)

    if WIDTH <= mouse_x <= WIDTH + 200 and mouse_y <= 117:
        c, r = "Cost: 100", 'Range: 180'
        text_c = font.render(c, True, text_color)
        text_r = font.render(r, True, text_color)
        screen.blit(text_c, (WIDTH + 20, 70))
        screen.blit(text_r, (WIDTH + 20, 90))

    elif WIDTH <= mouse_x <= WIDTH + 200 and mouse_y <= 234:
        c, r = "Cost: 500", 'Range: 170'
        text_c = font.render(c, True, text_color)
        text_r = font.render(r, True, text_color)
        screen.blit(text_c, (WIDTH + 20, 180))
        screen.blit(text_r, (WIDTH + 20, 200))

    elif WIDTH <= mouse_x <= WIDTH + 200 and mouse_y <= 351:
        c, r = "Cost: 900", 'Range: 170'
        text_c = font.render(c, True, text_color)
        text_r = font.render(r, True, text_color)
        screen.blit(text_c, (WIDTH + 20, 300))
        screen.blit(text_r, (WIDTH + 20, 320))


class LoginMenu:
    def load_image(name):
        size = 1200, 630
        screen = pygame.display.set_mode(size)

        fon = pygame.transform.scale(load_image('login.png'), size)
        screen.blit(fon, (0, 0))

        exit_x, exit_y = [i for i in range(506, 694)], [i for i in range(415, 592)]

        base_font = pygame.font.Font(None, 170)
        user_text = ''
        input_rect = pygame.Rect(115, 245, 970, 135)
        color = pygame.Color('#4C4C45')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if pos[0] in exit_x and pos[1] in exit_y:
                        return user_text
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
            pygame.draw.rect(screen, color, input_rect)
            if len(user_text) < 15:
                text_surface = base_font.render(user_text, True, (255, 255, 255))
                screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
                pygame.display.flip()


class MainHouse:
    def __init__(self, max_health):
        self.max_health = max_health
        self.health = max_health

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def draw_health_bar(self, screen, x, y, width, height):
        pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
        health_width = int((self.health / self.max_health) * width)
        pygame.draw.rect(screen, (0, 255, 0), (x, y, health_width, height))


class Tower(pygame.sprite.Sprite):
    upgrade_arrow_costs = [150, 300, 400, 500, 1000]
    upgrade_stone_costs = [300, 800]
    upgrade_electric_costs = [500, 1000]

    def __init__(self, x, y, radius, arrow_images, tower_type):
        super().__init__()
        self.level = 0
        self.images = load_upgrade_images(tower_type)
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
        self.damage = 5
        self.plus_damage = 3

    def upgrade(self, player):
        if self.level < len(self.images) - 1:
            cost = self.get_upgrade_cost()
            if player.coins >= cost:
                player.coins -= cost
                self.level += 1
                self.image = self.images[self.level]
                self.shoot_delay = max(100, self.shoot_delay - 100)
                self.shoot_speed += 2
                self.damage += self.plus_damage

    def update(self, mobs, bullet_group):
        if self.placed:
            if not self.target:
                for mob in mobs:
                    distance = math.hypot(self.rect.centerx - mob.rect.centerx, self.rect.centery - mob.rect.centery)
                    if distance <= self.radius:
                        self.target = mob
                        break

            if self.target:
                if self.target.alive():
                    current_time = pygame.time.get_ticks()
                    if current_time - self.last_shot_time > self.shoot_delay:
                        self.shoot(bullet_group)
                        self.last_shot_time = current_time
                    distance = math.hypot(self.rect.centerx - self.target.rect.centerx,
                                          self.rect.centery - self.target.rect.centery)
                    if distance > self.radius:
                        self.target = None
                else:
                    self.target = None

    def shoot(self, bullet_group):
        if self.target:
            if self.tower_type == 'Upgrade_stone_tower':
                bullet = Bullet(self.rect.center, self.target.rect.center, self.arrow_images, self.damage,
                                is_stone=True)
            elif self.tower_type == 'Upgrade_electric_tower':
                bullet = Bullet(self.rect.center, self.target.rect.center, self.arrow_images, self.damage,
                                is_lightning=True)
            else:
                bullet = Bullet(self.rect.center, self.target.rect.center, self.arrow_images, self.damage)
            bullet.speed = self.shoot_speed
            bullet.damage = self.damage
            bullet_group.add(bullet)

    def get_upgrade_cost(self):
        if self.tower_type == 'Upgrade_stone_tower':
            return self.upgrade_stone_costs[self.level]
        elif self.tower_type == 'Upgrade_electric_tower':
            return self.upgrade_electric_costs[self.level]
        else:
            return self.upgrade_arrow_costs[self.level]


class StoneTower(Tower):
    def __init__(self, x, y, arrow_images):
        super().__init__(x=x, y=y, radius=170, arrow_images=arrow_images, tower_type='Upgrade_stone_tower')
        self.damage = 15
        self.plus_damage = 5


class ElectricTower(Tower):
    def __init__(self, x, y, arrow_images):
        super().__init__(x=x, y=y, radius=170, arrow_images=arrow_images, tower_type='Upgrade_electric_tower')
        self.damage = 30
        self.plus_damage = 5


class ArrowTower(Tower):
    def __init__(self, x, y, arrow_images):
        super().__init__(x=x, y=y, radius=180, arrow_images=arrow_images, tower_type='Upgrade_arrow_tower')
        self.damage = 10
        self.plus_damage = 3


class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos, arrow_images, damage, is_stone=False, is_lightning=False):
        super().__init__()
        self.start_pos = start_pos
        self.target_pos = target_pos
        self.arrow_images = arrow_images
        self.is_stone = is_stone
        self.is_lightning = is_lightning
        self.damage = damage

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
        self.frames = None
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.pos_x = 80
        self.pos_y = -40

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(70, -50, sheet.get_width() // columns, sheet.get_height() // rows)
        self.frames = []
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Mob(AnimatedSprite):
    def __init__(self, image_path, columns, rows, x, y, speed, health, damage, is_boss, lev_count):
        super().__init__(load_image(image_path), columns, rows, x, y)
        self.speed = speed
        self.x = 1
        self.y = 0
        self.last_y = self.rect.y
        self.last_x = self.rect.x
        self.count = 1
        self.spawn_time = pygame.time.get_ticks()
        self.health = health
        self.killed = False
        self.is_damaged = False
        self.is_dying = False
        self.damage = damage
        self.damage_time = 0
        self.damage_duration = 500
        self.is_boss = bool(is_boss)
        if lev_count in (1, 2, 5):
            self.lev_count = 38
        else:
            self.lev_count = 35
        if is_boss:
            self.death_sheet = load_image(image_path.replace(".png", "_falling.png"))
            self.make_boss()

    def start_death_animation(self):
        current_pos = self.rect.topleft
        self.cut_sheet(self.death_sheet, 6, 2)
        self.rect.topleft = current_pos
        self.cur_frame = 0
        self.is_dying = True

    def update(self):
        current_time = pygame.time.get_ticks()

        if self.is_dying:
            self.image = self.frames[self.cur_frame]
            self.cur_frame += 1
            if self.cur_frame == len(self.frames):
                self.killed = True
                self.kill()
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
        if self.count == self.lev_count:
            if hasattr(self, 'main_house'):
                self.main_house.take_damage(self.health)
            self.killed = True

    def take_damage(self, damage):
        self.health -= damage
        self.is_damaged = True
        self.damage_time = pygame.time.get_ticks()

        if self.health <= 0 and not self.is_dying:
            if self.is_boss:
                self.start_death_animation()
            else:
                self.killed = True

    def make_boss(self):
        self.health += 50
        self.damage += 10


class Skeleton(Mob):
    def __init__(self, is_boss, lev):
        super().__init__(
            image_path=f"mobs/skelet{is_boss}.png",
            columns=6,
            rows=2,
            x=37,
            y=50,
            speed=5,
            health=100,
            damage=20,
            is_boss=is_boss,
            lev_count=lev
        )
        self.damaged_image = AnimatedSprite(load_image(f'mobs/skelet{is_boss}_damaged.png'), 6, 2, 37, 50)


class Ogre(Mob):
    def __init__(self, is_boss, lev):
        super().__init__(
            image_path=f"mobs/ogre{is_boss}.png",
            columns=6,
            rows=2,
            x=37,
            y=50,
            speed=5,
            health=200,
            damage=20,
            is_boss=is_boss,
            lev_count=lev
        )
        self.damaged_image = AnimatedSprite(load_image(f'mobs/ogre{is_boss}_damaged.png'), 6, 2, 37, 50)


class Minotaur(Mob):
    def __init__(self, is_boss, lev):
        super().__init__(
            image_path=f"mobs/minotaur{is_boss}.png",
            columns=6,
            rows=2,
            x=37,
            y=50,
            speed=5,
            health=300,
            damage=20,
            is_boss=is_boss,
            lev_count=lev
        )
        self.damaged_image = AnimatedSprite(load_image(f'mobs/minotaur{is_boss}_damaged.png'), 6, 2, 37, 50)


class Zombie(Mob):
    def __init__(self, is_boss, lev):
        super().__init__(
            image_path=f"mobs/zombie{is_boss}.png",
            columns=6,
            rows=2,
            x=37,
            y=50,
            speed=5,
            health=250,
            damage=20,
            is_boss=is_boss,
            lev_count=lev
        )
        self.damaged_image = AnimatedSprite(load_image(f'mobs/zombie{is_boss}_damaged.png'), 6, 2, 37, 50)


class Golem(Mob):
    def __init__(self, is_boss, lev):
        super().__init__(
            image_path=f"mobs/golem{is_boss}.png",
            columns=6,
            rows=2,
            x=37,
            y=50,
            speed=5,
            health=400,
            damage=20,
            is_boss=is_boss,
            lev_count=lev
        )
        self.damaged_image = AnimatedSprite(load_image(f'mobs/golem{is_boss}_damaged.png'), 6, 2, 37, 50)
        if is_boss:
            self.health += 10


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


def draw_settings_menu(screen, font):
    overlay = pygame.Surface((WIDTH + 200, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 170))
    screen.blit(overlay, (0, 0))

    settings_font = pygame.font.Font(None, 100)
    settings_text = settings_font.render("SETTINGS", True, (255, 255, 255))
    settings_rect = settings_text.get_rect(center=(WIDTH // 2 + 10, HEIGHT // 2 - 150))
    screen.blit(settings_text, settings_rect)

    screen.blit(exit_button_image, (WIDTH // 2 - 20, HEIGHT // 2 + 50))
    text = font.render("Back", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - 10, HEIGHT // 2 + 150))

    volume_up_button = pygame.transform.scale(load_image("icons/soundon.png"), (80, 80))
    volume_down_button = pygame.transform.scale(load_image("icons/soundoff.png"), (80, 80))

    screen.blit(volume_up_button, (WIDTH // 2 - 100, HEIGHT // 2 - 100))
    screen.blit(volume_down_button, (WIDTH // 2 + 50, HEIGHT // 2 - 100))

    volume_text = font.render(f"Volume: {int(volume * 100)}%", True, (255, 255, 255))
    screen.blit(volume_text, (WIDTH // 2 - 60, HEIGHT // 2))


class LevelSelector:
    def __init__(self, name):
        self.name = name

    def load_image(self):
        size = 1200, 630
        screen = pygame.display.set_mode(size)
        fon = pygame.transform.scale(load_image('unlocked_1.png'), size)

        level_1_x, level_1_y = [i for i in range(217, 400)], [i for i in range(237, 390)]
        if get_levels(self.name) >= 2:
            level_2_x, level_2_y = [i for i in range(498, 675)], [i for i in range(237, 388)]
            fon = pygame.transform.scale(load_image('unlocked_2.png'), size)
            if get_levels(self.name) >= 3:
                level_3_x, level_3_y = [i for i in range(781, 965)], [i for i in range(228, 397)]
                fon = pygame.transform.scale(load_image('unlocked_3.png'), size)
                if get_levels(self.name) >= 4:
                    level_4_x, level_4_y = [i for i in range(386, 558)], [i for i in range(437, 593)]
                    fon = pygame.transform.scale(load_image('unlocked_4.png'), size)
                    if get_levels(self.name) >= 5:
                        level_5_x, level_5_y = [i for i in range(661, 831)], [i for i in range(431, 592)]
                        fon = pygame.transform.scale(load_image('unlocked_5.png'), size)
        screen.blit(fon, (0, 0))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    try:
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
                    except Exception:
                        ...
            pygame.display.flip()


class Player:
    start_coins = [250, 430, 500, 700, 900]
    spawn_quantity = [(10, 15, 20, 25, 30), (20, 25, 30, 35, 35), (30, 35, 40, 45, 45), (40, 45, 50, 55, 55),
                      (50, 55, 60, 65, 65)]
    boss_quantity = [(0, 0, 1, 0, 2), (0, 1, 2, 0, 3), (0, 1, 2, 0, 3), (0, 1, 2, 0, 3), (0, 1, 2, 0, 3)]

    def __init__(self, level):
        self.level = level
        self.coins = self.get_start_coins()
        self.last_coin_time = pygame.time.get_ticks()
        self.spawn_time = pygame.time.get_ticks()
        self.wave = 0
        self.to_spawn = 0
        self.to_spawn_boss = 0
        self.mobs_killed = 0
        self.bosses_killed = 0

    def update_coins(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_coin_time >= 5000:
            self.coins += 10
            self.last_coin_time = current_time

    def add_coins_for_kill(self, is_boss):
        if is_boss:
            self.coins += 50
            self.bosses_killed += 1
        else:
            self.coins += 10
            self.mobs_killed += 1

    def get_start_coins(self):
        return self.start_coins[self.level - 1]

    def spawn_mob(self, mob_sprites, type, main_house, lev):
        is_boss = ''
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time >= randint(500, 3000):
            if self.to_spawn_boss > 0:
                is_boss = '_boss' if randint(1, 2) == 1 or self.to_spawn == 0 else ''
                if is_boss:
                    self.to_spawn_boss -= 1
            dct = {'ogre': Ogre(is_boss, lev), 'skeleton': Skeleton(is_boss, lev), 'zombie': Zombie(is_boss, lev),
                   'minotaur': Minotaur(is_boss, lev), 'golem': Golem(is_boss, lev)}
            new_mob = dct[type]
            new_mob.main_house = main_house
            mob_sprites.add(new_mob)
            self.spawn_time = current_time
            self.to_spawn -= 1

    def update(self, mob_sprites, type, main_house, lev):
        if self.to_spawn + self.to_spawn_boss > 0:
            self.spawn_mob(mob_sprites, type, main_house, lev)  # 8563


def start_login():
    login_menu = LoginMenu()
    res = login_menu.load_image()
    return res


def game_start(name):
    start_screen()
    level_selector = LevelSelector(name)
    current_level = level_selector.load_image()
    return current_level


def add_player(name):
    database = DataBase()
    database.add_level(1, name)
    return database


def get_levels(name):
    database = DataBase()
    return database.get_level(name)


map_matrix = None
map_photo.image = pygame.transform.scale(load_image("map_photo1.png"), (1040, 800))
map_photo.rect = map_photo.image.get_rect()
map_photo.rect.x = 0
map_photo.rect.y = 0

mobs = ['skeleton', 'ogre', 'zombie', 'minotaur', 'golem']

tower_selector_image = pygame.transform.scale(load_image('tower_selector (2).png'), (200, 351))

coin_image = pygame.transform.scale(load_image('coin.png'), (50, 50))
stop_image = pygame.transform.scale(load_image('icons/stop.png'), (90, 90))

play_button_image = pygame.transform.scale(load_image('icons/playbuttonpdn.png'), (100, 100))
settings_button_image = pygame.transform.scale(load_image('icons/settings.png'), (80, 80))
exit_button_image = pygame.transform.scale(load_image('icons/exit.png'), (80, 80))
arrow_images = load_arrow_images()
map_sprites.add(map_photo)


def run_game(database, user_name):
    global map_matrix, map_photo
    cur_lev = game_start(user_name)
    map_matrix, main_x, main_y = choose_map_matrix(cur_lev)
    map_photo.image = pygame.transform.scale(load_image(f"map_photo{cur_lev}.png"), (1040, 800))
    main_screen = pygame.display.set_mode((WIDTH + 200, HEIGHT))
    running = True
    tower_sprites = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    mob_sprites = pygame.sprite.Group()
    map_sprites = pygame.sprite.Group()
    map_sprites.add(map_photo)
    selected_tower = None
    mob_type = mobs[cur_lev - 1]
    selected_tower_type = None
    player = Player(cur_lev)
    paused = False
    in_settings = False

    main_house = MainHouse(max_health=1000)

    while running:
        main_screen.fill(pygame.Color("black"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if WIDTH <= mouse_x <= WIDTH + 200 and HEIGHT - 30 <= mouse_y <= HEIGHT:
                        game_snapshot = main_screen.copy()
                        result = show_end_screen(main_screen, game_snapshot, "victory.png")
                        if result == "main_menu":
                            database.update_level(user_name)
                            return "restart"
                    if WIDTH + 50 <= mouse_x <= WIDTH + 140 and 420 <= mouse_y <= 510:
                        paused = not paused
                    elif paused and not in_settings:
                        if HEIGHT // 2 <= mouse_y <= HEIGHT // 2 + 60:
                            if WIDTH // 2 - 180 <= mouse_x <= WIDTH // 2 - 100:
                                return "restart"
                            elif WIDTH // 2 - 40 <= mouse_x <= WIDTH // 2 + 40:
                                paused = False
                            elif WIDTH // 2 + 140 <= mouse_x <= WIDTH // 2 + 200:
                                in_settings = True
                    elif in_settings:
                        if 505 <= mouse_x <= 577 and 455 <= mouse_y <= 526:
                            in_settings = False
                        elif 424 <= mouse_x <= 496 and 304 <= mouse_y <= 377:
                            change_volume('up')
                            pygame.mixer.music.set_volume(volume)
                        elif 578 <= mouse_x <= 640 and 304 <= mouse_y <= 377:
                            change_volume('down')
                            pygame.mixer.music.set_volume(volume)

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
                                if selected_tower_type and player.coins >= tower_costs[
                                    f"Upgrade_{selected_tower_type}_tower"]:
                                    if selected_tower_type == 'arrow':
                                        selected_tower = ArrowTower(mouse_x, mouse_y, arrow_images)
                                    elif selected_tower_type == 'stone':
                                        selected_tower = StoneTower(mouse_x, mouse_y, arrow_images)
                                    else:
                                        selected_tower = ElectricTower(mouse_x, mouse_y, arrow_images)
                                    player.coins -= tower_costs[f"Upgrade_{selected_tower_type}_tower"]
                                    pygame.mouse.set_visible(False)

        if not paused:
            player.update_coins()
            if player.wave < 5 and player.mobs_killed >= (player.spawn_quantity[player.level - 1][
                player.wave - 1] if player.wave > 0 else 0):
                player.to_spawn += player.spawn_quantity[player.level - 1][player.wave]
                player.to_spawn_boss += player.boss_quantity[player.level - 1][player.wave]
                player.wave += 1

            mob_sprites.update()
            bullet_group.update()
            tower_sprites.update(mob_sprites, bullet_group)
            player.update(mob_sprites, mob_type, main_house, cur_lev)

            for bullet in bullet_group:
                collisions = pygame.sprite.spritecollide(bullet, mob_sprites, False, pygame.sprite.collide_mask)
                if collisions:
                    for mob in collisions:
                        mob.take_damage(bullet.damage)
                        if mob.killed:
                            player.add_coins_for_kill(mob.is_boss)
                            mob.kill()
                    bullet.kill()
            for mob in mob_sprites:
                if mob.killed:
                    player.mobs_killed += 1
                    mob.kill()

        map_sprites.draw(main_screen)
        mob_sprites.draw(main_screen)
        tower_sprites.draw(main_screen)
        bullet_group.draw(main_screen)
        main_house.draw_health_bar(main_screen, x=main_x, y=main_y, width=200, height=20)

        main_screen.blit(tower_selector_image, (WIDTH, 0))
        text = font.render(f'Coins: {player.coins}', True, (255, 255, 255))
        main_screen.blit(text, (WIDTH + 55, 351 + 25))
        main_screen.blit(coin_image, (WIDTH + 5, 361))
        main_screen.blit(stop_image, (WIDTH + 50, 420))

        if main_house.health <= 0:
            game_snapshot = main_screen.copy()
            result = show_end_screen(main_screen, game_snapshot, "loose.png")
            if result == "main_menu":
                return "restart"

        if (player.wave == 5 and len(mob_sprites) == 0):
            game_snapshot = main_screen.copy()
            result = show_end_screen(main_screen, game_snapshot, "victory.png")
            if result == "main_menu":
                database.update_level(user_name)
                return "restart"

        mouse_x, mouse_y = pygame.mouse.get_pos()
        draw_tower_stats(main_screen, mouse_x, mouse_y)
        if selected_tower:
            selected_tower.rect.center = pygame.mouse.get_pos()
            temp_image = selected_tower.image.copy()
            temp_image.set_alpha(128)
            main_screen.blit(temp_image, selected_tower.rect.topleft)
            radius_center = (selected_tower.rect.centerx, selected_tower.rect.centery + RADIUS_Y_OFFSET)
            pygame.draw.circle(main_screen, (255, 0, 0), radius_center, selected_tower.radius, 1)

        if paused:
            if in_settings:
                draw_settings_menu(main_screen, font)
            else:
                draw_pause_menu(main_screen, font)

        pygame.display.flip()
        clock.tick(FPS)
    return "exit"


def main():
    user_name = start_login()
    database = add_player(user_name)
    while True:
        result = run_game(database, user_name)
        if result == "exit":
            break

    terminate()


if __name__ == '__main__':
    main()
