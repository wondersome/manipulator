# a = m; b = n; c = f
def degrees(m, n, f, k):
    if k == 5:
        if 210 > m >= 30:
            return round(65.2 - m, 1), round(-n-73.8,1), round(-f+38.6,1)

        else:
            if 0 <= m < 30:
                return round(-5.2 - m, 1), round(-n + 73.8, 1), round(-f - 38.6, 1)
            else:
                return round(354.8 - m, 1), round(-n + 73.8, 1), round(-f - 38.6, 1)


    if k == 4:
        if 240 > m >= 60:
            return round(95.2 - m, 1), round(-n - 73.8, 1), round(-f + 38.6, 1)
        else:
            if 0 <= m < 60:
                return round(24.8 - m, 1), round(-n + 73.8, 1), round(-f - 38.6, 1)
            else:
                return round(384.8 - m, 1), round(-n + 73.8, 1), round(-f - 38.6, 1)


    if k == 3:
        if 270 > m >= 90:
            return round(125.2 - m, 1), round(-n - 73.8, 1), round(-f + 38.6, 1)
        else:
            if 0 <= m < 90:
                return round(54.8 - m, 1), round(-n + 73.8, 1), round(-f - 38.6, 1)
            else:
                return round(414.8 - m, 1), round(-n + 73.8, 1), round(-f - 38.6, 1)


    if k == 2:
        if 300 >= m >= 120:
            return round(155.2 - m, 1), round(-n - 73.8, 1), round(-f + 38.6, 1)
        else:
            if 0 <= m <= 120:
                return round(84.8 - m, 1), round(-n + 73.8, 1), round(-f - 38.6, 1)
            else:
                return round(444.8 - m, 1), round(-n + 73.8, 1), round(-f - 38.6, 1)


    if k == 1:
        if 330 > m >= 150:
            return round(185.2 - m, 1), round(-n - 73.8, 1), round(-f + 38.6, 1)
        else:
            if 0 <= m < 90:
                return round(84.8 - m, 1), round(-n + 73.8, 1), round(-f - 38.6, 1)
            else:
                return round(444.8 - m, 1), round(-n + 73.8, 1), round(-f - 38.6, 1)


    if k == 6:
        if 270 > m >= 90:
            return round(234.8 - m, 1), round(-n + 73.8, 1), round(-f - 38.6, 1)
        else:
            if 0 <= m < 90:
                return round(-54.8 - m, 1), round(-n - 73.8, 1), round(-f + 38.6, 1)
            else:
                return round(305.2 - m, 1), round(-n - 73.8, 1), round(-f + 38.6, 1)


    if k == 7:
        if 243.4349 > m >= 63.4349:
            return round(217.9349 - m, 2), round(-n + 53.2, 1), round(-f - 1.1349, 1)
        else:
            if 0 <= m < 63.4349:
                return round(-91.0651 - m, 2), round(-n - 53.2, 1), round(-f - 53.2, 1)
            else:
                return round(268.9349 - m, 2), round(-n - 53.2, 1), round(-f - 53.2, 1)

    if k == 8:
        if 296.5651 > m >= 116.5651:
            return round(271.0651 - m, 2), round(-n + 53.2, 1), round(-f - 54.2651, 1)
        else:
            if 0 <= m < 116.5651:
                return round(-37.9349 - m, 2), round(-n - 53.2, 1), round(-f + 1.1349, 1)
            else:
                return round(322.0651 - m, 2), round(-n - 53.2, 1), round(-f + 1.1349, 1)


