def height(n_big, n_small):
    if n_small == 0:
        return round(((19 - 4*n_big - 1)*360)/3.5/3.1415,4)
    elif n_small > 0:
        return round(((19 - n_big*4 - 3 - 3*n_small) * 360) / 3.5/3.1415,4)
