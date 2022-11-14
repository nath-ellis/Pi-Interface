"""
For parsing the config.yaml file
"""

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
                globals.Values.primary_colour = eval(v["primary"])
                globals.Values.secondary_colour = eval(v["secondary"])
                globals.Values.background_colour = eval(v["background"])
            elif k == "Services":  # Get service settings
                pass
            elif k == "Settings":  # Get application settings
                globals.Values.fps = int(v["fps"])
