"""
__init__.py
"""

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

    if services.music.enabled:
        services.music.init_playlist()

    while Values.running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                Values.running = False

            services.exit.manage(e)
            services.music.manage(e)
            services.games.manage_menu(e)

        services.manage()

        redraw()

if __name__ == "__main__":
    main()
    pygame.quit()
    quit()
