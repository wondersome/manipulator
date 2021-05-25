from pprint import pprint
from project import degrees
import time
import math
from motors import motor
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT) 
GPIO.setup(24, GPIO.OUT) 

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
        print("выкидываем кубик поворачиваясь на градус", degrees(m, 0, int(blocks[1].index(x) + 1)))
        motor(blocks[1].index(x) + 1)
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

        print(f'{blocks[1].index(first) + 1} маленький кубик перемещаем из колоды в строй под номером # {col + 1}',
              degrees(m, 0, blocks[1].index(first) + 1))
        motor(blocks[1].index(first) + 1)

        if m + degrees(m, 0, blocks[1].index(first) + 1) < 0:
            m += degrees(m, 0, blocks[1].index(first) + 1) + 360
        elif m + degrees(m, 0, blocks[1].index(first) + 1) > 360:
            m += degrees(m, 0, blocks[1].index(first) + 1) - 360
        else:
            m += degrees(m, 0, blocks[1].index(first) + 1)

        print(f'все перемещение от {blocks[1].index(first) + 1} маленького кубика до строя № {col + 1}', degrees(m, 0, h))

        motor(degrees(m, 0, h))

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
        print(f'расстояние от {h} позиции до {big + 1} большого кубика', degrees(m, 0, big + 1))
        motor(degrees(m, 0, big + 1))

        if m + degrees(m, 0, big + 1) < 0:
            m += degrees(m, 0, big + 1) + 360
        elif m + degrees(m, 0, big + 1) > 360:
            m += degrees(m, 0, big + 1) - 360
        else:
            m += degrees(m, 0, big + 1)

        print(f'все перемещение от большого кубика {big + 1} до строя # {col + 1}', degrees(m, 0, h))

        motor(degrees(m, 0, h))

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
            print(f'расстояние от предыдущей позиции до {big + 1} маленького кубика {degrees(m, 0, big + 1)}')
            motor(degrees(m, 0, big + 1))
            if m + degrees(m, 0, big + 1) < 0:
                m += degrees(m, 0, big + 1) + 360
            elif m + degrees(m, 0, big + 1) > 360:
                m += degrees(m, 0, big + 1) - 360
            else:
                m += degrees(m, 0, big + 1)

            print(f'все перемещение от маленького кубика {big + 1} до другой колоды # {tmp + 1}', degrees(m, 0, tmp + 1))

            motor(degrees(m, 0, tmp + 1))

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
            print(f'расстояние от предыдущей позиции до {big + 1} маленького кубика {degrees(m, 0, big + 1)}')

            motor(degrees(m, 0, big + 1))
            if m + degrees(m, 0, big + 1) < 0:
                m += degrees(m, 0, big + 1) + 360
            elif m + degrees(m, 0, big + 1) > 360:
                m += degrees(m, 0, big + 1) - 360
            else:
                m += degrees(m, 0, big + 1)
            print(f'расстояние от {big + 1} маленького до такого же в другой позиции номер # {tmp + 1} {degrees(m, 0, tmp + 1)}')

            motor(degrees(m, 0, tmp + 1))

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
        print(f'{big + 1} большой кубик в строй под номером # {col + 1}', degrees(m, 0, big + 1))

        motor(degrees(m, 0, big + 1))
        if m + degrees(m, 0, big + 1) < 0:
            m += degrees(m, 0, big + 1)+360
        elif m + degrees(m, 0, big + 1) > 360:
            m += degrees(m, 0, big + 1)-360
        else:
            m += degrees(m, 0, big + 1)

        print(f'расстояние от {big + 1} большого кубика в строй до строя под номером # {col + 1}', degrees(m, 0, h))

        motor(degrees(m, 0, h))

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
            print(f'{blocks[1].index(second) + 1} маленький кубик(сколько до него ехать) {degrees(m, 0, blocks[1].index(second) + 1)}')

            motor(degrees(m, 0, blocks[1].index(second) + 1))
            if m + degrees(m, 0, blocks[1].index(second) + 1) < 0:
                m += degrees(m, 0, blocks[1].index(second) + 1) + 360
            elif m + degrees(m, 0, blocks[1].index(second) + 1) > 360:
                m += degrees(m, 0, blocks[1].index(second) + 1) - 360
            else:
                m += degrees(m, 0, blocks[1].index(second) + 1)

            print(f'расстояние от {blocks[1].index(second) + 1} маленького кубика до строя под номером # {col + 1} {degrees(m, 0, h)}')

            motor(degrees(m, 0, h))

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

            print(f'{blocks[2].index(second) + 1} маленький кубик(сколько до него ехать) {degrees(m, 0, blocks[2].index(second) + 1)}')

            motor(degrees(m, 0, blocks[2].index(second) + 1))
            if m + degrees(m, 0, blocks[2].index(second) + 1) < 0:
                m += degrees(m, 0, blocks[1].index(second) + 1) + 360
            elif m + degrees(m, 0, blocks[2].index(second) + 1) > 360:
                m += degrees(m, 0, blocks[2].index(second) + 1) - 360
            else:
                m += degrees(m, 0, blocks[2].index(second) + 1)

            print(f'расстояние от {blocks[2].index(second) + 1} маленького кубика до строя под номером # {col + 1} {degrees(m, 0, h)}')

            motor(degrees(m, 0, h))

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

        print(f'{mid + 1} большой кубик(сколько до него ехать) {degrees(m, 0, mid + 1)}')

        motor(degrees(m, 0, mid + 1))
        if m + degrees(m, 0, mid + 1) < 0:
            m += degrees(m, 0, mid + 1) + 360
        elif m + degrees(m, 0, mid + 1) > 360:
            m += degrees(m, 0, mid + 1) - 360
        else:
            m += degrees(m, 0, mid + 1)

        print(f'расстояние от {mid + 1} большого кубика до строя под номером # {col + 1} {degrees(m, 0, h)}')

        motor(degrees(m, 0, h))

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
        print(f'{mid + 1} маленький из колоды в колоду номер(сколько ехать до {mid + 1} маленького кубика) # {tmp + 1} {degrees(m, 0, mid + 1)}')

        motor(degrees(m, 0, mid + 1))

        if m + degrees(m, 0, mid + 1) < 0:
            m += degrees(m, 0, mid + 1) + 360
        elif m + degrees(m, 0, mid + 1) > 360:
            m += degrees(m, 0, mid + 1) - 360
        else:
            m += degrees(m, 0, mid + 1)

        print(f'расстояние от {mid + 1} маленького кубика из колоды до колоды номер № {tmp + 1} {degrees(m, 0, tmp + 1)}')

        motor(degrees(m, 0, tmp + 1))

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

        print(f'{mid + 1} большой кубик(сколько до него ехать) {degrees(m, 0, mid + 1)}')

        motor(degrees(m, 0, mid + 1))

        if m + degrees(m, 0, mid + 1) < 0:
            m += degrees(m, 0, mid + 1) + 360
        elif m + degrees(m, 0, mid + 1) > 360:
            m += degrees(m, 0, mid + 1) - 360
        else:
            m += degrees(m, 0, mid + 1)

        print(f'расстояние от {mid + 1} большого кубика до строя под номером # {col + 1} {degrees(m, 0, h)}')

        motor(degrees(m, 0, h))

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

        print(f'{blocks[1].index(third) + 1} маленький кубик(сколько до него ехать) {degrees(m, 0, blocks[1].index(third) + 1)}')

        motor(degrees(m, 0, blocks[1].index(third) + 1))
        if m +  degrees(m, 0, blocks[1].index(third) + 1) < 0:
            m += degrees(m, 0, blocks[1].index(third) + 1) + 360
        elif m + degrees(m, 0, blocks[1].index(third) + 1) > 360:
            m += degrees(m, 0, blocks[1].index(third) + 1) - 360
        else:
            m += degrees(m, 0, blocks[1].index(third) + 1)

        print(f'расстояние от {blocks[1].index(third) + 1} маленького кубика до строя под номером # {col + 1} {degrees(m, 0, h)}')

        motor(degrees(m, 0, h))

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

        print(f'{blocks[2].index(third) + 1} маленький кубик(сколько до него ехать) {degrees(m, 0, blocks[2].index(third) + 1)}')

        motor(degrees(m, 0, blocks[2].index(third) + 1))
        if m + degrees(m, 0, blocks[2].index(third) + 1) < 0:
            m += degrees(m, 0, blocks[2].index(third) + 1) + 360
        elif m + degrees(m, 0, blocks[2].index(third) + 1) > 360:
            m += degrees(m, 0, blocks[2].index(third) + 1) - 360
        else:
            m += degrees(m, 0, blocks[2].index(third) + 1)

        print(f'расстояние от {blocks[2].index(third) + 1} маленького кубика до строя под номером # {col + 1} {degrees(m, 0, h)}')

        motor(degrees(m, 0, h))

        if m + degrees(m, 0, h) < 0:
            m += degrees(m, 0, h) + 360
        elif m + degrees(m, 0, h) > 360:
            m += degrees(m, 0, h) - 360
        else:
            m += degrees(m, 0, h)
        blocks[2][blocks[2].index(third)] = ''

pprint(algo)







