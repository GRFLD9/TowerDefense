import math
import os
import sys
from random import randint
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
# Радиус поражения башни
# Стоимость башни

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
TRANSPARENT = (255, 255, 255, 128)  # Прозрачный цвет

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()


# Класс башни (наследуется от pygame.sprite.Sprite)
class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, radius, cost):
        super().__init__()
        self.image = load_image(image_path)
        self.rect = self.image.get_rect(center=(x, y))
        self.radius = radius
        self.cost = cost
        self.placed = False  # Флаг, установлена ли башня
        self.target = None  # Цель для стрельбы
        self.bullets = []  # Список пуль

    def update(self, mobs):
        if self.placed:
            # Поиск цели в радиусе поражения
            if not self.target:
                for mob in mobs:
                    distance = math.hypot(self.rect.centerx - mob.rect.centerx, self.rect.centery - mob.rect.centery)
                    if distance <= self.radius:
                        self.target = mob
                        break
            # Стрельба по цели
            if self.target:
                self.shoot()
                # Проверка, если цель вышла за радиус
                distance = math.hypot(self.rect.centerx - self.target.rect.centerx,
                                      self.rect.centery - self.target.rect.centery)
                if distance > self.radius:
                    self.target = None

    def shoot(self):
        if self.target:
            # Создание пули (линии от башни до цели)
            bullet = {
                'start': self.rect.center,
                'end': self.target.rect.center,
                'lifetime': 2  # Время отображения пули
            }
            self.bullets.append(bullet)

    def update_bullets(self):
        # Обновление времени жизни пуль
        for bullet in self.bullets:
            bullet['lifetime'] -= 1
        # Удаление пуль с истекшим временем жизни
        self.bullets = [bullet for bullet in self.bullets if bullet['lifetime'] > 0]

    def draw_bullets(self, surface):
        # Отрисовка пуль
        for bullet in self.bullets:
            pygame.draw.line(surface, RED, bullet['start'], bullet['end'], 3)


# Класс моба (наследуется от pygame.sprite.Sprite)
class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.transform.scale(load_image(image_path), (55, 55))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2

    def update(self):
        self.rect.x += self.speed


# Основной цикл игры
def main():
    running = True
    tower_sprites = pygame.sprite.Group()  # Группа для башен
    mob_sprites = pygame.sprite.Group()  # Группа для мобов
    selected_tower = None

    # Создаем несколько мобов для примера
    for i in range(5):
        mob = Mob(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT), "mob.png")
        mob_sprites.add(mob)

    while running:
        clock.tick(FPS)
        screen.fill(WHITE)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    if selected_tower and not selected_tower.placed:
                        # Установка башни
                        selected_tower.placed = True
                        tower_sprites.add(selected_tower)
                        selected_tower = None
                    else:
                        # Выбор башни
                        selected_tower = Tower(event.pos[0], event.pos[1], "tower.png", 100, 50)

        # Обновление мобов
        mob_sprites.update()

        # Обновление башен
        for tower in tower_sprites:
            tower.update(mob_sprites)
            tower.update_bullets()

        # Отрисовка мобов
        mob_sprites.draw(screen)

        # Отрисовка башен
        tower_sprites.draw(screen)

        # Отрисовка пуль
        for tower in tower_sprites:
            tower.draw_bullets(screen)

        # Отрисовка выбранной башни (если есть)
        if selected_tower:
            selected_tower.rect.center = pygame.mouse.get_pos()
            temp_image = selected_tower.image.copy()
            temp_image.set_alpha(128)  # Прозрачность
            screen.blit(temp_image, selected_tower.rect.topleft)
            # Рисуем радиус поражения
            pygame.draw.circle(screen, RED, selected_tower.rect.center, selected_tower.radius, 1)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
