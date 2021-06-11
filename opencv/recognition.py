from PIL import Image
import webcolors

im = Image.open('blocks.jpg')  # Can be many different formats.
pix = im.load()
x = 670
y = 300
print(im.size)  # Get the width and hight of the image for iterating over
print(pix[x, y])  # Get the RGBA Value of the a pixel of an image


def get_colour_name(rgb_triplet):
    min_colours = {}
    for key, name in webcolors.css21_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgb_triplet[0]) ** 2
        gd = (g_c - rgb_triplet[1]) ** 2
        bd = (b_c - rgb_triplet[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


print(get_colour_name(pix[x, y]))
