"""
For all the different services available.
"""
import datetime
import os.path
import platform
import socket
import GPUtil
import psutil
import pygame
import values


def manage_services():
    """
    Decides which services should be run.
    """
    if values.Services.clock_enabled:
        clock()

    if values.Services.device_info_enabled:
        device_info()

    if values.Services.music_enabled:
        draw_music()

    if values.Services.games_enabled:
        games_menu()


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


def init_music():
    """
    Initialises the playlist for the music service
    """
    pygame.mixer.music.set_endevent(pygame.USEREVENT+1)  # Sets an event which will run when a song ends

    try:
        pygame.mixer.music.load(values.Services.playlist[0])
    except pygame.error:
        print("pygame.error: Failed to load music. Disabling service.")
        values.Services.music_enabled = False
    except:
        print("Unknown error: Failed to load music. Disabling service.")
        values.Services.music_enabled = False

    # Moves the song to the end of the playlist
    values.Services.playlist.append(values.Services.playlist[0])
    values.Services.playlist.pop(0)


def draw_music():
    """
    Draws the music service
    """
    # Draw pause button when playing
    if pygame.mixer.music.get_busy():
        values.Values.screen.blit(
            values.Services.pause_icon,
            (values.Services.music_btn_x, values.Services.music_btn_y)
        )
    else:  # Draw play button when paused or not playing
        values.Values.screen.blit(
            values.Services.play_icon,
            (values.Services.music_btn_x, values.Services.music_btn_y)
        )


def manage_music(e):
    """
    For managing the music service
    :param e: pygame event
    """
    if e.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Input for the music service
        if values.Services.music_enabled:
            btn_x = values.Services.music_btn_x
            btn_y = values.Services.music_btn_y
            width = values.Services.play_icon.get_width()
            height = values.Services.play_icon.get_height()

            # Assumes the play button and pause button are the same size
            if btn_x < mouse_x < btn_x + width and \
                    btn_y < mouse_y < btn_y + height:
                # If music is playing, pause it
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    # If music is not playing but has been started
                    if values.Services.music_playing:
                        pygame.mixer.music.unpause()
                    else:  # If music has not been started
                        pygame.mixer.music.play()
                        values.Services.music_playing = True

    # When music ends
    if e.type == pygame.mixer.music.get_endevent():
        try:
            pygame.mixer.music.load(values.Services.playlist[0])  # Loads the next song
            pygame.mixer.music.play()  # Plays it
            # Moves the song to the end of the playlist
            values.Services.playlist.append(values.Services.playlist[0])
            values.Services.playlist.pop(0)
        except pygame.error:
            print("pygame.error: Failed to load music. Disabling service.")
            values.Services.music_enabled = False
        except:
            print("Unknown error: Failed to load music. Disabling service.")
            values.Services.music_enabled = False


def games_menu():
    """
    Either draws the button to open the game menu or draws the game menu
    """
    if values.Services.games_menu_open:
        values.Values.screen.fill(values.Theme.background_colour)
        values.Values.screen.blit(values.Services.games_menu_cross,
                                  (values.Services.games_menu_cross_x, values.Services.games_menu_cross_y))

        for g in values.Services.games_menu_items:
            g.draw()
    else:
        values.Values.screen.blit(
            values.Services.games_menu_btn,
            (values.Services.games_menu_btn_x, values.Services.games_menu_btn_y)
        )

def manage_games_menu(e):
    """
    Check if a game menu item is pressed.
    """
    if values.Services.games_menu_open:
        for g in values.Services.games_menu_items:
            g.is_pressed(e)

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if values.Services.games_menu_cross_x < mouse_x < values.Services.games_menu_cross_x + \
                    values.Services.games_menu_cross.get_width() and \
                    values.Services.games_menu_cross_y < mouse_y < values.Services.games_menu_cross_y + \
                    values.Services.games_menu_cross.get_height():
                values.Services.games_menu_open = False

    if e.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if values.Services.games_menu_btn_x < mouse_x < values.Services.games_menu_btn_x + \
                values.Services.games_menu_btn.get_width() and \
                values.Services.games_menu_btn_y < mouse_y < values.Services.games_menu_btn_y + \
                values.Services.games_menu_btn.get_height():
            values.Services.games_menu_open = True
