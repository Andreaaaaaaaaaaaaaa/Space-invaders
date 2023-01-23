import pygame
from pygame.locals import *

clock = pygame.time.Clock()
fps = 60

screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')

red = (255, 0, 0)
green = (0, 225, 0)

#load image
bg = pygame.image.load("img/bg.png")


def draw_bg():
    screen.blit(bg, (0, 0))


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_start = health
        self.health_remaining = health


spaceship_group = pygame.sprite.Group()

spaceship = Spaceship(int(screen_width / 2), screen_height - 100, 3)
spaceship_group.add(spaceship)

run = True
while run:

    clock.tick(fps)

    #draw background
    draw_bg()

    #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#    spaceship.update()

    spaceship_group.draw(screen)


    pygame.display.update()

pygame.quit()
