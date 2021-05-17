"""
This program generates "Warhol effect" from original image
"""

import random
from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    for y in range(N_COLS):
        for x in range(N_ROWS):
            patch = make_recolored_patch(random.uniform(0.0, 1.5), 
                    random.uniform(0.0, 1.5), random.uniform(0.0, 1.5))
            put_patch(final_image, y * PATCH_SIZE, x * PATCH_SIZE, patch)

    final_image.show()

def put_patch(final_image, start_x, start_y, patch):
    for y in range(patch.height):
        for x in range(patch.width):
            final_image.set_pixel(start_x + x, start_y + y, patch.get_pixel(x, y))
    return final_image

def make_recolored_patch(red_scale, green_scale, blue_scale):
    patch = SimpleImage(PATCH_NAME)
    for y in range(patch.height):
        for x in range(patch.width):
            pixel.red = pixel.red * red_scale
            pixel.green = pixel.green * green_scale
            pixel.blue = pixel.blue * blue_scale
        return patch

if __name__ == '__main__':
    main()
