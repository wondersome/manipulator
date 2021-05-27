from pprint import pprint
from project import degrees
import time
import math



scheme = [['G', 'y', ''],
          ['R', 'C', 'r'],
          ['b', '', '']]

blocks = [['B', 'C', 'G', 'R', 'Y'],
          ['y', 'r', 'c', 'g', 'b'],
          ['', '', '', '', '']]

algo = []
m = 90
n = 0
f = 0
# вычисляем какой кубик следует выкинуть
for x in blocks[1]:
    if x not in scheme[0] + scheme[1] + scheme[2]:
        algo.append(f'{blocks[1].index(x) + 1} throw from blocks')
        blocks[1][blocks[1].index(x)] = ''


for col in range(3):
    first, second, third = scheme[col]
    # Если на схеме в ряду только 1 кубик, то ищем среди маленьких кубиков кубик нужного цвета
    if second == '':
        algo.append(f'{blocks[1].index(first) + 1} small from blocks to column # {col + 1}')
        blocks[1][blocks[1].index(first)] = ''  # удаляем перемещенный элемент
        continue

    big = blocks[0].index(first)
    if blocks[1][big] == '':
        algo.append(f'{big + 1} big from blocks to column # {col + 1}')  # Перемещаем если сверху нет маленького кубика
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
            blocks[1][tmp] = blocks[1][big]
            blocks[1][big] = ''
        else:
            algo.append(f'{big + 1} small from blocks to blocks # {tmp + 1}')
            blocks[2][tmp] = blocks[1][big]
            blocks[1][big] = ''
        algo.append(f'{big + 1} big from blocks to column # {col + 1}')
        blocks[0][big] = ''

    if third == '':
        if second in blocks[1]:
            algo.append(f'{blocks[1].index(second) + 1} small from blocks to column # {col + 1}')
            blocks[1][blocks[1].index(second)] = ''
        else:
            algo.append(f'{blocks[2].index(second) + 1} small from blocks to column # {col + 1}')
            blocks[2][blocks[2].index(second)] = ''
        continue

    mid = blocks[0].index(second)
    if blocks[1][mid] == '':
        algo.append(f'{mid + 1} big from blocks to column # {col + 1}')
        blocks[0][mid] = ''
    else:
        for i in range(5):
            if blocks[0][i] != '':
                if blocks[2][i] == '':
                    if blocks[1][i] != third:
                        tmp = i
                        break
        algo.append(f'{mid + 1} small from blocks to blocks # {tmp + 1}')
        if blocks[1][tmp] == '':
            blocks[1][tmp] = blocks[1][mid]
        else:
            blocks[2][tmp] = blocks[1][mid]
        blocks[1][mid] = ''
        algo.append(f'{mid + 1} big from blocks to column # {col + 1}')
        blocks[0][mid] = ''

    if third in blocks[1]:
        algo.append(f'{blocks[1].index(third) + 1} small from blocks to column # {col + 1}')
        blocks[1][blocks[1].index(third)] = ''
    else:
        algo.append(f'{blocks[2].index(third) + 1} small from blocks to column # {col + 1}')

        blocks[2][blocks[2].index(third)] = ''

pprint(algo)

