from PIL import Image
import cv2
import colorsys
import numpy
from pprint import pprint


def recognize():
    im = Image.open('scheme.jpg')  # Can be many different formats.
    im1 = Image.open('13.jpg')
    im2 = Image.open('35.jpg')
    pix = im.load()
    pix1 = im1.load()
    pix2 = im2.load()

    column1 = [[709, 484], [715, 569], [717, 661]]
    column2 = [[789, 478], [795, 566], [801, 652]]
    column3 = [[868, 477], [877, 558], [886, 655]]



    first = [[325, 469], [671, 306], [1010, 362]]
    first_first = [[649, 347],[1024, 364]]

    second = [[224, 439], [646, 253], [1071, 265]]
    second_second = [[633, 254],[1018, 261]]



    scheme = [[], [], []]

    blocks = [
            [],
            [],
            ['', '', '', '', '']]

    # ---comapring colors ----

    # Red Color
    low_red = [150, 50, 45]
    high_red = [255, 183, 255]
    low_red_2 = [0, 80, 45]
    high_red_2 = [15, 255, 255]

    # Blue color
    low_blue = [80, 50, 30]
    high_blue = [125, 255, 255]

    # Green color
    low_green = [45, 100, 30]
    high_green = [80, 255, 255]

    # Yellow color
    low_yellow = [15, 80, 45]
    high_yellow = [45, 255, 255]

    # Black color
    low_black = [0, 0, -10]
    high_black = [180, 100, 50]

    # White color
    low_white = [75, 100, 150]
    high_white= [94, 255, 255]

    for i in column1:
        h, s, v = pix[i[0], i[1]]
        h, s, v = colorsys.rgb_to_hsv(h, s, v)
        h = round(h * 180)
        s = round(s * 255)
        pixel = numpy.array([h, s, v])

        is_blue = ((low_blue <= pixel) & (pixel <= high_blue)).all()
        is_black = ((low_black <= pixel) & (pixel <= high_black)).all()
        is_yellow = ((low_yellow <= pixel) & (pixel <= high_yellow)).all()
        is_green = ((low_green <= pixel) & (pixel <= high_green)).all()
        is_red = (((low_red <= pixel) & (pixel <= high_red)) | ((low_red_2 <= pixel) & (pixel <= high_red_2))).all()

        if is_blue == True:
            scheme[0].append("B")
        elif is_black == True:
            scheme[0].append("C")
        elif is_yellow == True:
            scheme[0].append("Y")
        elif is_green == True:
            scheme[0].append("G")
        elif is_red == True:
            scheme[0].append("R")


    for i in column2:
        h, s, v = pix[i[0], i[1]]
        h, s, v = colorsys.rgb_to_hsv(h, s, v)
        h = round(h * 180)
        s = round(s * 255)
        pixel = numpy.array([h, s, v])

        is_blue = ((low_blue <= pixel) & (pixel <= high_blue)).all()
        is_black = ((low_black <= pixel) & (pixel <= high_black)).all()
        is_yellow = ((low_yellow <= pixel) & (pixel <= high_yellow)).all()
        is_green = ((low_green <= pixel) & (pixel <= high_green)).all()
        is_red = (((low_red <= pixel) & (pixel <= high_red)) | ((low_red_2 <= pixel) & (pixel <= high_red_2))).all()
        if is_blue == True:
            scheme[1].append("B")
        elif is_black == True:
            scheme[1].append("C")
        elif is_yellow == True:
            scheme[1].append("Y")
        elif is_green == True:
            scheme[1].append("G")
        elif is_red == True:
            scheme[1].append("R")

    for i in column3:
        h, s, v = pix[i[0], i[1]]
        h, s, v = colorsys.rgb_to_hsv(h, s, v)
        h = round(h * 180)
        s = round(s * 255)
        pixel = numpy.array([h, s, v])

        is_blue = ((low_blue <= pixel) & (pixel <= high_blue)).all()
        is_black = ((low_black <= pixel) & (pixel <= high_black)).all()
        is_yellow = ((low_yellow <= pixel) & (pixel <= high_yellow)).all()
        is_green = ((low_green <= pixel) & (pixel <= high_green)).all()
        is_red = (((low_red <= pixel) & (pixel <= high_red)) | ((low_red_2 <= pixel) & (pixel <= high_red_2))).all()
        if is_blue == True:
            scheme[2].append("B")
        elif is_black == True:
            scheme[2].append("C")
        elif is_yellow == True:
            scheme[2].append("Y")
        elif is_green == True:
            scheme[2].append("G")
        elif is_red == True:
            scheme[2].append("R")

    a = len(scheme[0])
    b = len(scheme[1])
    c = len(scheme[2])
    scheme[0][a-1] = scheme[0][a-1].lower()
    scheme[1][b-1] = scheme[1][b-1].lower()
    scheme[2][c-1] = scheme[2][c-1].lower()




    #------ blocks --------


    for i in first:
        h, s, v = pix1[i[0], i[1]]
        h, s, v = colorsys.rgb_to_hsv(h, s, v)
        h = round(h * 180)
        s = round(s * 255)
        pixel = numpy.array([h, s, v])

        is_blue = ((low_blue <= pixel) & (pixel <= high_blue)).all()
        is_black = ((low_black <= pixel) & (pixel <= high_black)).all()
        is_yellow = ((low_yellow <= pixel) & (pixel <= high_yellow)).all()
        is_green = ((low_green <= pixel) & (pixel <= high_green)).all()
        is_red = (((low_red <= pixel) & (pixel <= high_red)) | ((low_red_2 <= pixel) & (pixel <= high_red_2))).all()
        is_white = ((low_white <= pixel) & (pixel <= high_white)).all()
        if is_blue == True:
            blocks[0].append("B")
        elif is_green == True:
            blocks[0].append("G")
        elif is_black == True:
            blocks[0].append("C")
        elif is_yellow == True:
            blocks[0].append("Y")
        elif is_red == True:
            blocks[0].append("R")
        else:
            blocks[0].append('W')

    for i in first_first:
        h, s, v = pix2[i[0], i[1]]
        h, s, v = colorsys.rgb_to_hsv(h, s, v)
        h = round(h * 180)
        s = round(s * 255)
        pixel = numpy.array([h, s, v])

        is_blue = ((low_blue <= pixel) & (pixel <= high_blue)).all()
        is_black = ((low_black <= pixel) & (pixel <= high_black)).all()
        is_yellow = ((low_yellow <= pixel) & (pixel <= high_yellow)).all()
        is_green = ((low_green <= pixel) & (pixel <= high_green)).all()
        is_red = (((low_red <= pixel) & (pixel <= high_red)) | ((low_red_2 <= pixel) & (pixel <= high_red_2))).all()

        if is_blue == True:
            blocks[0].append("B")
        elif is_black == True:
            blocks[0].append("C")
        elif is_yellow == True:
            blocks[0].append("Y")
        elif is_green == True:
            blocks[0].append("G")
        elif is_red == True:
            blocks[0].append("R")
        else:
            blocks[0].append('W')


    for i in second:
        h, s, v = pix1[i[0], i[1]]
        h, s, v = colorsys.rgb_to_hsv(h, s, v)
        h = round(h * 180)
        s = round(s * 255)
        pixel = numpy.array([h, s, v])

        is_blue = ((low_blue <= pixel) & (pixel <= high_blue)).all()
        is_black = ((low_black <= pixel) & (pixel <= high_black)).all()
        is_yellow = ((low_yellow <= pixel) & (pixel <= high_yellow)).all()
        is_green = ((low_green <= pixel) & (pixel <= high_green)).all()
        is_red = (((low_red <= pixel) & (pixel <= high_red)) | ((low_red_2 <= pixel) & (pixel <= high_red_2))).all()

        if is_blue == True:
            blocks[1].append("b")
        elif is_black == True:
            blocks[1].append("c")
        elif is_yellow == True:
            blocks[1].append("y")
        elif is_green == True:
            blocks[1].append("g")
        elif is_red == True:
            blocks[1].append("r")
        else:
            blocks[1].append("w")

    for i in second_second:
        h, s, v = pix2[i[0], i[1]]
        h, s, v = colorsys.rgb_to_hsv(h, s, v)
        h = round(h * 180)
        s = round(s * 255)
        pixel = numpy.array([h, s, v])

        is_blue = ((low_blue <= pixel) & (pixel <= high_blue)).all()
        is_black = ((low_black <= pixel) & (pixel <= high_black)).all()
        is_yellow = ((low_yellow <= pixel) & (pixel <= high_yellow)).all()
        is_green = ((low_green <= pixel) & (pixel <= high_green)).all()
        is_red = (((low_red <= pixel) & (pixel <= high_red)) | ((low_red_2 <= pixel) & (pixel <= high_red_2))).all()


        if is_blue == True:
            blocks[1].append("b")
        elif is_black == True:
            blocks[1].append("c")
        elif is_yellow == True:
            blocks[1].append("y")
        elif is_green == True:
            blocks[1].append("g")
        elif is_red == True:
            blocks[1].append("r")
        else:
            blocks[1].append("w")



    a = len(scheme[0])
    b = len(scheme[1])
    c = len(scheme[2])
    if a == 2:
        scheme[0].append('')
    elif a == 1:
        scheme[0].append('')
        scheme[0].append('')

    if b == 2:
        scheme[1].append('')
    elif b == 1:
        scheme[1].append('')
        scheme[1].append('')

    if c == 2:
        scheme[2].append('')
    elif c == 1:
        scheme[2].append('')
        scheme[2].append('')


    return scheme, blocks
    pprint(scheme)
    pprint(blocks)
