import pygame
from pygame import *

pygame.init()
running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((480, 320))
pygame.display.set_caption("Pi Interface")

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    clock.tick(30)
    pygame.display.update()
