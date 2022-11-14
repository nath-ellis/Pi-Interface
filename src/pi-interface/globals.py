"""
For global variables which need to be accessed from multiple areas of the project
"""

import pygame


class Values:
    """
    For global variables
    """
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((480, 320))

    # Colours
    primary_colour = (108, 204, 98)
    secondary_colour = (98, 204, 141)
    background_colour = (0, 0, 0)

    # Services
    clock_enabled = True

    # Settings
    fps = 30
