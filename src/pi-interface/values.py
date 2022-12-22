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

    # Music
    music_enabled = True
    music_playing = False
    playlist = []
    music_btn_x = 390
    music_btn_y = 220
    play_icon = pygame.image.load(
        os.path.join("../../assets/icons", "play.png")
    )
    pause_icon = pygame.image.load(
        os.path.join("../../assets/icons", "pause.png")
    )

    # Games
    games_enabled = True
    games_menu_open = False
    games_menu_btn = pygame.image.load(
        os.path.join("../../assets/icons", "games.png")
    )
    games_menu_btn_x = 438
    games_menu_btn_y = 10
    games_menu_cross = pygame.image.load(
        os.path.join("../../assets/icons", "cross.png")
    )
    games_menu_cross_x = 10
    games_menu_cross_y = 10

    class GameMenuItem:
        """
        An item on the game menu
        """

        def __init__(self, x, y, name, icon):
            self.x = x
            self.y = y
            self.width = 64
            self.height = 64
            self.name = name
            self.icon = pygame.image.load(
                os.path.join("../../assets/icons/game", icon)
            )

        def draw(self):
            """
            Draws the menu item
            """
            Values.screen.blit(self.icon, (self.x, self.y))

        def is_pressed(self, e):
            """
            Check whether it has been pressed or not
            :param e: pygame event
            """
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if self.x < mouse_x < self.x + self.width and \
                        self.y < mouse_y < self.y +self.height:
                    print(self.name + " Pressed")


    games_menu_items = []


class Settings:
    """
    For global settings
    """
    fps = 30
