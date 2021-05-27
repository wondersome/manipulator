from degrees import degrees
from pprint import pprint
from height import height

global m
global n
global f
m = 90
n = 0
f = 0

def addition(value):
    if m + degrees(m, n, f, value)[0] < 0:
        m += degrees(m, n, f, value)[0] + 360
    elif m + degrees(m, n, f, value)[0] > 360:
        m += degrees(m, n, f, value)[0] - 360
    else:
        m += degrees(m, n, f, value)[0]
    n += degrees(m, n, f, blocks[1].index(x) + 1)[1]
    f += degrees(m, n, f, blocks[1].index(x) + 1)[2]

def qnum(value):
    q = 0
    w = 0
    for i in made[value]:
        if i.isupper():
            q += 1
        elif i.islower():
            w += 1
    return height(q, w)

def cnum(value):
    q = 0
    w = 0
    if blocks[0][value].isupper():
        q += 1
    elif blocks[0][value].islower():
        w += 1

    if blocks[1][value].isupper():
        q += 1
    elif blocks[1][value].islower():
        w += 1

    if blocks[2][value].isupper():
        q += 1
    elif blocks[2][value].islower():
        w += 1
    return height(q, w)




scheme = [['G', 'y', ''],
          ['R', 'C', 'r'],
          ['b', '', '']]

blocks = [['Y', 'R', 'B', 'G', 'C'],
          ['b', 'c', 'g', 'r', 'y'],
          ['', '', '', '', '']]
algo = []
made = [[], [], []]





# вычисляем какой кубик следует выкинуть
for x in blocks[1]:
    if x not in scheme[0] + scheme[1] + scheme[2]:
        algo.append(f'{blocks[1].index(x) + 1} throw from blocks')
        print(f'выкидываем кубик {blocks[1].index(x) + 1} поворачиваясь на градус",'
              f' {degrees(m, n, f, blocks[1].index(x) + 1)[0]}, '
              f'{degrees(m, n, f, blocks[1].index(x) + 1)[1]}, '
              f'{degrees(m, n, f, blocks[1].index(x) + 1)[2]}, {height(1, 1)}')
        if m + degrees(m, n, f, blocks[1].index(x) + 1)[0] < 0:
            m += degrees(m, n, f, blocks[1].index(x) + 1)[0]+360
        elif m + degrees(m, n, f, blocks[1].index(x) + 1)[0] > 360:
            m += degrees(m, n, f, blocks[1].index(x) + 1)[0]-360
        else:
            m += degrees(m, n, f, blocks[1].index(x) + 1)[0]
        n += degrees(m, n, f, blocks[1].index(x) + 1)[1]
        f += degrees(m, n, f, blocks[1].index(x) + 1)[2]
        blocks[1][blocks[1].index(x)] = ''


