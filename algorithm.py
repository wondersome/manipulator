from motor_control.degrees import degrees
from motor_control.height import height
import math
from num import abcs
from rec import recognize


def algorithm(col):
    scheme = recognize()[0]

    blocks = recognize()[1]

    made = [[], [], []]
    indexes = []

    global m
    global n
    global f
    global kam


    if col == 0:
        w = 8
    elif col == 1:
        w = 6
    elif col == 2:
        w = 7

    m = 90
    n = 0
    f = 0
    kam = 0


    def output_to_small(value):

        global n, f, m
        global kam
        a=abcs(degrees(m, n, f, value + 1)[0], 1)
        b=abcs(degrees(m, n, f, value + 1)[1], 2)
        c=abcs(degrees(m, n, f, value + 1)[2], 3)

        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m += a - 360
        else:
            m += a
        n += b
        f += c
        kam += math.fabs(a)

    def output_to_big(value):

        global n, f, m
        global kam
        a=abcs(degrees(m, n, f, value + 1)[0], 1)
        b=abcs(degrees(m, n, f, value + 1)[1], 2)
        c=abcs(degrees(m, n, f, value + 1)[2], 3)

        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m += a - 360
        else:
            m += a
        n += b
        f += c
        kam += math.fabs(a)

    def output_from_small(value):

        global n, f, m
        global kam
        h = w
        a=abcs(degrees(m, n, f, h)[0], 1)
        b=abcs(degrees(m, n, f, h)[1], 2)
        c=abcs(degrees(m, n, f, h)[2], 3)
        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m += a - 360
        else:
            m += a
        n += b
        f += c
        kam += math.fabs(a)

    def output_from_big(value):

        global n, f, m
        global kam
        h = w
        a=abcs(degrees(m, n, f, h)[0], 1)
        b=abcs(degrees(m, n, f, h)[1], 2)
        c=abcs(degrees(m, n, f, h)[2], 3)
        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m += a - 360
        else:
            m += a
        n += b
        f += c
        kam += math.fabs(a)


    def same(value, value1):

        global n, f, m
        global kam
        a=abcs(degrees(m, n, f, value1 + 1)[0], 1)
        b=abcs(degrees(m, n, f, value1 + 1)[1], 2)
        c=abcs(degrees(m, n, f, value1 + 1)[2], 3)
        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m += a - 360
        else:
            m += a
        n += b
        f += c
        kam += math.fabs(a)


    for x in blocks[1]:
        if x not in scheme[0] + scheme[1] + scheme[2]:
            if blocks[0][blocks[1].index(x)] in scheme[0] + scheme[1] + scheme[2]:

                blocks[1][blocks[1].index(x)] = ''


    if col == 0:
        a = 0
        b = 1
    elif col == 1:
        a = 1
        b = 2
    elif col == 2:
        a = 2
        b = 3


    for col in range(a, b):


        first, second, third = scheme[col]
        # Если на схеме в ряду только 1 кубик, то ищем среди маленьких кубиков кубик нужного цвета
        if second == '':

            output_to_small(blocks[1].index(first))
            made[col].append(blocks[1][blocks[1].index(first)])
            output_from_small(blocks[1].index(first))

            blocks[1][blocks[1].index(first)] = ''  # удаляем перемещенный элемент

            continue

        big = blocks[0].index(first)
        if blocks[1][big] == '':  # Проверяем есть ли сверху маленький кубик

            output_to_big(big)
            made[col].append(blocks[0][big])
            output_from_big(big)

            blocks[0][big] == ''

        else:
            for i in range(5):
                if i != big:
                    if third == '':
                        if blocks[0][i] != '' and blocks[2][i] == '' and blocks[1][i] != second:
                            tmp = i
                            indexes.append(tmp)
                    else:
                        if blocks[0][i] != '' and blocks[2][i] == '' and blocks[0][i] != second:
                            tmp = i
                            indexes.append(tmp)
            indexes.sort()
            if blocks[1][indexes[0]] == '': # если сверху(только один кубик есть) нет кубика то перемещаем

                output_to_small(big)
                made[col].append(blocks[0][big])
                same(big, indexes[0])

                blocks[1][indexes[0]] = blocks[1][big]
                blocks[1][big] = ''

            else:  # если наверху два кубика, то перемещаем

                output_to_small(big)
                made[col].append(blocks[0][big])
                same(big, indexes[0])

                blocks[2][indexes[0]] = blocks[1][big]
                blocks[1][big] = ''


            output_to_big(big)
            made[col].append(blocks[0][big]) #changed
            output_from_big(big)
            blocks[0][big] = ''

        if third == '':  # Если на схеме нужно построить только 2 ряда
            if second in blocks[1]:  # Если маленький кубик который нам нужен находится во 2 ряду, то перемещаем его

                output_to_small(blocks[1].index(second))
                made[col].append(blocks[1][blocks[1].index(second)])
                output_from_small(blocks[1].index(second))

                blocks[1][blocks[1].index(second)] = ''

            else:  # Иначе кубик находится в 3 ряду, где 2 кубика больших, перемещаем его

                output_to_small(blocks[2].index(second))
                made[col].append(blocks[2][blocks[2].index(second)])
                output_from_small(blocks[2].index(second))

                blocks[2][blocks[2].index(second)] = ''

            continue

        mid = blocks[0].index(second)
        if blocks[1][mid] == '':  # Если сверху никаких кубиков нет, то большой кубик перемещаеам

            output_to_big(mid)
            made[col].append(blocks[0][mid])
            output_from_big(mid)

            blocks[0][mid] = ''

        else:
            for i in range(5):
                if blocks[0][i] != '':
                    if blocks[2][i] == '':
                        if blocks[1][i] != third: # Если мы не используем 2 кубик(маленький) то ставим сверх него еще один кубик
                            tmp = i
                            break

            output_to_small(mid)
            same(mid, tmp)


            if blocks[1][tmp] == '':
                blocks[1][tmp] = blocks[1][mid]
            else:
                blocks[2][tmp] = blocks[1][mid]
            blocks[1][mid] = ''

            made[col].append(blocks[0][mid])
            output_from_big(mid)

            output_to_big(mid)

            blocks[0][mid] = ''

        if third in blocks[1]: # Если один из элементов 3 столбца есть в колоде на 2 ряду, то перемещаеам его в нужный столбец


            output_to_small(blocks[1].index(third))
            made[col].append(blocks[1][blocks[1].index(third)])
            output_from_small(blocks[1].index(third))

            blocks[1][blocks[1].index(third)] = ''

        else:  # Если один из элементов 3 столбца есть в колоде на 3 ряду, то перемещаеам его в нужный столбец

            output_to_small(blocks[2].index(third))
            made[col].append(blocks[2][blocks[2].index(third)])
            output_from_small(blocks[2].index(third))

            blocks[2][blocks[2].index(third)] = ''

    return kam
