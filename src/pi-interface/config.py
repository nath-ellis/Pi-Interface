"""
For parsing the config.yaml file
"""

import os.path
import yaml
from values import *


def init():
    """
    Parses the config.yaml file and gets the values provided
    """

    config = yaml.load_all(open("../../config.yaml"), Loader=yaml.FullLoader)  # Load the full file

    for c in config:  # Iterates over the yaml documents
        for k, v in c.items():  # Iterates over the items in the document
            if k == "Theme":  # Get the theme from the yaml
                try:
                    # Background Image
                    if v["backgroundImage"] != "":
                        Theme.background_img = pygame.image.load(
                            os.path.join(
                                "../../assets/images",
                                v["backgroundImage"]
                            )
                        )

                    # Colours
                    Theme.primary_colour = eval(v["Colours"]["primary"])
                    Theme.secondary_colour = eval(v["Colours"]["secondary"])
                    Theme.background_colour = eval(v["Colours"]["background"])

                    # Fonts
                    if bool(v["Font"]["useGlobal"]):
                        Theme.clock_font = pygame.font.Font(
                            os.path.join("../../assets/fonts",
                                         v["Font"]["globalFont"]),
                            int(v["Font"]["clockFontSize"])
                        )

                        Theme.device_info_font = pygame.font.Font(
                            os.path.join("../../assets/fonts",
                                         v["Font"]["globalFont"]),
                            int(v["Font"]["deviceInfoFontSize"])
                        )
                    else:
                        Theme.clock_font = pygame.font.Font(
                            os.path.join("../../assets/fonts",
                                         v["Font"]["clockFont"]),
                            int(v["Font"]["clockFontSize"])
                        )

                        Theme.device_info_font = pygame.font.Font(
                            os.path.join("../../assets/fonts",
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
                    # Clock
                    Services.clock_enabled = bool(v["Clock"]["enabled"])
                    Services.clock_format = v["Clock"]["format"]
                    Services.clock_x = int(v["Clock"]["x"])
                    Services.clock_y = int(v["Clock"]["y"])

                    # Device Info
                    Services.device_info_enabled = bool(v["DeviceInfo"]["enabled"])
                    Services.device_info_line_height = int(v["DeviceInfo"]["lineHeight"])
                    Services.device_info_x = int(v["DeviceInfo"]["x"])
                    Services.device_info_y = int(v["DeviceInfo"]["y"])

                    # Music
                    Services.music_enabled = bool(v["Music"]["enabled"])
                    for p in v["Music"]["playlist"]:
                        Services.playlist.append(
                            os.path.join("../../assets/music", p)
                        )
                    Services.play_icon = pygame.image.load(
                        os.path.join("../../assets/icons", v["Music"]["playIcon"])
                    )
                    Services.music_btn_x = int(v["Music"]["btnX"])
                    Services.music_btn_y = int(v["Music"]["btnY"])
                    Services.pause_icon = pygame.image.load(
                        os.path.join("../../assets/icons", v["Music"]["pauseIcon"])
                    )

                    # Games
                    Services.games_enabled = bool(v["Games"]["enabled"])
                    Services.games_menu_btn = pygame.image.load(
                        os.path.join("../../assets/icons", v["Games"]["icon"])
                    )
                    Services.games_menu_btn_x = int(v["Games"]["iconX"])
                    Services.games_menu_btn_y = int(v["Games"]["iconY"])
                    Services.games_menu_cross = pygame.image.load(
                        os.path.join("../../assets/icons", v["Games"]["crossIcon"])
                    )
                    Services.games_menu_cross_x = int(v["Games"]["crossX"])
                    Services.games_menu_cross_y = int(v["Games"]["crossY"])
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
