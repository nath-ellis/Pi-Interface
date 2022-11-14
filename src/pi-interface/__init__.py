"""
__init__.py
"""

import pygame
from pygame import *
import config
import globals


def redraw():
    """
    Clears the window and redraws everything.
    Runs 30 times per second.
    """
    globals.Values.clock.tick(globals.Values.fps)
    pygame.display.update()


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

        redraw()

if __name__ == "__main__":
    main()
    pygame.quit()
    quit()
