"""
For all the different services available.
"""
import datetime
import values


def manage_services():
    """
    Decides which services should be run.
    """
    if values.Services.clock_enabled:
        clock()


def clock():
    """
    Draws the clock service onto the screen using the configuration provided by values.py
    """
    current_time = datetime.datetime.now().strftime(values.Services.clock_format)

    values.Values.screen.blit(
        values.Theme.clock_font.render(current_time, True, values.Theme.primary_colour),
        (values.Services.clock_x, values.Services.clock_y)
    )
