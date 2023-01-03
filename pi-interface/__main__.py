"""
__main__.py
"""

import os

os.chdir(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

from pygame import *
import config
from values import *
from services import services

def redraw():
    """
    Clears the window and redraws everything.
    Runs a given amount of times per second using the fps value provided by config.yaml.
    """
    Values.pygame_clock.tick(Settings.fps)
    pygame.display.update()
    Values.screen.fill(Theme.background_colour)

    if Theme.background_img is not None:
        Values.screen.blit(Theme.background_img, (0, 0))


def main():
    """
    Main
    """
    pygame.init()
    config.init()
    pygame.display.set_caption("Pi Interface")
    pygame.event.set_allowed([QUIT, MOUSEBUTTONDOWN])

    if Theme.fullscreen:
        pygame.display.set_mode((0, 0), FULLSCREEN | DOUBLEBUF)

    if not Theme.mouse_cursor_visible:
        # Makes cursor invisible
        pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))

    if services.music.enabled:
        services.music.init_playlist()

    while Values.running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                Values.running = False

            if services.exit.enabled:
                services.exit.manage(e)

            if services.music.enabled:
                services.music.manage(e)

            if services.games.enabled:
                services.games.manage_controls(e)

        services.manage()

        redraw()

if __name__ == "__main__":
    main()
    pygame.quit()
    quit()
