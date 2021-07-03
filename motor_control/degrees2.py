# a = m; b = n; c = f
def degrees(m, n, f, k):
    if k == 5:
        if 210 > m >= 30:
            return round( 63.9734 - m,4),round( -n-71.2861,4),round( -f+37.3127,4)

        else:
            if 0 <= m < 30:
                return round(-3.9734 - m,4),round(-n + 71.2861,4),round( -f - 37.3127,4)
            else:
                return round(356.0266 - m,4),round( -n + 71.2861,4),round( -f - 37.3127,4)


    if k == 4:
        if 240 > m >= 60:
            return round(93.9734 - m,4),round( -n - 71.2861,4),round( -f + 37.3127,4)
        else:
            if 0 <= m < 60:
                return round(26.0266 - m,4),round( -n + 71.2861,4),round( -f - 37.3127,4)
            else:
                return round(386.0266 - m,4),round( -n + 71.2861,4),round( -f - 37.3127,4)

    if k == 3:
        if 270 > m >= 90:
            return round(127.5555 - m,4),round( -n - 78.9458,4),round( -f + 41.3903,4)
        else:
            if 0 <= m < 90:
                return round(52.4445 - m,4),round( -n + 78.9458,4),round( -f - 41.3903,4)
            else:
                return round(412.4445 - m,4),round( -n + 78.9458,4),round( -f - 41.3903,4)


    if k == 2:
        if 300 >= m >= 120:
            return round(157.5555 - m,4),round( -n - 78.9458,4),round( -f + 41.3903,4)
        else:
            if 0 <= m <= 120:
                return round(82.4445 - m,4),round( -n + 78.9458,4),round( -f - 41.3903,4)
            else:
                return round(442.4445 - m,4),round( -n + 78.9458,4),round( -f - 41.3903,4)


    if k == 1:
        if 330 > m >= 150:
            return round(187.5555 - m,4),round( -n - 78.9458,4),round( -f + 41.3903,4)
        else:
            if 0 <= m < 150:
                return round(112.4445 - m,4),round( -n + 78.9458,4),round( -f - 41.3903,4)
            else:
                return round(472.4445 - m,4),round( -n + 78.9458,4),round( -f - 41.3903,4)


    if k == 6:
        if 270 > m >= 90:
            return round(234.5266 - m,4),round( -n + 78.9458,4),round( -f - 41.3903,4)
        else:
            if 0 <= m < 90:
                return round(-54.5266 - m,4),round( -n - 78.9458,4),round( -f + 41.3903,4)
            else:
                return round(295.4734 - m,4),round( -n - 78.9458,4),round( -f + 41.3903,4)

    if k == 7:
        if 243.4349 > m >= 63.4349:
            return round(223.2077 - m,4),round( -n + 49.3163,4),round( -f - 3.9761,4)
        else:
            if 0 <= m < 63.4349:
                return round(-92.3379 - m,4),round( -n - 49.3163,4),round( -f + 51.1541,4)
            else:
                return round(273.6621 - m,4),round( -n - 49.3163,4),round( -f + 51.1541,4)

    if k == 8:
        if 296.5651 > m >= 116.5651:
            return round(276.3379 - m,4),round( -n + 49.3163,4),round( -f - 51.1541,4)
        else:
            if 0 <= m < 116.5651:
                return round(-43.2077 - m,4),round( -n - 49.3163,4),round( -f + 3.9761,4)
            else:
                return round(322.7923 - m,4),round( -n - 49.3163,4),round( -f + 3.9761,4)
