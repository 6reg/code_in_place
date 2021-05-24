"""
A visualization of major cities in the world
"""

import os

from PIL.Image import Image

from simpleimage import SimpleImage 

# Dimensions of final image
VISUALIZATION_WIDTH = 1920
VISUALIZATION_HEIGHT = 1080

# Set visualization boundaries
MIN_LONGITUDE = -180
MAX_LONGITUDE = 180
MIN_LATITUDE = -90
MAX_LATITUDE  = 90


def main():
    # create blank canvas to plot cities on
    visualization = SimpleImage.blank(
        VISUALIZATION_WIDTH, VISUALIZATION_HEIGHT
    )
    Image.show(visualization)


main()