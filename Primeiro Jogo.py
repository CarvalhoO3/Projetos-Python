import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 1920, 1080
TILE_SIZE = 40
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)

PLAYER_SPEED = 5
PROJECTILE_SPEED = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Roguelike Game")
clock = pygame.time.Clock()

default_font = pygame.font.Font(None, 36)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.health = 100
        self.direction = (1, 0)

    def move(self, dx=0, dy=0):
        self.rect.x += dx
        self.rect.y += dy
        if dx > 0:
            self.direction = (1, 0)
        elif dx < 0:
            self.direction = (-1, 0)
        elif dy > 0:
            self.direction = (0, 1)
        elif dy < 0:
            self.direction = (0, -1)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.move(-PLAYER_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            self.move(PLAYER_SPEED, 0)
        if keys[pygame.K_UP]:
            self.move(0, -PLAYER_SPEED)
        if keys[pygame.K_DOWN]:
            self.move(0, PLAYER_SPEED)

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction

    def update(self):
        self.rect.x += self.direction[0] * PROJECTILE_SPEED
        self.rect.y += self.direction[1] * PROJECTILE_SPEED
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        if player.rect.x > self.rect.x:
            self.rect.x += 2
        if player.rect.x < self.rect.x:
            self.rect.x -= 2
        if player.rect.y > self.rect.y:
            self.rect.y += 2
        if player.rect.y < self.rect.y:
            self.rect.y -= 2

def spawn_enemy():
    x = random.randint(0, WIDTH - TILE_SIZE)
    y = random.randint(0, HEIGHT - TILE_SIZE)
    enemy = Enemy(x, y)
    enemies.add(enemy)
    all_sprites.add(enemy)

def main():
    global player, enemies, all_sprites

    player = Player(WIDTH // 2, HEIGHT // 2)
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()

    all_sprites.add(player)

    for _ in range(10):
        spawn_enemy()

    enemy_spawn_timer = 10

    running = True
    while running:
        clock.tick(FPS)
        enemy_spawn_timer += 1

        if enemy_spawn_timer >= 60:
            spawn_enemy()
            enemy_spawn_timer = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                projectile = Projectile(player.rect.centerx, player.rect.centery, player.direction)
                projectiles.add(projectile)
                all_sprites.add(projectile)

        keys = pygame.key.get_pressed()
        player.update(keys)
        enemies.update()
        projectiles.update()

        for projectile in projectiles:
            hit_enemies = pygame.sprite.spritecollide(projectile, enemies, True)
            if hit_enemies:
                projectile.kill()

        if pygame.sprite.spritecollideany(player, enemies):
            player.health -= 1
            if player.health <= 0:
                running = False

        screen.fill(BLACK)
        all_sprites.draw(screen)
        draw_text(f"Health: {player.health}", default_font, WHITE, screen, WIDTH // 2, 20)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
