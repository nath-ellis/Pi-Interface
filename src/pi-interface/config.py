"""
For parsing the config.yaml file
"""

import pygame
import os.path
import yaml
import globals


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
                    globals.Theme.primary_colour = eval(v["primary"])
                    globals.Theme.secondary_colour = eval(v["secondary"])
                    globals.Theme.background_colour = eval(v["background"])

                    # Fonts
                    if bool(v["useSameFont"]):
                        globals.Theme.clock_font = pygame.font.Font(
                            os.path.join("../../fonts",
                                         v["globalFontPath"]),
                            int(v["clockFontSize"])
                        )
                    else:
                        globals.Theme.clock_font = pygame.font.Font(
                            os.path.join("../../fonts",
                                         v["clockFontPath"]),
                            int(v["clockFontSize"])
                        )
                except KeyError:
                    print("KeyError: Failed to load theme configuration. Reverting to default values.")
                except NameError:
                    print("NameError: Failed to load theme configuration. Reverting to default values.")
                except:
                    print("Unknown Error: Failed to load theme configuration. Reverting to default values.")
            elif k == "Services":  # Get service settings
                try:
                    globals.Services.clock_enabled = bool(v["clock"])
                    globals.Services.clock_format = v["clockFormat"]
                    globals.Services.clock_x = int(v["clockX"])
                    globals.Services.clock_y = int(v["clockY"])
                except KeyError:
                    print("KeyError: Failed to load service configuration. Reverting to default values.")
                except NameError:
                    print("NameError: Failed to load service configuration. Reverting to default values.")
                except:
                    print("Unknown Error: Failed to load service configuration. Reverting to default values.")
            elif k == "Settings":  # Get application settings
                try:
                    globals.Settings.fps = int(v["fps"])
                except KeyError:
                    print("KeyError: Failed to load settings configuration. Reverting to default values.")
                except NameError:
                    print("NameError: Failed to load settings configuration. Reverting to default values.")
                except:
                    print("Unknown Error: Failed to load settings configuration. Reverting to default values.")