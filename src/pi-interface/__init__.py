"""
__init__.py
"""

import pygame
from pygame import *
import config
import values
import services


def redraw():
    """
    Clears the window and redraws everything.
    Runs a given amount of times per second using the fps value provided by config.yaml.
    """
    values.Values.pygame_clock.tick(values.Settings.fps)
    pygame.display.update()
    values.Values.screen.fill(values.Theme.background_colour)

    if values.Theme.background_img is not None:
        values.Values.screen.blit(values.Theme.background_img, (0, 0))


def main():
    """
    Main
    """
    pygame.init()
    config.init()
    pygame.display.set_caption("Pi Interface")

    if values.Services.music_enabled:
        services.init_music()

    running = True

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            services.manage_music(e)
            services.manage_games_menu(e)

        services.manage_services()

        redraw()

if __name__ == "__main__":
    main()
    pygame.quit()
    quit()
