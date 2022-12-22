"""
For all the different services available.
"""
import datetime
import platform
import socket
import GPUtil
import psutil
from values import *


def manage_services():
    """
    Decides which services should be run.
    """
    if Services.clock_enabled:
        clock()

    if Services.device_info_enabled:
        device_info()

    if Services.music_enabled:
        draw_music()

    if Services.games_enabled:
        games_menu()


def clock():
    """
    Draws the clock service onto the screen using the configuration provided by values.py
    """
    current_time = datetime.datetime.now().strftime(Services.clock_format)

    Values.screen.blit(
        Theme.clock_font.render(current_time, True, Theme.primary_colour),
        (Services.clock_x, Services.clock_y)
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
        Values.screen.blit(
            Theme.device_info_font.render(i, True, Theme.primary_colour),
            (Services.device_info_x, Services.device_info_y +
             (Services.device_info_line_height * info.index(i)))
        )


def init_music():
    """
    Initialises the playlist for the music service
    """
    pygame.mixer.music.set_endevent(pygame.USEREVENT+1)  # Sets an event which will run when a song ends

    try:
        pygame.mixer.music.load(Services.playlist[0])
    except pygame.error:
        print("pygame.error: Failed to load music. Disabling service.")
        Services.music_enabled = False
    except:
        print("Unknown error: Failed to load music. Disabling service.")
        Services.music_enabled = False

    # Moves the song to the end of the playlist
    Services.playlist.append(Services.playlist[0])
    Services.playlist.pop(0)


def draw_music():
    """
    Draws the music service
    """
    # Draw pause button when playing
    if pygame.mixer.music.get_busy():
        Values.screen.blit(
            Services.pause_icon,
            (Services.music_btn_x, Services.music_btn_y)
        )
    else:  # Draw play button when paused or not playing
        Values.screen.blit(
            Services.play_icon,
            (Services.music_btn_x, Services.music_btn_y)
        )


def manage_music(e):
    """
    For managing the music service
    :param e: pygame event
    """
    if e.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Input for the music service
        if Services.music_enabled:
            btn_x = Services.music_btn_x
            btn_y = Services.music_btn_y
            width = Services.play_icon.get_width()
            height = Services.play_icon.get_height()

            # Assumes the play button and pause button are the same size
            if btn_x < mouse_x < btn_x + width and \
                    btn_y < mouse_y < btn_y + height:
                # If music is playing, pause it
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    # If music is not playing but has been started
                    if Services.music_playing:
                        pygame.mixer.music.unpause()
                    else:  # If music has not been started
                        pygame.mixer.music.play()
                        Services.music_playing = True

    # When music ends
    if e.type == pygame.mixer.music.get_endevent():
        try:
            pygame.mixer.music.load(Services.playlist[0])  # Loads the next song
            pygame.mixer.music.play()  # Plays it
            # Moves the song to the end of the playlist
            Services.playlist.append(Services.playlist[0])
            Services.playlist.pop(0)
        except pygame.error:
            print("pygame.error: Failed to load music. Disabling service.")
            Services.music_enabled = False
        except:
            print("Unknown error: Failed to load music. Disabling service.")
            Services.music_enabled = False


def games_menu():
    """
    Either draws the button to open the game menu or draws the game menu
    """
    if Services.games_menu_open:
        Values.screen.fill(Theme.background_colour)
        Values.screen.blit(Services.games_menu_cross,
                                  (Services.games_menu_cross_x, Services.games_menu_cross_y))

        for g in Services.games_menu_items:
            g.draw()
    else:
        Values.screen.blit(
            Services.games_menu_btn,
            (Services.games_menu_btn_x, Services.games_menu_btn_y)
        )

def manage_games_menu(e):
    """
    Check if a game menu item is pressed.
    """
    if Services.games_menu_open:
        for g in Services.games_menu_items:
            g.is_pressed(e)

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if Services.games_menu_cross_x < mouse_x < Services.games_menu_cross_x + \
                    Services.games_menu_cross.get_width() and \
                    Services.games_menu_cross_y < mouse_y < Services.games_menu_cross_y + \
                    Services.games_menu_cross.get_height():
                Services.games_menu_open = False

    if e.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if Services.games_menu_btn_x < mouse_x < Services.games_menu_btn_x + \
                Services.games_menu_btn.get_width() and \
                Services.games_menu_btn_y < mouse_y < Services.games_menu_btn_y + \
                Services.games_menu_btn.get_height():
            Services.games_menu_open = True
