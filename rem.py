from PIL import Image
import cv2
import colorsys
import numpy
from pprint import pprint


def recognize():
    im = Image.open('scheme.jpg')  # Can be many different formats.
    im1 = Image.open('13.jpg')
    im2 = Image.open('35.jpg')
    im3 = Image.open('block.jpg')
    pix = im.load()
    pix1 = im1.load()
    pix2 = im2.load()
    pix3 = im3.load()

    column1 = [[698, 489], [709, 570], [716, 663]]
    column2 = [[782, 482], [792, 563], [798, 655]]
    column3 = [[860, 480], [872, 558], [885, 652]]

    arr = ['R', 'G', 'Y', 'B', 'C']

    first = [[211, 466], [637, 349], [1016, 359]]
    first_first = [[172, 658], [530, 392]]

    second = [[140, 389], [612, 177], [1078, 170]]
    second_second = [[66, 602], [494, 309]]
    block = [[1223, 223]]
    small = [[1241, 355]]
    block2 = [[410, 423]]
    small2 = [[327, 463]]



    scheme = [[], [], []]

    blocks = [
            [],
            [],
            ['', '', '', '', '']]

    # ---comapring colors ----

    # Red Color
    low_red = [150, 80, 45]
    high_red = [255, 255, 155]
    low_red_2 = [0, 80, 45]
    high_red_2 = [15, 255, 155]

    # Blue color
    low_blue = [80, 80, 45]
    high_blue = [125, 255, 255]

    # Green color
    low_green = [45, 80, 45]
    high_green = [80, 255, 155]

    # Yellow color
    low_yellow = [15, 80, 45]
    high_yellow = [45, 255, 180]

    # Black color
    low_black = [0, 0, -10]
    high_black = [180, 255, 50]

    # White color
    low_white = [75, 0, 150]
    high_white= [94, 30, 255]


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
        is_white = ((low_white <= pixel) & (pixel <= high_white)).all()
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
            blocks[0].append("W")

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
        is_white = ((low_white <= pixel) & (pixel <= high_white)).all()
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
            blocks[0].append("W")


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
        is_white = ((low_white <= pixel) & (pixel <= high_white)).all()
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
        is_white = ((low_white <= pixel) & (pixel <= high_white)).all()
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
    k = 0
    
    for i in block:
        h, s, v = pix2[i[0], i[1]]
        h, s, v = colorsys.rgb_to_hsv(h, s, v)
        h = round(h * 180)
        s = round(s * 255)
        pixel = numpy.array([h, s, v])

        is_blue = ((low_blue <= pixel) & (pixel <= high_blue)).all()
        is_black = ((low_black <= pixel) & (pixel <= high_black)).all()
        is_yellow = ((low_yellow <= pixel) & (pixel <= high_yellow)).all()
        is_green = ((low_green <= pixel) & (pixel <= high_green)).all()
        is_white = ((low_white <= pixel) & (pixel <= high_white)).all()
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
            k += 1

    if k == 1:
        for i in small:
            h, s, v = pix2[i[0], i[1]]
            h, s, v = colorsys.rgb_to_hsv(h, s, v)
            h = round(h * 180)
            s = round(s * 255)
            pixel = numpy.array([h, s, v])

            is_blue = ((low_blue <= pixel) & (pixel <= high_blue)).all()
            is_black = ((low_black <= pixel) & (pixel <= high_black)).all()
            is_yellow = ((low_yellow <= pixel) & (pixel <= high_yellow)).all()
            is_green = ((low_green <= pixel) & (pixel <= high_green)).all()
            is_white = ((low_white <= pixel) & (pixel <= high_white)).all()
            is_red = (((low_red <= pixel) & (pixel <= high_red)) | ((low_red_2 <= pixel) & (pixel <= high_red_2))).all()

            
                
            if is_blue == True:
                blocks[0].append("b")
            elif is_black == True:
                blocks[0].append("c")
            elif is_yellow == True:
                blocks[0].append("y")
            elif is_green == True:
                blocks[0].append("g")
            elif is_red == True:
                blocks[0].append("r")
    
    g = 0
    for i in block2:
        h, s, v = pix3[i[0], i[1]]
        h, s, v = colorsys.rgb_to_hsv(h, s, v)
        h = round(h * 180)
        s = round(s * 255)
        pixel = numpy.array([h, s, v])

        is_blue = ((low_blue <= pixel) & (pixel <= high_blue)).all()
        is_black = ((low_black <= pixel) & (pixel <= high_black)).all()
        is_yellow = ((low_yellow <= pixel) & (pixel <= high_yellow)).all()
        is_green = ((low_green <= pixel) & (pixel <= high_green)).all()
        is_white = ((low_white <= pixel) & (pixel <= high_white)).all()
        is_red = (((low_red <= pixel) & (pixel <= high_red)) | ((low_red_2 <= pixel) & (pixel <= high_red_2))).all()

        
            
        if is_blue == True:
            blocks[0].insert(0,"B")
            
        elif is_black == True:
            blocks[0].insert(0,"C")
        elif is_yellow == True:
            blocks[0].insert(0,"Y")
        elif is_green == True:
            blocks[0].insert(0,"G")
        elif is_red == True:
            blocks[0].insert(0,"R")
        else:
            g += 1
        

        if g == 1:
            for i in small:
                h, s, v = pix2[i[0], i[1]]
                h, s, v = colorsys.rgb_to_hsv(h, s, v)
                h = round(h * 180)
                s = round(s * 255)
                pixel = numpy.array([h, s, v])

                is_blue = ((low_blue <= pixel) & (pixel <= high_blue)).all()
                is_black = ((low_black <= pixel) & (pixel <= high_black)).all()
                is_yellow = ((low_yellow <= pixel) & (pixel <= high_yellow)).all()
                is_green = ((low_green <= pixel) & (pixel <= high_green)).all()
                is_white = ((low_white <= pixel) & (pixel <= high_white)).all()
                is_red = (((low_red <= pixel) & (pixel <= high_red)) | ((low_red_2 <= pixel) & (pixel <= high_red_2))).all()

                
                    
                if is_blue == True:
                    blocks[0].insert(0, "b")
                elif is_black == True:
                    blocks[0].insert(0,"c")
                elif is_yellow == True:
                    blocks[0].insert(0,"y")
                elif is_green == True:
                    blocks[0].insert(0,"g")
                elif is_red == True:
                    blocks[0].insert(0,"r")


    

    blocks[1].append('')
    

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
    

