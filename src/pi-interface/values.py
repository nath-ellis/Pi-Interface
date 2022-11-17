"""
For global variables which need to be accessed from multiple areas of the project
"""

import os.path
import pygame


class Values:
    """
    For miscellaneous global variables
    """
    pygame_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((480, 320))


class Theme:
    """
    For global theme configuration
    """
    # Background Image
    background_img = None

    # Colours
    primary_colour = (108, 204, 98)
    secondary_colour = (98, 204, 141)
    background_colour = (0, 0, 0)

    # Fonts
    pygame.font.init()
    global_font = pygame.font.Font(os.path.join("../../assets/fonts", "embodial.ttf"), 50)
    clock_font = pygame.font.Font(os.path.join("../../assets/fonts", "apollo.ttf"), 50)
    device_info_font = pygame.font.Font(os.path.join("../../assets/fonts", "embodial.ttf"), 25)


class Services:
    """
    For global service configurations
    """
    # Clock
    clock_enabled = True
    clock_format = "%H:%M"
    clock_x = 10
    clock_y = 220

    # Device Info
    device_info_enabled = True
    device_info_line_height = 30
    device_info_x = 10
    device_info_y = 10


class Settings:
    """
    For global settings
    """
    fps = 30
