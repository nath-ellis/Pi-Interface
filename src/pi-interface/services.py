"""
For all the different services available.
"""
import datetime
import globals


def manage_services():
    """
    Decides which services should be run.
    """
    if globals.Values.clock_enabled:
        clock()


def clock():
    """
    Draws the clock service onto the screen using the configuration provided by globals.py
    """
    current_time = datetime.datetime.now().strftime(globals.Values.clock_format)

    globals.Values.screen.blit(
        globals.Values.clock_font.render(current_time, True, globals.Values.primary_colour),
        (globals.Values.clock_x, globals.Values.clock_y)
    )
