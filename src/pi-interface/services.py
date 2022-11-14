"""
For all the different services available.
"""
import datetime
import globals


def manage_services():
    """
    Decides which services should be run.
    """
    if globals.Services.clock_enabled:
        clock()


def clock():
    """
    Draws the clock service onto the screen using the configuration provided by globals.py
    """
    current_time = datetime.datetime.now().strftime(globals.Services.clock_format)

    globals.Values.screen.blit(
        globals.Theme.clock_font.render(current_time, True, globals.Theme.primary_colour),
        (globals.Services.clock_x, globals.Services.clock_y)
    )
