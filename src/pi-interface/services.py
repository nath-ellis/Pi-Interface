"""
For all the different services available.
"""
import datetime
import platform
import socket
import GPUtil
import psutil
from values import *


class Button:
    """
    For adding buttons
    """


    def __init__(self, x, y, icon):
        self.enabled = True
        self.x = x
        self.y = y
        self.icon = pygame.image.load(
            os.path.join("../../assets/icons", icon)
        )


    def is_pressed(self, e):
        """
        Checks whether the button was pressed
        :param e: pygame event
        :return: bool
        """

        if e.type == pygame.MOUSEBUTTONDOWN and self.enabled:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if self.x < mouse_x < self.x + self.icon.get_width() and \
                    self.y < mouse_y < self.y + self.icon.get_height():
                return True

        return False


    def draw(self):
        """
        Draws the button
        """

        Values.screen.blit(
            self.icon,
            (self.x, self.y)
        )


class Clock:
    """
    The Clock Service
    """


    def __init__(self, x, y, clock_format):
        self.enabled = True
        self.x = x
        self.y = y
        self.format = clock_format
        self.current_time = datetime.datetime.now().strftime(self.format)


    def update(self):
        """
        Updates the time shown on the clock
        """

        self.current_time = datetime.datetime.now().strftime(self.format)


    def draw(self):
        """
        Draws the clock service
        """

        Values.screen.blit(
            Theme.clock_font.render(self.current_time, True, Theme.primary_colour),
            (self.x, self.y)
        )


class DeviceInfo:
    """
    The Device Info Service
    """


    def __init__(self, x, y, line_height):
        self.enabled = True
        self.x = x
        self.y = y
        self.line_height = line_height
        self.info = []


    def update(self):
        """
        Updates the info to be drawn
        """

        self.info = [
            socket.gethostname(),
            platform.system() + " " + platform.machine(),
            str(round(psutil.cpu_percent(), 2)) + "% CPU Usage",
            str(round(psutil.virtual_memory().percent, 2)) + "% Memory Usage",
            str(round(psutil.disk_usage("/").percent, 2)) + "% Disk Usage"
        ]


    def draw(self):
        """
        Draws the service
        """

        # Draws the devices info onto the screen with the correct line height between it
        for i in self.info:
            Values.screen.blit(
                Theme.device_info_font.render(i, True, Theme.primary_colour),
                (self.x, self.y + (self.line_height * self.info.index(i)))
            )


class Music:
    """
    The Music Service
    """


    def __init__(self, x, y):
        self.enabled = True
        self.playing = False
        self.playlist = []
        self.play_btn = Button(x, y, "play.png")
        self.pause_btn = Button(x, y, "pause.png")


    def init_playlist(self):
        """
        Initialises the playlist for the music service
        """

        pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)  # Sets an event which will run when a song ends

        try:
            pygame.mixer.music.load(self.playlist[0])
        except pygame.error:
            print("pygame.error: Failed to load music. Disabling service.")
            self.enabled = False
        except:
            print("Unknown error: Failed to load music. Disabling service.")
            self.enabled = False

        # Moves the song to the end of the playlist
        self.playlist.append(self.playlist[0])
        self.playlist.pop(0)


    def draw(self):
        """
        Draws the music service
        """

        # Draw pause button when playing
        if pygame.mixer.music.get_busy():
            self.play_btn.enabled = False
            self.pause_btn.enabled = True
            self.pause_btn.draw()
        else:  # Draw play button when paused or not playing
            self.play_btn.enabled = True
            self.pause_btn.enabled = False
            self.play_btn.draw()


    def manage(self, e):
        """
        For managing the music service
        :param e: pygame event
        """

        # Input for the music service
        if self.enabled:
            if self.play_btn.is_pressed(e) or self.pause_btn.is_pressed(e):
                # If music is playing, pause it
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    # If music is not playing but has been started
                    if self.playing:
                        pygame.mixer.music.unpause()
                    else:  # If music has not been started
                        pygame.mixer.music.play()
                        services.music.playing = True

        # When music ends
        if e.type == pygame.mixer.music.get_endevent():
            try:
                pygame.mixer.music.load(self.playlist[0])  # Loads the next song
                pygame.mixer.music.play()  # Plays it
                # Moves the song to the end of the playlist
                self.playlist.append(self.playlist[0])
                self.playlist.pop(0)
            except pygame.error:
                print("pygame.error: Failed to load music. Disabling service.")
                self.enabled = False
            except:
                print("Unknown error: Failed to load music. Disabling service.")
                self.enabled = False


class GamesMenuItem (Button):
    """
    An item on the game menu
    """

    def __init__(self, x, y, icon, name):
        super().__init__(x, y, icon)
        self.name = name


class Games:
    """
    The Games Service
    """


    def __init__(self, btn_x, btn_y, cross_x, cross_y):
        self.enabled = True
        self.menu_open = False
        self.open_btn = Button(btn_x, btn_y, "games.png")
        self.close_btn = Button(cross_x, cross_y, "cross.png")
        self.menu_items = []


    def menu(self):
        """
        Either draws the button to open the game menu or draws the game menu
        """

        if self.menu_open:
            Values.screen.fill(Theme.background_colour)
            self.close_btn.draw()

            for m in self.menu_items:
                m.draw()
        else:
            self.open_btn.draw()


    def manage_menu(self, e):
        """
        Check if a game menu item is pressed.
        :param e: pygame event
        """

        if self.menu_open:
            for g in self.menu_items:
                if g.is_pressed(e):
                    print(g.name)  # Launch game

            if self.close_btn.is_pressed(e):
                self.menu_open = False
        else:
            if self.open_btn.is_pressed(e):
                self.menu_open = True


class Services:
    """
    Stores and manages the instances of the services
    """


    def __init__(self):
        self.clock = Clock(10, 220, "%H:%M")
        self.device_info = DeviceInfo(10, 10 , 30)
        self.music = Music(390, 220)
        self.games = Games(438, 10, 10, 10)


    def manage(self):
        """
        Decides which services should be run
        """

        if self.clock.enabled:
            self.clock.update()
            self.clock.draw()

        if self.device_info.enabled:
            self.device_info.update()
            self.device_info.draw()

        if self.music.enabled:
            self.music.draw()

        if self.games.enabled:
            self.games.menu()


services = Services()
