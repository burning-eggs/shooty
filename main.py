import pygame
import sys

pygame.init()

display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

while True:
    display.fill((0, 0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    clock.tick(60)
    pygame.display.update()
