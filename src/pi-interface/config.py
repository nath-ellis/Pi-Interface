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
                    # Colours
                    values.Theme.primary_colour = eval(v["Colours"]["primary"])
                    values.Theme.secondary_colour = eval(v["Colours"]["secondary"])
                    values.Theme.background_colour = eval(v["Colours"]["background"])

                    # Fonts
                    if bool(v["Font"]["useGlobal"]):
                        values.Theme.clock_font = pygame.font.Font(
                            os.path.join("../../fonts",
                                         v["Font"]["globalFont"]),
                            int(v["Font"]["clockFontSize"])
                        )
                    else:
                        values.Theme.clock_font = pygame.font.Font(
                            os.path.join("../../fonts",
                                         v["Font"]["clockFont"]),
                            int(v["Font"]["clockFontSize"])
                        )
                except KeyError:
                    print("KeyError: Failed to load theme configuration. Reverting to default values.")
                except NameError:
                    print("NameError: Failed to load theme configuration. Reverting to default values.")
                except:
                    print("Unknown Error: Failed to load theme configuration. Reverting to default values.")
            elif k == "Services":  # Get service settings
                try:
                    values.Services.clock_enabled = bool(v["Clock"]["enabled"])
                    values.Services.clock_format = v["Clock"]["format"]
                    values.Services.clock_x = int(v["Clock"]["x"])
                    values.Services.clock_y = int(v["Clock"]["y"])
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
