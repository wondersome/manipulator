from project import degrees
import time
import math

from pprint import pprint
from project import degrees

scheme = [['R', 'C', 'y'],
          ['G', 'b', ''],
          ['Y', 'c', '']]

blocks = [['B', 'C', 'G', 'R', 'Y'],
          ['y', 'r', 'c', 'g', 'b'],
          ['', '', '', '', '']]

algo = []
m = 90
# вычисляем какой кубик следует выкинуть
for x in blocks[1]:
    if x not in scheme[0] + scheme[1] + scheme[2]:
        algo.append(f'{blocks[1].index(x) + 1} throw from blocks')
        print(f'выкидываем кубик {blocks[1].index(x) + 1} поворачиваясь на градус", {degrees(m, 0, int(blocks[1].index(x) + 1))}')
        if m + degrees(m, 0, int(blocks[1].index(x) + 1)) < 0:
            m += degrees(m, 0, int(blocks[1].index(x) + 1))+360
        elif m + degrees(m, 0, int(blocks[1].index(x) + 1)) > 360:
            m += degrees(m, 0, int(blocks[1].index(x) + 1))-360
        else:
            m += degrees(m, 0, int(blocks[1].index(x) + 1))
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
              f'{degrees(m, 0, blocks[1].index(first) + 1)}')

        if m + degrees(m, 0, blocks[1].index(first) + 1) < 0:
            m += degrees(m, 0, blocks[1].index(first) + 1) + 360
        elif m + degrees(m, 0, blocks[1].index(first) + 1) > 360:
            m += degrees(m, 0, blocks[1].index(first) + 1) - 360
        else:
            m += degrees(m, 0, blocks[1].index(first) + 1)

        print(f'Чтобы доехать от {blocks[1].index(first) + 1} башни (маленький кубик) до столбца # {col + 1} '
              f'поварачиваемся на {degrees(m, 0, h)}')


        if m + degrees(m, 0, h) < 0:
            m += degrees(m, 0, h)+360
        elif m + degrees(m, 0, h) > 360:
            m += degrees(m, 0, h)-360
        else:
            m += degrees(m, 0, h)

        blocks[1][blocks[1].index(first)] = ''  # удаляем перемещенный элемент
        continue

    big = blocks[0].index(first)
    if blocks[1][big] == '':
        algo.append(f'{big + 1} big from blocks to column # {col + 1}')  # Перемещаем если сверху нет маленького кубика
        if col+1 == 1:
            h = 8
        elif col+1 == 2:
            h = 6
        elif col+1 == 3:
            h = 7
            #от {col+1} столбца
        print(f'Чтобы доехать до {big + 1} башни (большой кубик) поворачиваемся на '
              f'{degrees(m, 0, big + 1)}')

        if m + degrees(m, 0, big + 1) < 0:
            m += degrees(m, 0, big + 1) + 360
        elif m + degrees(m, 0, big + 1) > 360:
            m += degrees(m, 0, big + 1) - 360
        else:
            m += degrees(m, 0, big + 1)

        print(f'Чтобы доехать от {big + 1} большого кубика до столбца # {col + 1} поворачиваемся на', degrees(m, 0, h))


        if m + degrees(m, 0, h) < 0:
            m += degrees(m, 0, h)+360
        elif m + degrees(m, 0, h) > 360:
            m += degrees(m, 0, h)-360
        else:
            m += degrees(m, 0, h)

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
        if blocks[1][tmp] == '':
            algo.append(f'{big + 1} small from blocks to blocks # {tmp + 1}')

            print(f'Чтобы доехать до {big + 1} башни (маленький кубик) поворачиваемся на {degrees(m, 0, big + 1)}')
            if m + degrees(m, 0, big + 1) < 0:
                m += degrees(m, 0, big + 1) + 360
            elif m + degrees(m, 0, big + 1) > 360:
                m += degrees(m, 0, big + 1) - 360
            else:
                m += degrees(m, 0, big + 1)

            print(f'Чтобы доехать от {big + 1} башни (маленький кубик) до башни # {tmp + 1} поворачиваемся на',
                  degrees(m, 0, tmp + 1))


            if m + degrees(m, 0, tmp + 1) < 0:
                m += degrees(m, 0, tmp + 1) + 360
            elif m + degrees(m, 0, tmp + 1) > 360:
                m += degrees(m, 0, tmp + 1) - 360
            else:
                m += degrees(m, 0, tmp + 1)

            blocks[1][tmp] = blocks[1][big]
            blocks[1][big] = ''
        else:
            algo.append(f'{big + 1} small from blocks to blocks # {tmp + 1}')
            print(f'Чтобы доехать до {big + 1} башни (маленький кубик) поворачиваемся на {degrees(m, 0, big + 1)}')

            if m + degrees(m, 0, big + 1) < 0:
                m += degrees(m, 0, big + 1) + 360
            elif m + degrees(m, 0, big + 1) > 360:
                m += degrees(m, 0, big + 1) - 360
            else:
                m += degrees(m, 0, big + 1)
            print(f'Чтобы доехать от {big + 1} башни (маленький кубик) до башни # {tmp + 1} поворачиваемся на '
                  f'{degrees(m, 0, tmp + 1)}')


            if m + degrees(m, 0, tmp + 1) < 0:
                m += degrees(m, 0, tmp + 1) + 360
            elif m + degrees(m, 0, tmp + 1) > 360:
                m += degrees(m, 0, tmp + 1) - 360
            else:
                m += degrees(m, 0, tmp + 1)

            blocks[2][tmp] = blocks[1][big]
            blocks[1][big] = ''
        algo.append(f'{big + 1} big from blocks to column # {col + 1}')
        if col+1 == 1:
            h = 8
        elif col+1 == 2:
            h = 6
        elif col+1 == 3:
            h = 7
        print(f'Чтобы доехать до {big + 1} башни (большой кубик) поворачиваемся на {degrees(m, 0, big + 1)}')

        if m + degrees(m, 0, big + 1) < 0:
            m += degrees(m, 0, big + 1)+360
        elif m + degrees(m, 0, big + 1) > 360:
            m += degrees(m, 0, big + 1)-360
        else:
            m += degrees(m, 0, big + 1)

        print(f'Чтобы доехать от {big + 1} башни (большой кубик) до столбца # {col + 1} поворачиваемся '
              f'на {degrees(m, 0, h)}')


        if m + degrees(m, 0, h) < 0:
            m += degrees(m, 0, h)+360
        elif m + degrees(m, 0, h) > 360:
            m += degrees(m, 0, h)-360
        else:
            m += degrees(m, 0, h)
        blocks[0][big] = ''

    if third == '':
        if second in blocks[1]:
            algo.append(f'{blocks[1].index(second) + 1} small from blocks to column # {col + 1}')
            if col + 1 == 1:
                h = 8
            elif col + 1 == 2:
                h = 6
            elif col + 1 == 3:
                h = 7
            print(f'Чтобы доехать до {blocks[1].index(second) + 1} башни (маленький кубик) поворачиваемся на'
                  f' {degrees(m, 0, blocks[1].index(second) + 1)}')

            if m + degrees(m, 0, blocks[1].index(second) + 1) < 0:
                m += degrees(m, 0, blocks[1].index(second) + 1) + 360
            elif m + degrees(m, 0, blocks[1].index(second) + 1) > 360:
                m += degrees(m, 0, blocks[1].index(second) + 1) - 360
            else:
                m += degrees(m, 0, blocks[1].index(second) + 1)

            print(f'Чтобы доехать от {blocks[1].index(second) + 1} башни (маленький кубик) до столбца # {col + 1} '
                  f'поворачиваемся на {degrees(m, 0, h)}')


            if m + degrees(m, 0, h) < 0:
                m += degrees(m, 0, h)+360
            elif m + degrees(m, 0, h) > 360:
                m += degrees(m, 0, h)-360
            else:
                m += degrees(m, 0, h)
            blocks[1][blocks[1].index(second)] = ''
        else:
            algo.append(f'{blocks[2].index(second) + 1} small from blocks to column # {col + 1}')
            if col + 1 == 1:
                h = 8
            elif col + 1 == 2:
                h = 6
            elif col + 1 == 3:
                h = 7

            print(f'Чтобы доехать до {blocks[2].index(second) + 1} башни (маленький кубик)'
                  f' поворачиваемся на {degrees(m, 0, blocks[2].index(second) + 1)}')

            if m + degrees(m, 0, blocks[2].index(second) + 1) < 0:
                m += degrees(m, 0, blocks[1].index(second) + 1) + 360
            elif m + degrees(m, 0, blocks[2].index(second) + 1) > 360:
                m += degrees(m, 0, blocks[2].index(second) + 1) - 360
            else:
                m += degrees(m, 0, blocks[2].index(second) + 1)

            print(f'Чтобы доехать от {blocks[2].index(second) + 1} башни (маленький кубик) до столбца # '
                  f'{col + 1} поворачиваемся на {degrees(m, 0, h)}')


            if m + degrees(m, 0, h) < 0:
                m += degrees(m, 0, h)+360
            elif m + degrees(m, 0, h) > 360:
                m += degrees(m, 0, h)-360
            else:
                m += degrees(m, 0, h)

            blocks[2][blocks[2].index(second)] = ''
        continue

    mid = blocks[0].index(second)
    if blocks[1][mid] == '':
        algo.append(f'{mid + 1} big from blocks to column # {col + 1}')
        if col + 1 == 1:
            h = 8
        elif col + 1 == 2:
            h = 6
        elif col + 1 == 3:
            h = 7

        print(f'Чтобы доехать до {mid + 1} башни (большой кубик) поворачиваемся на {degrees(m, 0, mid + 1)}')

        if m + degrees(m, 0, mid + 1) < 0:
            m += degrees(m, 0, mid + 1) + 360
        elif m + degrees(m, 0, mid + 1) > 360:
            m += degrees(m, 0, mid + 1) - 360
        else:
            m += degrees(m, 0, mid + 1)

        print(f'Чтобы доехать от {mid + 1} большого кубика до столбца # {col + 1} поворачиваемся на{degrees(m, 0, h)}')


        if m + degrees(m, 0, h) < 0:
            m += degrees(m, 0, h) + 360
        elif m + degrees(m, 0, h) > 360:
            m += degrees(m, 0, h) - 360
        else:
            m += degrees(m, 0, h)

        blocks[0][mid] = ''
    else:
        for i in range(5):
            if blocks[0][i] != '':
                if blocks[2][i] == '':
                    if blocks[1][i] != third:
                        tmp = i
                        break
        algo.append(f'{mid + 1} small from blocks to blocks # {tmp + 1}')
        print(f'Чтобы доехать до {mid + 1} башни (маленький кубик) поворачиваемся на {degrees(m, 0, mid + 1)}')


        if m + degrees(m, 0, mid + 1) < 0:
            m += degrees(m, 0, mid + 1) + 360
        elif m + degrees(m, 0, mid + 1) > 360:
            m += degrees(m, 0, mid + 1) - 360
        else:
            m += degrees(m, 0, mid + 1)

        print(f'Чтобы доехать от {mid + 1} башни (маленький кубик) до башни # {tmp + 1} '
              f'поворачиваемся на {degrees(m, 0, tmp + 1)}')


        if m + degrees(m, 0, tmp + 1) < 0:
            m += degrees(m, 0, tmp + 1) + 360
        elif m + degrees(m, 0, tmp + 1) > 360:
            m += degrees(m, 0, tmp + 1) - 360
        else:
            m += degrees(m, 0, tmp + 1)

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

        print(f'Чтобы доехаать до {mid + 1} башни (большой кубик) поворачиваемся на {degrees(m, 0, mid + 1)}')


        if m + degrees(m, 0, mid + 1) < 0:
            m += degrees(m, 0, mid + 1) + 360
        elif m + degrees(m, 0, mid + 1) > 360:
            m += degrees(m, 0, mid + 1) - 360
        else:
            m += degrees(m, 0, mid + 1)

        print(f'Чтобы доехать от {mid + 1} башни (большой кубик) до столбца # {col + 1} '
              f'поворачиваемся на {degrees(m, 0, h)}')


        if m + degrees(m, 0, h) < 0:
            m += degrees(m, 0, h) + 360
        elif m + degrees(m, 0, h) > 360:
            m += degrees(m, 0, h) - 360
        else:
            m += degrees(m, 0, h)

        blocks[0][mid] = ''

    if third in blocks[1]:
        algo.append(f'{blocks[1].index(third) + 1} small from blocks to column # {col + 1}')
        if col + 1 == 1:
            h = 8
        elif col + 1 == 2:
            h = 6
        elif col + 1 == 3:
            h = 7

        print(f'Чтобы доехать до {blocks[1].index(third) + 1} башни (маленький кубик) поворачиваемся на'
              f' {degrees(m, 0, blocks[1].index(third) + 1)}')

        if m +  degrees(m, 0, blocks[1].index(third) + 1) < 0:
            m += degrees(m, 0, blocks[1].index(third) + 1) + 360
        elif m + degrees(m, 0, blocks[1].index(third) + 1) > 360:
            m += degrees(m, 0, blocks[1].index(third) + 1) - 360
        else:
            m += degrees(m, 0, blocks[1].index(third) + 1)

        print(f'Чтобы доехать от {blocks[1].index(third) + 1} башни (маленький кубик) до столбца # {col + 1} '
              f'поворачиваемся на {degrees(m, 0, h)}')


        if m + degrees(m, 0, h) < 0:
            m += degrees(m, 0, h) + 360
        elif m + degrees(m, 0, h) > 360:
            m += degrees(m, 0, h) - 360
        else:
            m += degrees(m, 0, h)
        blocks[1][blocks[1].index(third)] = ''
    else:
        algo.append(f'{blocks[2].index(third) + 1} small from blocks to column # {col + 1}')
        if col + 1 == 1:
            h = 8
        elif col + 1 == 2:
            h = 6
        elif col + 1 == 3:
            h = 7

        print(f'Чтобы доехать до {blocks[2].index(third) + 1} башни (маленький кубик) поворачиваемся на '
              f' {degrees(m, 0, blocks[2].index(third) + 1)}')

        if m + degrees(m, 0, blocks[2].index(third) + 1) < 0:
            m += degrees(m, 0, blocks[2].index(third) + 1) + 360
        elif m + degrees(m, 0, blocks[2].index(third) + 1) > 360:
            m += degrees(m, 0, blocks[2].index(third) + 1) - 360
        else:
            m += degrees(m, 0, blocks[2].index(third) + 1)

        print(f'Чтобы доехать от {blocks[2].index(third) + 1} башни (маленький кубик) до столбца # {col + 1} '
              f'поворачиваемся на {degrees(m, 0, h)}')


        if m + degrees(m, 0, h) < 0:
            m += degrees(m, 0, h) + 360
        elif m + degrees(m, 0, h) > 360:
            m += degrees(m, 0, h) - 360
        else:
            m += degrees(m, 0, h)
        blocks[2][blocks[2].index(third)] = ''

pprint(algo)