for col in range(3):
    first, second, third = scheme[col]
    # Если на схеме в ряду только 1 кубик, то ищем среди маленьких кубиков кубик нужного цвета
    if second == '':
        algo.append(f'{blocks[1].index(first) + 1} small from blocks to column # {col + 1}')
        if col+1 == 1:
            h = 8
        elif col+1 == 2:
            h = 6
        elif col+1 == 3:
            h = 7
        print(f'Чтобы доехать до {blocks[1].index(first) + 1} башни (маленький кубик) поворачивааемся на '
              f'{degrees(m, n, f, blocks[1].index(first) + 1)[0]}, '
              f'{degrees(m, n, f, blocks[1].index(first) + 1)[1]}, '
              f'{degrees(m, n, f, blocks[1].index(first) + 1)[2]}, '
              f'{cnum(blocks[1].index(first))}')


        if m + degrees(m, n, f, blocks[1].index(first) + 1)[0] < 0:
            m += degrees(m, n, f, blocks[1].index(first) + 1)[0] + 360
        elif m + degrees(m, n, f, blocks[1].index(first) + 1)[0] > 360:
            m += degrees(m, n, f, blocks[1].index(first) + 1)[0] - 360
        else:
            m += degrees(m, n, f, blocks[1].index(first) + 1)[0]
        n += degrees(m, n, f, blocks[1].index(first) + 1)[1]
        f += degrees(m, n, f, blocks[1].index(first) + 1)[2]
        made[col].append(blocks[1][blocks[1].index(first)])

        print(f'Чтобы доехать от {blocks[1].index(first) + 1} башни (маленький кубик) до столбца # {col + 1} '
              f'поварачиваемся на {degrees(m, n, f, h)[0]}, {degrees(m, n, f, h)[1]}, {degrees(m, n, f, h)[2]}, {qnum(col)}')

        if m + degrees(m, n, f, h)[0] < 0:
            m += degrees(m, n, f, h)[0] + 360
        elif m + degrees(m, n, f, h)[0] > 360:
            m += degrees(m, n, f, h)[0] - 360
        else:
            m += degrees(m, n, f, h)[0]
        n += degrees(m, n, f, h)[1]
        f += degrees(m, n, f, h)[2]
        blocks[1][blocks[1].index(first)] = ''  # удаляем перемещенный элемент
        continue

    big = blocks[0].index(first)
    if blocks[1][big] == '':  # Проверяем есть ли сверху маленький кубик
        cnum(big)
        algo.append(f'{big + 1} big from blocks to column # {col + 1}')  # Перемещаем если сверху нет маленького кубика
        if col+1 == 1:
            h = 8
        elif col+1 == 2:
            h = 6
        elif col+1 == 3:
            h = 7
            #от {col+1} столбца
        print(f'Чтобы доехать до {big + 1} башни (большой кубик) поворачиваемся на '
              f'{degrees(m, n, f, big + 1)[0]}, '
              f'{degrees(m, n, f, big + 1)[1]}, '
              f'{degrees(m, n, f, big + 1)[2]}, '
              f'{cnum(big)}')

        if m + degrees(m, n, f, big + 1)[0] < 0:
            m += degrees(m, n, f, big + 1)[0] + 360
        elif m + degrees(m, n, f, big + 1)[0] > 360:
            m += degrees(m, n, f, big + 1)[0] - 360
        else:
            m += degrees(m, n, f, big + 1)[0]
        n += degrees(m, n, f, big + 1)[1]
        f += degrees(m, n, f, big + 1)[2]

        made[col].append(blocks[0][big])

        print(f'Чтобы доехать от {big + 1} большого кубика до столбца # {col + 1} поворачиваемся на '
              f'{degrees(m, n, f, h)[0]}, '
              f'{degrees(m, n, f, h)[1]}, '
              f'{degrees(m, n, f, h)[2]}, '
              f'{qnum(col)}')



        if m + degrees(m, n, f, h)[0] < 0:
            m += degrees(m, n, f, h)[0]+360
        elif m + degrees(m, n, f, h)[0] > 360:
            m += degrees(m, n, f, h)[0]-360
        else:
            m += degrees(m, n, f, h)[0]
        n += degrees(m, n, f, h)[1]
        f += degrees(m, n, f, h)[2]

        blocks[0][big] == ''


    else:
        for i in range(5):
            if i != big:
                if third == '':
                    if blocks[0][i] != '' and blocks[2][i] == '' and blocks[1][i] != second:
                        tmp = i
                else:
                    if blocks[0][i] != '' and blocks[2][i] == '' and blocks[0][i] != second:
                        tmp = i
        if blocks[1][tmp] == '': # если сверху(только один кубик есть) нет кубика то перемещаем
            cnum(big)
            algo.append(f'{big + 1} small from blocks to blocks # {tmp + 1}')
            blocks[1][tmp] = blocks[1][big]
            blocks[1][big] = ''
            cnum(tmp)

        else:  # если наверху два кубика, то перемещаем
            algo.append(f'{big + 1} small from blocks to blocks # {tmp + 1}')
            print(
                f'Чтобы доехать до {big + 1} башни (маленький кубик) поворачиваемся на {degrees(m, n, f, big + 1)[0]},'
                f'{degrees(m, n, f, big + 1)[1]}, {degrees(m, n, f, big + 1)[2]}, {cnum(big)}')

            if m + degrees(m, n, f, big + 1)[0] < 0:
                m += degrees(m, n, f, big + 1)[0] + 360
            elif m + degrees(m, n, f, big + 1)[0] > 360:
                m += degrees(m, n, f, big + 1)[0] - 360
            else:
                m += degrees(m, n, f, big + 1)[0]
            n += degrees(m, n, f, big + 1)[1]
            f += degrees(m, n, f, big + 1)[2]

            made[col].append(blocks[0][big])

            print(f'Чтобы доехать от {big + 1} башни (маленький кубик) до башни # {tmp + 1} поворачиваемся на '
                  f'{degrees(m, n, f, tmp + 1)[0]}, {degrees(m, n, f, tmp + 1)[1]}, {degrees(m, n, f, tmp + 1)[2]}, {cnum(tmp)}')

            if m + degrees(m, n, f, tmp + 1)[0] < 0:
                m += degrees(m, n, f, tmp + 1)[0] + 360
            elif m + degrees(m, n, f, tmp + 1)[0] > 360:
                m += degrees(m, n, f, tmp + 1)[0] - 360
            else:
                m += degrees(m, n, f, tmp + 1)[0]
            n += degrees(m, n, f, tmp + 1)[1]
            f += degrees(m, n, f, tmp + 1)[2]

            blocks[2][tmp] = blocks[1][big]
            blocks[1][big] = ''

        algo.append(f'{big + 1} big from blocks to column # {col + 1}')# после того как расчистили все сверху, всегда 1 большой кубик
        print(f'Чтобы доехать до {big + 1} башни (маленький кубик) поворачиваемся на '
              f'{degrees(m, n, f, big + 1)[0]}, {degrees(m, n, f, big + 1)[1]}, {degrees(m, n, f, big + 1)[2]}, {cnum(big)}')

        if m + degrees(m, n, f, big + 1)[0] < 0:
            m += degrees(m, n, f, big + 1)[0] + 360
        elif m + degrees(m, n, f, big + 1)[0] > 360:
            m += degrees(m, n, f, big + 1)[0] - 360
        else:
            m += degrees(m, n, f, big + 1)[0]
        n += degrees(m, n, f, big + 1)[1]
        f += degrees(m, n, f, big + 1)[2]

        print(f'Чтобы доехать от {big + 1} башни (маленький кубик) до столбца # {tmp + 1} поворачиваемся на '
              f'{degrees(m, n, f, tmp + 1)[0]}, {degrees(m, n, f, tmp + 1)[1]}, {degrees(m, n, f, tmp + 1)[2]}, {cnum(tmp)}')

        if m + degrees(m, n, f, tmp + 1)[0] < 0:
            m += degrees(m, n, f, tmp + 1)[0] + 360
        elif m + degrees(m, n, f, tmp + 1)[0] > 360:
            m += degrees(m, n, f, tmp + 1)[0] - 360
        else:
            m += degrees(m, n, f, tmp + 1)[0]
        n += degrees(m, n, f, tmp + 1)[1]
        f += degrees(m, n, f, tmp + 1)[2]

        blocks[0][big] = ''
        qnum(col)

    if third == '':  # Если на схеме нужно построить только 2 ряда
        if second in blocks[1]:  # Если маленький кубик который нам нужен находится во 2 ряду, то перемещаем его
            algo.append(f'{blocks[1].index(second) + 1} small from blocks to column # {col + 1}')
            if col + 1 == 1:
                h = 8
            elif col + 1 == 2:
                h = 6
            elif col + 1 == 3:
                h = 7
            print(f'Чтобы доехать до {blocks[1].index(second) + 1} башни (маленький кубик) поворачиваемся на'
                  f' {degrees(m, n, f, blocks[1].index(second) + 1)[0]}, '
                  f'{degrees(m, n, f, blocks[1].index(second) + 1)[1]}, '
                  f'{degrees(m, n, f, blocks[1].index(second) + 1)[2]}, '
                  f'{cnum(blocks[1].index(second))}')

            if m + degrees(m, n, f, blocks[1].index(second) + 1)[0] < 0:
                m += degrees(m, n, f, blocks[1].index(second) + 1)[0] + 360
            elif m + degrees(m, n, f, blocks[1].index(second) + 1)[0] > 360:
                m += degrees(m, n, f, blocks[1].index(second) + 1)[0] - 360
            else:
                m += degrees(m, n, f, blocks[1].index(second) + 1)[0]
            n += degrees(m, n, f, blocks[1].index(second) + 1)[1]
            f += degrees(m, n, f, blocks[1].index(second) + 1)[2]

            made[col].append(blocks[1][blocks[1].index(second)])


            print(f'Чтобы доехать от {blocks[1].index(second) + 1} башни (маленький кубик) до столбца # {col + 1} '
                  f'поворачиваемся на {degrees(m, n, f, h)[0]}, {degrees(m, n, f, h)[1]}, {degrees(m, n, f, h)[2]}, '
                  f'{qnum(col)}')


            if m + degrees(m, n, f, h)[0] < 0:
                m += degrees(m, n, f, h)[0] + 360
            elif m + degrees(m, n, f, h)[0] > 360:
                m += degrees(m, n, f, h)[0]-360
            else:
                m += degrees(m, n, f, h)[0]
            n += degrees(m, n, f, h)[1]
            f += degrees(m, n, f, h)[2]

            blocks[1][blocks[1].index(second)] = ''

        else:  # Иначе кубик находится в 3 ряду, где 2 кубика больших, перемещаем его
            algo.append(f'{blocks[2].index(second) + 1} small from blocks to column # {col + 1}')
            if col + 1 == 1:
                h = 8
            elif col + 1 == 2:
                h = 6
            elif col + 1 == 3:
                h = 7

            print(f'Чтобы доехать до {blocks[2].index(second) + 1} башни (маленький кубик)'
                  f' поворачиваемся на {degrees(m, n, f, blocks[2].index(second) + 1)[0]},'
                  f' {degrees(m, n, f, blocks[2].index(second) + 1)[1]}, '
                  f'{degrees(m, n, f, blocks[2].index(second) + 1)[2]}, '
                  f'{cnum(blocks[2].index(second))}')

            if m + degrees(m, n, f, blocks[2].index(second) + 1)[0] < 0:
                m += degrees(m, n, f, blocks[2].index(second) + 1)[0] + 360
            elif m + degrees(m, n, f, blocks[2].index(second) + 1)[0] > 360:
                m += degrees(m, n, f, blocks[2].index(second) + 1)[0] - 360
            else:
                m += degrees(m, n, f, blocks[2].index(second) + 1)[0]
            n += degrees(m, n, f, blocks[2].index(second) + 1)[1]
            f += degrees(m, n, f, blocks[2].index(second) + 1)[2]

            made[col].append(blocks[2][blocks[2].index(second)])


            print(f'Чтобы доехать от {blocks[2].index(second) + 1} башни (маленький кубик) до столбца # '
                  f'{col + 1} поворачиваемся на {degrees(m, n, f, h)[0]}, {degrees(m, n, f, h)[1]}, '
                  f'{degrees(m, n, f, h)[2]}, {qnum(col)}')


            if m + degrees(m, n, f, h)[0] < 0:
                m += degrees(m, n, f, h)[0]+360
            elif m + degrees(m, n, f, h)[0] > 360:
                m += degrees(m, n, f, h)[0]-360
            else:
                m += degrees(m, n, f, h)[0]
            n += degrees(m, n, f, h)[1]
            f += degrees(m, n, f, h)[2]

            blocks[2][blocks[2].index(second)] = ''
            qnum(col)

        continue

    mid = blocks[0].index(second)
    if blocks[1][mid] == '':  # Если сверху никаких кубиков нет, то большой кубик перемещаеам
        algo.append(f'{mid + 1} big from blocks to column # {col + 1}')

        if col + 1 == 1:
            h = 8
        elif col + 1 == 2:
            h = 6
        elif col + 1 == 3:
            h = 7

        print(f'Чтобы доехать до {mid + 1} башни (большой кубик) поворачиваемся на {degrees(m, n, f, mid + 1)[0]}, '
              f'{degrees(m, n, f, mid + 1)[1]}, {degrees(m, n, f, mid + 1)[2]}, {cnum(mid)}')

        if m + degrees(m, n, f, mid + 1)[0] < 0:
            m += degrees(m, n, f, mid + 1)[0] + 360
        elif m + degrees(m, n, f, mid + 1)[0] > 360:
            m += degrees(m, n, f, mid + 1)[0] - 360
        else:
            m += degrees(m, n, f, mid + 1)[0]
        n += degrees(m, n, f, mid + 1)[1]
        f += degrees(m, n, f, mid + 1)[2]
        made[col].append(blocks[0][mid])

        print(f'Чтобы доехать от {mid + 1} большого кубика до столбца # {col + 1} поворачиваемся на '
              f'{degrees(m, n, f, h)[0]}, {degrees(m, n, f, h)[1]}, {degrees(m, n, f, h)[2]}, {qnum(col)}')


        if m + degrees(m, n, f, h)[0] < 0:
            m += degrees(m, n, f, h)[0] + 360
        elif m + degrees(m, n, f, h)[0] > 360:
            m += degrees(m, n, f, h)[0] - 360
        else:
            m += degrees(m, n, f, h)[0]
        n += degrees(m, n, f, h)[1]
        f += degrees(m, n, f, h)[2]

        blocks[0][mid] = ''
        qnum(col)

    else:
        for i in range(5):
            if blocks[0][i] != '':
                if blocks[2][i] == '':
                    if blocks[1][i] != third: # Если мы не используем 2 кубик(маленький) то ставим сверх него еще один кубик
                        tmp = i
                        break
        algo.append(f'{mid + 1} small from blocks to blocks # {tmp + 1}')

        print(f'Чтобы доехать до {mid + 1} башни (маленький кубик) поворачиваемся на '
              f'{degrees(m, n, f, mid + 1)[0]}, {degrees(m, n, f, mid + 1)[1]}, {degrees(m, n, f, mid + 1)[2]}, {cnum(mid)}')

        if m + degrees(m, n, f, mid + 1)[0] < 0:
            m += degrees(m, n, f, mid + 1)[0] + 360
        elif m + degrees(m, n, f, mid + 1)[0] > 360:
            m += degrees(m, n, f, mid + 1)[0] - 360
        else:
            m += degrees(m, n, f, mid + 1)[0]
        n += degrees(m, n, f, mid + 1)[1]
        f += degrees(m, n, f, mid + 1)[2]

        print(f'Чтобы доехать от {mid + 1} башни (маленький кубик) до башни # {tmp + 1} '
              f'поворачиваемся на {degrees(m, n, f, tmp + 1)[0]}, {degrees(m, n, f, tmp + 1)[1]}, '
              f'{degrees(m, n, f, tmp + 1)[2]}, {cnum(tmp)}')

        if m + degrees(m, n, f, tmp + 1)[0] < 0:
            m += degrees(m, n, f, tmp + 1)[0] + 360
        elif m + degrees(m, n, f, tmp + 1)[0] > 360:
            m += degrees(m, n, f, tmp + 1)[0] - 360
        else:
            m += degrees(m, n, f, tmp + 1)[0]
        n += degrees(m, n, f, tmp + 1)[1]
        f += degrees(m, n, f, tmp + 1)[2]

        if blocks[1][tmp] == '':
            blocks[1][tmp] = blocks[1][mid]
        else:
            blocks[2][tmp] = blocks[1][mid]
        blocks[1][mid] = ''
        algo.append(f'{mid + 1} big from blocks to column # {col + 1}')

        if col + 1 == 1:
            h = 8
        elif col + 1 == 2:
            h = 6
        elif col + 1 == 3:
            h = 7

        print(f'Чтобы доехаать до {mid + 1} башни (большой кубик) поворачиваемся на '
              f'{degrees(m, n, f, mid + 1)[0]}, {degrees(m, n, f, mid + 1)[1]}, '
              f'{degrees(m, n, f, mid + 1)[2]}, {cnum(mid)}')


        if m + degrees(m, n, f, mid + 1)[0] < 0:
            m += degrees(m, n, f, mid + 1)[0] + 360
        elif m + degrees(m, n, f, mid + 1)[0] > 360:
            m += degrees(m, n, f, mid + 1)[0] - 360
        else:
            m += degrees(m, n, f, mid + 1)[0]
        n += degrees(m, n, f, mid + 1)[1]
        f += degrees(m, n, f, mid + 1)[2]

        made[col].append(blocks[0][mid])


        print(f'Чтобы доехать от {mid + 1} башни (большой кубик) до столбца # {col + 1} '
              f'поворачиваемся на {degrees(m, n, f, h)[0]}, {degrees(m, n, f, h)[1]}, {degrees(m, n, f, h)[2]}, {qnum(col)}')


        if m + degrees(m, n, f, h)[0] < 0:
            m += degrees(m, n, f, h)[0] + 360
        elif m + degrees(m, n, f, h)[0] > 360:
            m += degrees(m, n, f, h)[0] - 360
        else:
            m += degrees(m, n, f, h)[0]
        n += degrees(m, n, f, h)[1]
        f += degrees(m, n, f, h)[2]


        blocks[0][mid] = ''
        qnum(col)

    if third in blocks[1]: # Если один из элементов 3 столбца есть в колоде на 2 ряду, то перемещаеам его в нужный столбец

        algo.append(f'{blocks[1].index(third) + 1} small1 from blocks to column # {col + 1}')

        if col + 1 == 1:
            h = 8
        elif col + 1 == 2:
            h = 6
        elif col + 1 == 3:
            h = 7

        print(f'Чтобы доехать до {blocks[1].index(third) + 1} башни (маленький кубик) поворачиваемся на'
              f' {degrees(m, n, f, blocks[1].index(third) + 1)[0]}, {degrees(m, n, f, blocks[1].index(third) + 1)[1]},'
              f' {degrees(m, n, f, blocks[1].index(third) + 1)[2]}, {cnum(blocks[1].index(third))}')

        if m + degrees(m, n, f, blocks[1].index(third) + 1)[0] < 0:
            m += degrees(m, n, f, blocks[1].index(third) + 1)[0] + 360
        elif m + degrees(m, n, f, blocks[1].index(third) + 1)[0] > 360:
            m += degrees(m, n, f, blocks[1].index(third) + 1)[0] - 360
        else:
            m += degrees(m, n, f, blocks[1].index(third) + 1)[0]
        n += degrees(m, n, f, blocks[1].index(third) + 1)[1]
        f += degrees(m, n, f, blocks[1].index(third) + 1)[2]

        made[col].append(blocks[1][blocks[1].index(third)])


        print(f'Чтобы доехать от {blocks[1].index(third) + 1} башни (маленький кубик) до столбца # {col + 1} '
              f'поворачиваемся на {degrees(m, n, f, h)[0]}, {degrees(m, n, f, h)[1]}, '
              f'{degrees(m, n, f, h)[2]}, {qnum(col)}')


        if m + degrees(m, n, f, h)[0] < 0:
            m += degrees(m, n, f, h)[0] + 360
        elif m + degrees(m, n, f, h)[0] > 360:
            m += degrees(m, n, f, h)[0] - 360
        else:
            m += degrees(m, n, f, h)[0]

        n += degrees(m, n, f, h)[1]
        f += degrees(m, n, f, h)[2]
        blocks[1][blocks[1].index(third)] = ''
        qnum(col)

    else:  # Если один из элементов 3 столбца есть в колоде на 3 ряду, то перемещаеам его в нужный столбец
        algo.append(f'{blocks[2].index(third) + 1} small from blocks to column # {col + 1}')

        if col + 1 == 1:
            h = 8
        elif col + 1 == 2:
            h = 6
        elif col + 1 == 3:
            h = 7

        print(f'Чтобы доехать до {blocks[2].index(third) + 1} башни (маленький кубик) поворачиваемся на '
              f' {degrees(m, n, f, blocks[2].index(third) + 1)[0]}, {degrees(m, n, f, blocks[2].index(third) + 1)[1]}, '
              f'{degrees(m, n, f, blocks[2].index(third) + 1)[2]}, {cnum(blocks[2].index(third))}')

        if m + degrees(m, n, f, blocks[2].index(third) + 1)[0] < 0:
            m += degrees(m, n, f, blocks[2].index(third) + 1)[0] + 360
        elif m + degrees(m, n, f, blocks[2].index(third) + 1)[0] > 360:
            m += degrees(m, n, f, blocks[2].index(third) + 1)[0] - 360
        else:
            m += degrees(m, n, f, blocks[2].index(third) + 1)[0]
        n += degrees(m, n, f, blocks[2].index(third) + 1)[1]
        f += degrees(m, n, f, blocks[2].index(third) + 1)[2]

        made[col].append(blocks[2][blocks[2].index(third)])


        print(f'Чтобы доехать от {blocks[2].index(third) + 1} башни (маленький кубик) до столбца # {col + 1} '
              f'поворачиваемся на {degrees(m, n, f, h)[0]}, {degrees(m, n, f, h)[1]}, '
              f'{degrees(m, n, f, h)[2]}, {qnum(col)}')


        if m + degrees(m, n, f, h)[0] < 0:
            m += degrees(m, n, f, h)[0] + 360
        elif m + degrees(m, n, f, h)[0] > 360:
            m += degrees(m, n, f, h)[0] - 360
        else:
            m += degrees(m, n, f, h)[0]
        n += degrees(m, n, f, h)[1]
        f += degrees(m, n, f, h)[2]
        blocks[2][blocks[2].index(third)] = ''
        qnum(col)


pprint(algo)
pprint(made)
