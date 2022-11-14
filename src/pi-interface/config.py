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
                    globals.Values.primary_colour = eval(v["primary"])
                    globals.Values.secondary_colour = eval(v["secondary"])
                    globals.Values.background_colour = eval(v["background"])

                    # Fonts
                    if bool(v["useSameFont"]):
                        globals.Values.clock_font = pygame.font.Font(
                            os.path.join("../../fonts",
                                         v["globalFontPath"]),
                            int(v["clockFontSize"])
                        )
                    else:
                        globals.Values.clock_font = pygame.font.Font(
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
                    globals.Values.clock_enabled = bool(v["clock"])
                except KeyError:
                    print("KeyError: Failed to load service configuration. Reverting to default values.")
                except NameError:
                    print("NameError: Failed to load service configuration. Reverting to default values.")
                except:
                    print("Unknown Error: Failed to load service configuration. Reverting to default values.")
            elif k == "Settings":  # Get application settings
                try:
                    globals.Values.fps = int(v["fps"])
                except KeyError:
                    print("KeyError: Failed to load settings configuration. Reverting to default values.")
                except NameError:
                    print("NameError: Failed to load settings configuration. Reverting to default values.")
                except:
                    print("Unknown Error: Failed to load settings configuration. Reverting to default values.")
