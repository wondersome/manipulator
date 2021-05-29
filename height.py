def height(n_big, n_small):
    if n_small == 0:
        return round(((15 - 4*(n_big - 1) - 2)*360)/3.3/3.1415, 2)
    elif n_small > 0:
        return round(((15 - n_big*4 - 1.5 - 3*(n_small - 1)) * 360) / 3.3/3.1415, 2)
