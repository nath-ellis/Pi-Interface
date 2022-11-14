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
    Runs 30 times per second.
    """
    values.Values.pygame_clock.tick(values.Settings.fps)
    pygame.display.update()
    values.Values.screen.fill(values.Theme.background_colour)


def main():
    """
    Main
    """
    pygame.init()
    config.init()
    pygame.display.set_caption("Pi Interface")

    running = True

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        services.manage_services()

        redraw()

if __name__ == "__main__":
    main()
    pygame.quit()
    quit()
