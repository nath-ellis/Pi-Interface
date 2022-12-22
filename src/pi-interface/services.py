"""
For all the different services available.
"""
import datetime
import platform
import socket
import GPUtil
import psutil
from values import *


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
            str(round(GPUtil.getGPUs()[0].load * 100, 2)) + "% GPU Usage",
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
        self.x = x
        self.y = y
        self.play_icon = pygame.image.load(
            os.path.join("../../assets/icons", "play.png")
        )
        self.pause_icon = pygame.image.load(
            os.path.join("../../assets/icons", "pause.png")
        )


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
            Values.screen.blit(
                self.pause_icon, (self.x, self.y)
            )
        else:  # Draw play button when paused or not playing
            Values.screen.blit(
                self.play_icon, (self.x, self.y)
            )


    def manage(self, e):
        """
        For managing the music service
        :param e: pygame event
        """

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Input for the music service
            if self.enabled:
                width = self.play_icon.get_width()
                height = self.play_icon.get_height()

                # Assumes the play button and pause button are the same size
                if self.x < mouse_x < self.x + width and self.y < mouse_y < self.y + height:
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


class GamesMenuItem:
    """
    An item on the game menu
    """

    def __init__(self, x, y, name, icon):
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.name = name
        self.icon = pygame.image.load(
            os.path.join("../../assets/icons/game", icon)
        )

    def draw(self):
        """
        Draws the menu item
        """

        Values.screen.blit(self.icon, (self.x, self.y))

    def is_pressed(self, e):
        """
        Check whether it has been pressed or not
        :param e: pygame event
        """

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if self.x < mouse_x < self.x + self.width and \
                    self.y < mouse_y < self.y + self.height:
                print(self.name + " Pressed")


class Games:
    """
    The Games Service
    """


    def __init__(self, btn_x, btn_y, cross_x, cross_y):
        self.enabled = True
        self.menu_open = False
        self.btn = pygame.image.load(
            os.path.join("../../assets/icons", "games.png")
        )
        self.btn_x = btn_x
        self.btn_y = btn_y
        self.cross = pygame.image.load(
            os.path.join("../../assets/icons", "cross.png")
        )
        self.cross_x = cross_x
        self.cross_y = cross_y
        self.menu_items = []


    def menu(self):
        """
        Either draws the button to open the game menu or draws the game menu
        """

        if self.menu_open:
            Values.screen.fill(Theme.background_colour)
            Values.screen.blit(self.cross, (self.cross_x, self.cross_y))

            for m in self.menu_items:
                m.draw()
        else:
            Values.screen.blit(
                self.btn, (self.btn_x, self.btn_y)
            )


    def manage_menu(self, e):
        """
        Check if a game menu item is pressed.
        :param e: pygame event
        """

        if self.menu_open:
            for g in self.menu_items:
                g.is_pressed(e)

            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if self.cross_x < mouse_x < self.cross_x + self.cross.get_width() and \
                        self.cross_y < mouse_y < self.cross_y + self.cross.get_height():
                    self.menu_open = False
        else:
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if self.btn_x < mouse_x < self.btn_x + self.btn.get_width() and \
                        self.btn_y < mouse_y < self.btn_y + self.btn.get_height():
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
