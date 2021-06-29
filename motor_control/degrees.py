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
            return round(123.9734 - m,4),round( -n - 71.2861,4),round( -f + 37.3127,4)
        else:
            if 0 <= m < 90:
                return round(56.0266 - m,4),round( -n + 71.2861,4),round( -f - 37.3127,4)
            else:
                return round(416.0266 - m,4),round( -n + 71.2861,4),round( -f - 37.3127,4)


    if k == 2:
        if 300 >= m >= 120:
            return round(153.9734 - m,4),round( -n - 71.2861,4),round( -f + 37.3127,4)
        else:
            if 0 <= m <= 120:
                return round(86.0266 - m,4),round( -n + 71.2861,4),round( -f - 37.3127,4)
            else:
                return round(446.0266 - m,4),round( -n + 71.2861,4),round( -f - 37.3127,4)


    if k == 1:
        if 330 > m >= 150:
            return round(183.9734 - m,4),round( -n - 71.2861,4),round( -f + 37.3127,4)
        else:
            if 0 <= m < 150:
                return round(116.0266 - m,4),round( -n + 71.2861,4),round( -f - 37.3127,4)
            else:
                return round(476.0266 - m,4),round( -n + 71.2861,4),round( -f - 37.3127,4)


    if k == 6:
        if 270 > m >= 90:
            return round(236.0266 - m,4),round( -n + 71.2861,4),round( -f - 37.3127,4)
        else:
            if 0 <= m < 90:
                return round(-56.0266 - m,4),round( -n - 71.2861,4),round( -f + 37.3127,4)
            else:
                return round(303.9734 - m,4),round( -n - 71.2861,4),round( -f + 37.3127,4)


    if k == 7:
        if 243.4349 > m >= 63.4349:
            return round(220.7077 - m,4),round( -n + 49.3163,4),round( -f - 3.9761,4)
        else:
            if 0 <= m < 63.4349:
                return round(-93.8379 - m,4),round( -n - 49.3163,4),round( -f + 51.1541,4)
            else:
                return round(272.1621 - m,4),round( -n - 49.3163,4),round( -f + 51.1541,4)

    if k == 8:
        if 296.5651 > m >= 116.5651:
            return round(273.8379 - m,4),round( -n + 49.3163,4),round( -f - 51.1541,4)
        else:
            if 0 <= m < 116.5651:
                return round(-40.7077 - m,4),round( -n - 49.3163,4),round( -f + 3.9761,4)
            else:
                return round(325.2923 - m,4),round( -n - 49.3163,4),round( -f + 3.9761,4)

