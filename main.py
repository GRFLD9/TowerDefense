import os

import pygame

import Tower

pygame.init()

FPS = 12
WIDTH = 1040
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
map_photo1 = pygame.sprite.Sprite()

map1 = [['g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
        ['g', '2', 'g', 'g', 'g', 'g', 'g', 'g', 'h', 'g', 'g', 'g', 'g'],
        ['g', '3', 'g', 'g', 'g', 'g', 'g', 'g', '38', 'g', 'g', 'g', 'g'],
        ['g', '4', 'g', 'g', '33', '34', '35', '36', '37', 'g', 'g', 'g', 'g'],
        ['g', '5', 'g', 'g', '32', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
        ['g', '6', 'g', 'g', '31', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
        ['g', '7', 'g', 'g', '30', '29', '28', '27', '26', '25', '24', '23', 'g'],
        ['g', '8', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', '22', 'g'],
        ['g', '9', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', '21', 'g'],
        ['g', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 'g']]


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
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

    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


def load_image(name):
    try:
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            raise SystemExit
        image = pygame.image.load(fullname)
        return image
    except:
        print(f"Не удалось загрузить изображение {fullname} не найден")


class Game:
    def __init__(self):
        pass


map_photo1.image = load_image("map_photo1.png")
map_photo1.rect = map_photo1.image.get_rect()
map_photo1.rect.x = 0
map_photo1.rect.y = 0
all_sprites.add(map_photo1)
skelet = AnimatedSprite(load_image("mobs/skelets.png"), 6, 2, 37, 50)
skelet_x = 1
skelet_y = 0
last_skelet_y = skelet.rect.y
last_skelet_x = skelet.rect.x
skelet_count = 1


def main():
    global skelet_x, skelet_y, last_skelet_x, last_skelet_y, skelet_count
    running = True
    tower_sprites = pygame.sprite.Group()
    mob_sprites = pygame.sprite.Group()
    mob_sprites.add(skelet)
    selected_tower = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if selected_tower and not selected_tower.placed:
                        selected_tower.placed = True
                        tower_sprites.add(selected_tower)
                        selected_tower = None
                    else:
                        selected_tower = Tower.Tower(event.pos[0], event.pos[1], "tower.png", 100, 50)
        if skelet_y >= 0 and skelet_y < len(map1) - 1:
            if map1[skelet_y + 1][skelet_x].isdigit() and skelet_count + 1 == int(map1[skelet_y + 1][skelet_x]):
                skelet.rect.y += 10
                if skelet.rect.y == last_skelet_y + 80:
                    skelet_y += 1
                    last_skelet_y = skelet.rect.y
                    skelet_count += 1
        if skelet_y <= len(map1) - 1:
            if map1[skelet_y - 1][skelet_x].isdigit() and skelet_count + 1 == int(map1[skelet_y - 1][skelet_x]):
                skelet.rect.y -= 10
                if skelet.rect.y == last_skelet_y - 80:
                    skelet_y -= 1
                    last_skelet_y = skelet.rect.y
                    skelet_count += 1
        if skelet_x >= 0 and skelet_x < len(map1[skelet_y]):
            if map1[skelet_y][skelet_x + 1].isdigit() and skelet_count + 1 == int(map1[skelet_y][skelet_x + 1]):
                skelet.rect.x += 10
                if skelet.rect.x == last_skelet_x + 80:
                    skelet_x += 1
                    last_skelet_x = skelet.rect.x
                    skelet_count += 1
            if map1[skelet_y][skelet_x - 1].isdigit() and skelet_count + 1 == int(map1[skelet_y][skelet_x - 1]):
                skelet.rect.x -= 10
                if skelet.rect.x == last_skelet_x - 80:
                    skelet_x -= 1
                    last_skelet_x = skelet.rect.x
                    skelet_count += 1
        skelet.draw(screen)
        screen.fill(pygame.Color("black"))
        all_sprites.draw(screen)
        all_sprites.update()
        for tower in tower_sprites:
            tower.update(mob_sprites)
            tower.update_bullets()
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
            pygame.draw.circle(screen, (255, 0, 0), selected_tower.rect.center, selected_tower.radius, 1)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
