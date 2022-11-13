"""
For global variables which need to be accessed from multiple areas of the project
"""

import pygame


def init():
    """
    Initialises the global variables
    """
    global clock, screen, primary_colour, secondary_colour, background_colour  # Global values

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((480, 320))
