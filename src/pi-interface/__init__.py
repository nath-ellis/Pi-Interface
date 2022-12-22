"""
__init__.py
"""

from pygame import *
import config
from values import *
import services


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

    if Services.music_enabled:
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
