"""
For all the different services available.
"""
import datetime
import platform
import socket
import GPUtil
import psutil
import values


def manage_services():
    """
    Decides which services should be run.
    """
    if values.Services.clock_enabled:
        clock()

    if values.Services.device_info_enabled:
        device_info()


def clock():
    """
    Draws the clock service onto the screen using the configuration provided by values.py
    """
    current_time = datetime.datetime.now().strftime(values.Services.clock_format)

    values.Values.screen.blit(
        values.Theme.clock_font.render(current_time, True, values.Theme.primary_colour),
        (values.Services.clock_x, values.Services.clock_y)
    )


def device_info():
    """
    Draws the device info service onto the screen.
    """
    info = [
        socket.gethostname(),
        platform.system() + " " + platform.machine(),
        socket.gethostbyname(socket.gethostname()),
        str(round(psutil.cpu_percent(), 2)) + "% CPU Usage",
        str(round(GPUtil.getGPUs()[0].load * 100, 2)) + "% GPU Usage",
        str(round(psutil.virtual_memory().percent, 2)) + "% Memory Usage",
        str(round(psutil.disk_usage("/").percent, 2)) + "% Disk Usage"
    ]

    # Draws the devices info onto the screen with the correct line height between it
    for i in info:
        values.Values.screen.blit(
            values.Theme.device_info_font.render(i, True, values.Theme.primary_colour),
            (values.Services.device_info_x, values.Services.device_info_y +
             (values.Services.device_info_line_height * info.index(i)))
        )
