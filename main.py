"""
Main python file
"""

import pygame
from pygame import *
import yaml

pygame.init()
running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((480, 320))
pygame.display.set_caption("Pi Interface")

global primary_colour, secondary_colour, background_colour  # Global colour values

config = yaml.load_all(open("config.yaml"), Loader=yaml.FullLoader)  # Load the full file

for c in config:  # Iterates over the yaml documents
    for k, v in c.items():  # Iterates over the items in the document
        if k == "Theme":  # Get the theme from the yaml
            primary_colour = eval(v["primary"])
            secondary_colour = eval(v["secondary"])
            background_colour = eval(v["background"])


def redraw():
    """
    Clears the window and redraws everything.
    Runs 30 times per second.
    """
    clock.tick(30)
    pygame.display.update()

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    redraw()

pygame.quit()
quit()
