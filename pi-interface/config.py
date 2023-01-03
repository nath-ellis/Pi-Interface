"""
For parsing the config.yaml file
"""

import os.path
import yaml
from values import *
from services import services


def init():
    """
    Parses the config.yaml file and gets the values provided
    """

    config = yaml.load_all(open("../config.yaml"), Loader=yaml.FullLoader)  # Load the full file

    for c in config:  # Iterates over the yaml documents
        for k, v in c.items():  # Iterates over the items in the document
            if k == "Theme":  # Get the theme from the yaml
                try:
                    # Background Image
                    if v["backgroundImage"] != "":
                        Theme.background_img = pygame.image.load(
                            os.path.join(
                                "../assets/images",
                                v["backgroundImage"]
                            )
                        ).convert_alpha()

                    # Fullscreen
                    Theme.fullscreen = bool(v["fullscreen"])

                    # Mouse Cursor Visibility
                    Theme.mouse_cursor_visible = bool(v["mouseCursorVisible"])

                    # Colours
                    Theme.primary_colour = eval(v["Colours"]["primary"])
                    Theme.secondary_colour = eval(v["Colours"]["secondary"])
                    Theme.background_colour = eval(v["Colours"]["background"])

                    # Fonts
                    if bool(v["Font"]["useGlobal"]):
                        Theme.clock_font = pygame.font.Font(
                            os.path.join("../assets/fonts",
                                         v["Font"]["globalFont"]),
                            int(v["Font"]["clockFontSize"])
                        )

                        Theme.device_info_font = pygame.font.Font(
                            os.path.join("../assets/fonts",
                                         v["Font"]["globalFont"]),
                            int(v["Font"]["deviceInfoFontSize"])
                        )
                    else:
                        Theme.clock_font = pygame.font.Font(
                            os.path.join("../assets/fonts",
                                         v["Font"]["clockFont"]),
                            int(v["Font"]["clockFontSize"])
                        )

                        Theme.device_info_font = pygame.font.Font(
                            os.path.join("../assets/fonts",
                                         v["Font"]["deviceInfoFont"]),
                            int(v["Font"]["deviceInfoFontSize"])
                        )
                except KeyError:
                    print("KeyError: Failed to load theme configuration. Reverting to default values.")
                except NameError:
                    print("NameError: Failed to load theme configuration. Reverting to default values.")
                except:
                    print("Unknown Error: Failed to load theme configuration. Reverting to default values.")
            elif k == "Services":  # Get service settings
                try:
                    # Exit
                    services.exit.enabled = bool(v["ExitBtn"]["enabled"])
                    services.exit.btn.x = int(v["ExitBtn"]["x"])
                    services.exit.btn.y = int(v["ExitBtn"]["y"])
                    services.exit.btn.icon = pygame.image.load(
                        os.path.join("../assets/icons", v["ExitBtn"]["icon"])
                    ).convert_alpha()

                    # Clock
                    services.clock.enabled = bool(v["Clock"]["enabled"])
                    services.clock.format = v["Clock"]["format"]
                    services.clock.x = int(v["Clock"]["x"])
                    services.clock.y = int(v["Clock"]["y"])

                    # Device Info
                    services.device_info.enabled = bool(v["DeviceInfo"]["enabled"])
                    services.device_info.line_height = int(v["DeviceInfo"]["lineHeight"])
                    services.device_info.x = int(v["DeviceInfo"]["x"])
                    services.device_info.y = int(v["DeviceInfo"]["y"])

                    # Music
                    services.music.enabled = bool(v["Music"]["enabled"])
                    for p in v["Music"]["playlist"]:
                        services.music.playlist.append(
                            os.path.join("../assets/music", p)
                        )
                    services.music.play_btn.x = int(v["Music"]["btnX"])
                    services.music.play_btn.y = int(v["Music"]["btnY"])
                    services.music.play_btn.icon = pygame.image.load(
                        os.path.join("../assets/icons", v["Music"]["playIcon"])
                    ).convert_alpha()
                    services.music.pause_btn.x = int(v["Music"]["btnX"])
                    services.music.pause_btn.y = int(v["Music"]["btnY"])
                    services.music.pause_btn.icon = pygame.image.load(
                        os.path.join("../assets/icons", v["Music"]["pauseIcon"])
                    ).convert_alpha()

                    # Games
                    services.games.enabled = bool(v["Games"]["enabled"])
                    services.games.open_btn.x = int(v["Games"]["iconX"])
                    services.games.open_btn.y = int(v["Games"]["iconY"])
                    services.games.open_btn.icon = pygame.image.load(
                        os.path.join("../assets/icons", v["Games"]["icon"])
                    ).convert_alpha()
                    services.games.close_btn.x = int(v["Games"]["crossX"])
                    services.games.close_btn.y = int(v["Games"]["crossY"])
                    services.games.close_btn.icon = pygame.image.load(
                        os.path.join("../assets/icons", v["Games"]["crossIcon"])
                    ).convert_alpha()
                except KeyError:
                    print("KeyError: Failed to load service configuration. Reverting to default values.")
                except NameError:
                    print("NameError: Failed to load service configuration. Reverting to default values.")
                except:
                    print("Unknown Error: Failed to load service configuration. Reverting to default values.")
            elif k == "Settings":  # Get application settings
                try:
                    Settings.fps = int(v["fps"])
                except KeyError:
                    print("KeyError: Failed to load settings configuration. Reverting to default values.")
                except NameError:
                    print("NameError: Failed to load settings configuration. Reverting to default values.")
                except:
                    print("Unknown Error: Failed to load settings configuration. Reverting to default values.")
