"""
For parsing the config.yaml file
"""

import pygame
import os.path
import yaml
import values


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
                        values.Theme.background_img = pygame.image.load(
                            os.path.join(
                                "../../assets/images",
                                v["backgroundImage"]
                            )
                        )

                    # Colours
                    values.Theme.primary_colour = eval(v["Colours"]["primary"])
                    values.Theme.secondary_colour = eval(v["Colours"]["secondary"])
                    values.Theme.background_colour = eval(v["Colours"]["background"])

                    # Fonts
                    if bool(v["Font"]["useGlobal"]):
                        values.Theme.clock_font = pygame.font.Font(
                            os.path.join("../../assets/fonts",
                                         v["Font"]["globalFont"]),
                            int(v["Font"]["clockFontSize"])
                        )

                        values.Theme.device_info_font = pygame.font.Font(
                            os.path.join("../../assets/fonts",
                                         v["Font"]["globalFont"]),
                            int(v["Font"]["deviceInfoFontSize"])
                        )
                    else:
                        values.Theme.clock_font = pygame.font.Font(
                            os.path.join("../../assets/fonts",
                                         v["Font"]["clockFont"]),
                            int(v["Font"]["clockFontSize"])
                        )

                        values.Theme.device_info_font = pygame.font.Font(
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
                    values.Services.clock_enabled = bool(v["Clock"]["enabled"])
                    values.Services.clock_format = v["Clock"]["format"]
                    values.Services.clock_x = int(v["Clock"]["x"])
                    values.Services.clock_y = int(v["Clock"]["y"])

                    # Device Info
                    values.Services.device_info_enabled = bool(v["DeviceInfo"]["enabled"])
                    values.Services.device_info_line_height = int(v["DeviceInfo"]["lineHeight"])
                    values.Services.device_info_x = int(v["DeviceInfo"]["x"])
                    values.Services.device_info_y = int(v["DeviceInfo"]["y"])
                except KeyError:
                    print("KeyError: Failed to load service configuration. Reverting to default values.")
                except NameError:
                    print("NameError: Failed to load service configuration. Reverting to default values.")
                except:
                    print("Unknown Error: Failed to load service configuration. Reverting to default values.")
            elif k == "Settings":  # Get application settings
                try:
                    values.Settings.fps = int(v["fps"])
                except KeyError:
                    print("KeyError: Failed to load settings configuration. Reverting to default values.")
                except NameError:
                    print("NameError: Failed to load settings configuration. Reverting to default values.")
                except:
                    print("Unknown Error: Failed to load settings configuration. Reverting to default values.")
