
def degrees(m, n, k):
    if k == 5:
        if 210 > m >= 30:
            return round(64.45 - m, 2)
        else:
            if 0 <= m < 30:
                return round(-4.45 - m, 2)
            else:
                return round(355.55 - m, 2)
    if k == 4:
        if 240 > m >= 60:
            return round(94.45 - m, 2)
        else:
            if 0 <= m < 60:
                return round(25.55 - m, 2)
            else:
                if m >= 240:
                    return round(385.55 - m, 2)
    if k == 3:
        if 270 > m >= 90:
            return round(124.45 - m, 2)
        else:
            if 0 <= m < 90:
                return round(55.55 - m, 2)
            else:
                if m >= 270:
                    return round(415.55 - m, 2)
    if k == 2:
        if 300 > m >= 120:
            return round(154.45 - m, 2)
        else:
            if 0 <= m < 120:
                return round(85.55 - m, 2)
            else:
                if m >= 300:
                    return round(445.55 - m, 2)
    if k == 1:
        if 330 > m >= 150:
            return round(184.45 - m, 2)
        else:
            if 0 <= m < 150:
                return round(115.55 - m, 2)
            else:
                if m >= 330:
                    return round(475.55 - m, 2)
    if k == 6:
        if 270 > m >= 90:
            return round(235.55 - m, 2)
        else:
            if 0 <= m < 90:
                return round(-55.55 - m, 2)
            else:
                if m >= 270:
                    return round(304.45 - m, 2)
    if k == 7:
        if 243.4349 > m >= 63.4349:
            return round(218.6849 - m, 2)
        else:
            if 0 <= m < 63.4349:
                return round(-91.8151 - m, 2)
            else:
                if m >= 243.4349:
                    return round(268.1849 - m, 2)
    if k == 8:
        if 296.5651 > m >= 116.5651:
            return round(271.8151 - m, 2)
        else:
            if 0 <= m < 116.5651:
                return round(-38.6849 - m, 2)
            else:
                if m >= 296.5651:
                    return round(321.3151 - m, 2)


print(degrees(21.1, 0, 8))