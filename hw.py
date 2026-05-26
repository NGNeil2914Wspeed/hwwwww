import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60

CHANGE_COLOR = pygame.USEREVENT + 1

pygame.time.set_timer(CHANGE_COLOR, 1000)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()

        self.image = pygame.Surface((100, 100))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

all_sprites = pygame.sprite.Group()

sprite1 = Sprite(100, 200, (255, 0, 0))
sprite2 = Sprite(400, 200, (0, 0, 255))

all_sprites.add(sprite1, sprite2)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == CHANGE_COLOR:

            sprite1_color = random.choice([
                (255, 0, 0),
                (0, 255, 0),
                (0, 0, 255)
            ])

            sprite2_color = random.choice([
                (255, 255, 0),
                (255, 0, 255),
                (0, 255, 255)
            ])

            sprite1.image.fill(sprite1_color)
            sprite2.image.fill(sprite2_color)

    screen.fill((30, 30, 30))

    all_sprites.draw(screen)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()