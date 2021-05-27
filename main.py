from project import degrees
from pprint import pprint
from height import height
scheme = [['G', 'y', ''],
          ['R', 'C', 'r'],
          ['b', '', '']]

blocks = [['B', 'C', 'G', 'R', 'Y'],
          ['y', 'r', 'c', 'g', 'b'],
          ['', '', '', '', '']]
algo = []
made = [[], [], []]
m = 90
n = 0
f = 0
k = 15


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
    print(height(q, w), q, w)

def qnum(value):
    q = 0
    w = 0
    for i in made[value]:
        if i.isupper():
            q += 1
        elif i.islower():
            w += 1
    print(height(q, w), q, w)

# вычисляем какой кубик следует выкинуть
for x in blocks[1]:
    if x not in scheme[0] + scheme[1] + scheme[2]:
        algo.append(f'{blocks[1].index(x) + 1} throw from blocks')
        print(height(1, 1))
        blocks[1][blocks[1].index(x)] = ''


for col in range(3):
    first, second, third = scheme[col]
    # Если на схеме в ряду только 1 кубик, то ищем среди маленьких кубиков кубик нужного цвета
    if second == '':
        cnum(blocks[1].index(first))
        algo.append(f'{blocks[1].index(first) + 1} small from blocks to column # {col + 1}')
        made[col].append(blocks[1][blocks[1].index(first)])
        blocks[1][blocks[1].index(first)] = ''  # удаляем перемещенный элемент
        qnum(col)
        continue

    big = blocks[0].index(first)
    if blocks[1][big] == '':  # Проверяем есть ли сверху маленький кубик
        cnum(big)
        algo.append(f'{big + 1} big from blocks to column # {col + 1}')  # Перемещаем если сверху нет маленького кубика
        made[col].append(blocks[0][big])
        blocks[0][big] == ''

        qnum(col)

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
            cnum(big)
            algo.append(f'{big + 1} small from blocks to blocks # {tmp + 1}')
            blocks[2][tmp] = blocks[1][big]
            blocks[1][big] = ''
            qnum(tmp)

        cnum(big)
        algo.append(f'{big + 1} big from blocks to column # {col + 1}')# после того как расчистили все сверху, всегда 1 большой кубик
        made[col].append(blocks[0][big])
        blocks[0][big] = ''
        qnum(col)

    if third == '':  # Если на схеме нужно построить только 2 ряда
        if second in blocks[1]:  # Если маленький кубик который нам нужен находится во 2 ряду, то перемещаем его
            cnum(blocks[1].index(second))
            algo.append(f'{blocks[1].index(second) + 1} small from blocks to column # {col + 1}')
            made[col].append(blocks[1][blocks[1].index(second)])
            blocks[1][blocks[1].index(second)] = ''
            qnum(col)

        else:  # Иначе кубик находится в 3 ряду, где 2 кубика больших, перемещаем его
            cnum(blocks[2].index(second))
            algo.append(f'{blocks[2].index(second) + 1} small from blocks to column # {col + 1}')
            made[col].append(blocks[2][blocks[2].index(second)])
            blocks[2][blocks[2].index(second)] = ''
            qnum(col)

        continue

    mid = blocks[0].index(second)
    if blocks[1][mid] == '':  # Если сверху никаких кубиков нет, то большой кубик перемещаеам
        cnum(mid)
        algo.append(f'{mid + 1} big from blocks to column # {col + 1}')
        made[col].append(blocks[0][mid])
        blocks[0][mid] = ''
        qnum(col)

    else:
        for i in range(5):
            if blocks[0][i] != '':
                if blocks[2][i] == '':
                    if blocks[1][i] != third: # Если мы не используем 2 кубик(маленький) то ставим сверх него еще один кубик
                        tmp = i
                        break
        cnum(mid)
        algo.append(f'{mid + 1} small from blocks to blocks # {tmp + 1}')
        qnum(tmp)

        if blocks[1][tmp] == '':
            blocks[1][tmp] = blocks[1][mid]
        else:
            blocks[2][tmp] = blocks[1][mid]
        blocks[1][mid] = ''
        cnum(mid)
        algo.append(f'{mid + 1} big from blocks to column # {col + 1}')
        made[col].append(blocks[0][mid])
        blocks[0][mid] = ''
        qnum(col)

    if third in blocks[1]: # Если один из элементов 3 столбца есть в колоде на 2 ряду, то перемещаеам его в нужный столбец
        cnum(blocks[1].index(third))
        print(blocks[0][blocks[1].index(third)], blocks[1][blocks[1].index(third)], blocks[2][blocks[1].index(third)])

        algo.append(f'{blocks[1].index(third) + 1} small1 from blocks to column # {col + 1}')
        made[col].append(blocks[1][blocks[1].index(third)])
        blocks[1][blocks[1].index(third)] = ''
        qnum(col)

    else:  # Если один из элементов 3 столбца есть в колоде на 3 ряду, то перемещаеам его в нужный столбец
        cnum(blocks[2].index(third))
        algo.append(f'{blocks[2].index(third) + 1} small from blocks to column # {col + 1}')
        made[col].append(blocks[2][blocks[2].index(third)])
        blocks[2][blocks[2].index(third)] = ''
        qnum(col)


pprint(algo)
pprint(made)
