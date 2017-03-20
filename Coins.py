import pygame
import random

YELLOW = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (255, 0, 0)


class Coins(pygame.sprite.Sprite):


    def __init__(self, color, width, height):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

pygame.init()

w = 500
h = 500
screen = pygame.display.set_mode([w, h])

coins_list = pygame.sprite.Group()

sprites = pygame.sprite.Group()

for i in range(50):

    coin = Coins(YELLOW, 20, 15)

    coin.rect.x = random.randrange(w)
    coin.rect.y = random.randrange(h)

    coins_list.add(coin)
    sprites.add(coin)

character = Coins(GREEN, 20, 15)
sprites.add(character)

done = False

clock = pygame.time.Clock()

score = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    pos = pygame.mouse.get_pos()

    character.rect.x = pos[0]
    character.rect.y = pos[1]

    hit_coins = pygame.sprite.spritecollide(character, coins_list, True)

    for block in hit_coins:
        score += 1
        print(score)

    sprites.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()