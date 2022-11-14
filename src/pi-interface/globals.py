"""
For global variables which need to be accessed from multiple areas of the project
"""

import os.path
import pygame


class Values:
    """
    For global variables
    """
    pygame_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((480, 320))

    # Colours
    primary_colour = (108, 204, 98)
    secondary_colour = (98, 204, 141)
    background_colour = (0, 0, 0)

    # Fonts
    pygame.font.init()
    global_font = pygame.font.Font(os.path.join("../../fonts", "embodial.ttf"), 50)
    clock_font = pygame.font.Font(os.path.join("../../fonts", "apollo.ttf"), 50)

    # Services
    clock_enabled = True
    clock_format = "%H:%M"
    clock_x = 10
    clock_y = 220

    # Settings
    fps = 30
