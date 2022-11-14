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
    globals.Values.pygame_clock.tick(globals.Values.fps)
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

        globals.Values.screen.blit(
            globals.Values.global_font.render("Global Font", True, globals.Values.primary_colour),
            (10, 10)
        )
        globals.Values.screen.blit(
            globals.Values.clock_font.render("Clock Font", True, globals.Values.primary_colour),
            (10, 100)
        )

        redraw()

if __name__ == "__main__":
    main()
    pygame.quit()
    quit()
