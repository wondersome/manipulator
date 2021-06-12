from threading import Thread
from motor_control.degrees import degrees
from motor_control.height import height
from motor_control.motors import motor
import RPi.GPIO as GPIO
import time

global m
global n
global f

m = 90
n = 0
f = 0
m1 = 0
m2 = 0
m3 = 0


def qnum(value):
    q = 0
    w = 0
    for i in made[value]:
        if i.isupper():
            q += 1
        elif i.islower():
            w += 1
    return height(q, w)

def abcs(o, f):
    if f == 1:
        coef = 0.075    
    elif f == 2:
        coef = 0.1125
    elif f == 3:
        coef = 0.225
    return(round( int(o/coef),0)*coef)

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
count = 0
a=0
b=0
c=0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
while GPIO.input(25)==0 :
    time.sleep(0.1)
# вычисляем какой кубик следует выкинуть
for x in blocks[1]:
    if x not in scheme[0] + scheme[1] + scheme[2]:
        algo.append(f'{blocks[1].index(x) + 1} throw from blocks')
        print(f'выкидываем кубик {blocks[1].index(x) + 1} поворачиваясь на градус",'
              f' {degrees(m, n, f, blocks[1].index(x) + 1)[0]}, '
              f'{degrees(m, n, f, blocks[1].index(x) + 1)[1]}, '
              f'{degrees(m, n, f, blocks[1].index(x) + 1)[2]}, {height(1, 1)}')
        
        Thread(target=motor, args=(1, degrees(m, n, f, blocks[1].index(x) + 1)[0], 0)).start()
        Thread(target=motor, args=(2, degrees(m, n, f, blocks[1].index(x) + 1)[1], 0)).start()
        Thread(target=motor, args=(3, degrees(m, n, f, blocks[1].index(x) + 1)[2], 0)).start()
        a=abcs(degrees(m, n, f, blocks[1].index(x) + 1)[0], 1)
        b=abcs(degrees(m, n, f, blocks[1].index(x) + 1)[1], 2)
        c=abcs(degrees(m, n, f, blocks[1].index(x) + 1)[2], 3)
        print(degrees(m, n, f, blocks[1].index(x) + 1)[1])
        print(a, b, c)
        motor(4, height(1, 1), 1)
        n+=b
        motor(2, 40,0)
        b=abcs(40, 2)
        n+=b
        motor(4 ,height(1, 1), 0)
        motor(2, -40,0)
        b=abcs(-40, 2)
        n+=b
        if m + a < 0:
            m += a+360
        elif m + a > 360:
            m += a-360
        else:
            m += a
        f += c
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

        Thread(target=motor, args=(2, degrees(m, n, f, blocks[1].index(first) + 1)[1], 0)).start()
        Thread(target=motor, args=(3, degrees(m, n, f, blocks[1].index(first) + 1)[2], 0)).start()
        motor(1, degrees(m, n, f, blocks[1].index(first) + 1)[0], 0)
        a=abcs(degrees(m, n, f, blocks[1].index(first) + 1)[0], 1)
        b=abcs(degrees(m, n, f, blocks[1].index(first) + 1)[1], 2)
        c=abcs(degrees(m, n, f, blocks[1].index(first) + 1)[2], 3)
        motor(4, cnum(blocks[1].index(first)), 1)


        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m += a - 360
        else:
            m += a
        n += b
        f += c
        made[col].append(blocks[1][blocks[1].index(first)])

        print(f'Чтобы доехать от {blocks[1].index(first) + 1} башни (маленький кубик) до столбца # {col + 1} '
              f'поварачиваемся на '
              f'{degrees(m, n, f, h)[0]}, '
              f'{degrees(m, n, f, h)[1]}, '
              f'{degrees(m, n, f, h)[2]}, '
              f' {qnum(col)}')



        Thread(target=motor, args=(2, degrees(m, n, f, h)[1], 0)).start()
        Thread(target=motor, args=(3, degrees(m, n, f, h)[2], 0)).start()
        motor(1, degrees(m, n, f, h)[0], 0)
        a=abcs(degrees(m, n, f, h)[0], 1)
        b=abcs(degrees(m, n, f, h)[1], 2)
        c=abcs(degrees(m, n, f, h)[2], 3)
        motor(4, qnum(col), 0)

        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m += a - 360
        else:
            m += a
        n += b
        f += c
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


        Thread(target=motor, args=(2, degrees(m, n, f, big + 1)[1], 0)).start()
        Thread(target=motor, args=(3, degrees(m, n, f, big + 1)[2], 0)).start()
        motor(1, degrees(m, n, f, big + 1)[0], 0)
        a=abcs(degrees(m, n, f, big + 1)[0], 1)
        b=abcs(degrees(m, n, f, big + 1)[1], 2)
        c=abcs(degrees(m, n, f, big + 1)[2], 3)
        motor(4, cnum(big), 1)

        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m += a - 360
        else:
            m += a
        n += b
        f += c

        made[col].append(blocks[0][big])

        print(f'Чтобы доехать от {big + 1} большого кубика до столбца # {col + 1} поворачиваемся на '
              f'{degrees(m, n, f, h)[0]}, '
              f'{degrees(m, n, f, h)[1]}, '
              f'{degrees(m, n, f, h)[2]}, '
              f'{qnum(col)}')

        Thread(target=motor, args=(2, degrees(m, n, f, h)[1], 0)).start()
        Thread(target=motor, args=(3, degrees(m, n, f, h)[2], 0)).start()
        motor(1, degrees(m, n, f, h)[0], 0)
        a=abcs(degrees(m, n, f, h)[0], 1)
        b=abcs(degrees(m, n, f, h)[1], 2)
        c=abcs(degrees(m, n, f, h)[2], 3)
        motor(4, qnum(col), 0)



        if m + a < 0:
            m += a+360
        elif m + a > 360:
            m += a-360
        else:
            m += a
        n += b
        f += c

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

            print(f'Чтобы доехать до {big + 1} башни (маленький кубик) поворачиваемся на '
                  f'{degrees(m, n, f, big + 1)[0]}, '
                  f'{degrees(m, n, f, big + 1)[1]}, '
                  f'{degrees(m, n, f, big + 1)[2]}, '
                  f'{cnum(big)}')

            Thread(target=motor, args=(2, degrees(m, n, f, big + 1)[1], 0)).start()
            Thread(target=motor, args=(3, degrees(m, n, f, big + 1)[2], 0)).start()
            motor(1, degrees(m, n, f, big + 1)[0], 0)
            a=abcs(degrees(m, n, f, big + 1)[0], 1)
            b=abcs(degrees(m, n, f, big + 1)[1], 2)
            c=abcs(degrees(m, n, f, big + 1)[2], 3)
            motor(4, cnum(big), 1)

            if m + a < 0:
                m += a + 360
            elif m + a > 360:
                m += a - 360
            else:
                m += a
            n += b
            f += c

            made[col].append(blocks[0][big])

            print(f'Чтобы доехать от {big + 1} маленького кубика до кубика # {tmp + 1} поворачиваемся на '
                  f'{degrees(m, n, f, tmp + 1)[0]}, '
                  f'{degrees(m, n, f, tmp + 1)[1]}, '
                  f'{degrees(m, n, f, tmp + 1)[2]}, '
                  f'{cnum(tmp)}')

            Thread(target=motor, args=(2, degrees(m, n, f, tmp + 1)[1], 0)).start()
            Thread(target=motor, args=(3, degrees(m, n, f, tmp + 1)[2], 0)).start()
            motor(1, degrees(m, n, f, tmp + 1)[0], 0)
            a=abcs(degrees(m, n, f, tmp + 1)[0], 1)
            b=abcs(degrees(m, n, f, tmp + 1)[1], 2)
            c=abcs(degrees(m, n, f, tmp + 1)[2], 3)
            motor(4, qnum(col), 0)

            if m + a < 0:
                m += a + 360
            elif m + a > 360:
                m += a - 360
            else:
                m += a
            n += b
            f += c


            blocks[1][tmp] = blocks[1][big]
            blocks[1][big] = ''
            cnum(tmp)

        else:  # если наверху два кубика, то перемещаем
            algo.append(f'{big + 1} small from blocks to blocks # {tmp + 1}')
            print(
                f'Чтобы доехать до {big + 1} башни (маленький кубик) поворачиваемся на '
                f'{degrees(m, n, f, big + 1)[0]},'
                f'{degrees(m, n, f, big + 1)[1]}, '
                f'{degrees(m, n, f, big + 1)[2]}, '
                f'{cnum(big)}')


            Thread(target=motor, args=(2, degrees(m, n, f, big + 1)[1], 0)).start()
            Thread(target=motor, args=(3, degrees(m, n, f, big + 1)[2], 0)).start()
            motor(1, degrees(m, n, f, big + 1)[0], 0)
            a=abcs(degrees(m, n, f, big + 1)[0], 1)
            b=abcs(degrees(m, n, f, big + 1)[1], 2)
            c=abcs(degrees(m, n, f, big + 1)[2], 3)
            motor(4, cnum(big), 1)

            if m + a < 0:
                m += a + 360
            elif m + a > 360:
                m += a - 360
            else:
                m +=a
            n += b
            f += c

            made[col].append(blocks[0][big])

            print(f'Чтобы доехать от {big + 1} башни (маленький кубик) до башни # {tmp + 1} поворачиваемся на '
                  f'{degrees(m, n, f, tmp + 1)[0]}, '
                  f'{degrees(m, n, f, tmp + 1)[1]}, '
                  f'{degrees(m, n, f, tmp + 1)[2]}, '
                  f'{cnum(tmp)}')

            Thread(target=motor, args=(2, degrees(m, n, f, tmp + 1)[1], 0)).start()
            Thread(target=motor, args=(3, degrees(m, n, f, tmp + 1)[2], 0)).start()
            motor(1, degrees(m, n, f, tmp + 1)[0], 0)
            a=abcs(degrees(m, n, f, tmp + 1)[0], 1)
            b=abcs(degrees(m, n, f, tmp + 1)[1], 2)
            c=abcs(degrees(m, n, f, tmp + 1)[2], 3)
            motor(4, cnum(tmp), 0)

            if m + a < 0:
                m += a + 360
            elif m + a > 360:
                m +=a - 360
            else:
                m += a
            n += b
            f += c

            blocks[2][tmp] = blocks[1][big]
            blocks[1][big] = ''

        algo.append(f'{big + 1} big from blocks to column # {col + 1}')# после того как расчистили все сверху, всегда 1 большой кубик

        if col + 1 == 1:
            h = 8
        elif col + 1 == 2:
            h = 6
        elif col + 1 == 3:
            h = 7

        print(f'Чтобы доехать до {big + 1} башни (маленький кубик) поворачиваемся на '
              f'{degrees(m, n, f, big + 1)[0]}, '
              f'{degrees(m, n, f, big + 1)[1]}, '
              f'{degrees(m, n, f, big + 1)[2]}, '
              f'{cnum(big)}')

        Thread(target=motor, args=(2, degrees(m, n, f, big + 1)[1], 0)).start()
        Thread(target=motor, args=(3, degrees(m, n, f, big + 1)[2], 0)).start()
        motor(1, degrees(m, n, f, big + 1)[0], 0)
        a=abcs(degrees(m, n, f, big + 1)[0], 1)
        b=abcs(degrees(m, n, f, big + 1)[1], 2)
        c=abcs(degrees(m, n, f, big + 1)[2], 3)
        motor(4, cnum(big), 1)

        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m += a - 360
        else:
            m += a
        n += b
        f += c

        print(f'Чтобы доехать от {big + 1} башни (маленький кубик) до столбца # {col + 1} поворачиваемся на '
              f'{degrees(m, n, f, h)[0]}, '
              f'{degrees(m, n, f, h)[1]}, '
              f'{degrees(m, n, f, h)[2]}, '
              f'{qnum(tmp)}')

        Thread(target=motor, args=(2, degrees(m, n, f, h)[1], 0)).start()
        Thread(target=motor, args=(3, degrees(m, n, f, h)[2], 0)).start()
        motor(1, degrees(m, n, f, h)[0], 0)
        a=abcs(degrees(m, n, f, h)[0], 1)
        b=abcs(degrees(m, n, f, h)[1], 2)
        c=abcs(degrees(m, n, f, h)[2], 3)
        motor(4, qnum(col), 0)

        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m +=a - 360
        else:
            m += a
        n += b
        f += c

        blocks[0][big] = ''

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

            Thread(target=motor, args=(2, degrees(m, n, f, blocks[1].index(second) + 1)[1], 0)).start()
            Thread(target=motor, args=(3, degrees(m, n, f, blocks[1].index(second) + 1)[2], 0)).start()
            motor(1, degrees(m, n, f, blocks[1].index(second) + 1)[0], 0)
            a=abcs(degrees(m, n, f, blocks[1].index(second) + 1)[0], 1)
            b=abcs(degrees(m, n, f, blocks[1].index(second) + 1)[1], 2)
            c=abcs(degrees(m, n, f, blocks[1].index(second) + 1)[2], 3)
            motor(4, cnum(blocks[1].index(second)), 1)

            if m + a < 0:
                m +=a + 360
            elif m + a > 360:
                m += a - 360
            else:
                m += a
            n += b
            f += c

            made[col].append(blocks[1][blocks[1].index(second)])


            print(f'Чтобы доехать от {blocks[1].index(second) + 1} башни (маленький кубик) до столбца # {col + 1} '
                  f'поворачиваемся на {degrees(m, n, f, h)[0]}, '
                  f'{degrees(m, n, f, h)[1]}, '
                  f'{degrees(m, n, f, h)[2]}, '
                  f'{qnum(col)}')

            Thread(target=motor, args=(2, degrees(m, n, f, h)[1], 0)).start()
            Thread(target=motor, args=(3, degrees(m, n, f, h)[2], 0)).start()
            motor(1, degrees(m, n, f, h)[0], 0)
            a=abcs(degrees(m, n, f, h)[0], 1)
            b=abcs(degrees(m, n, f, h)[1], 2)
            c=abcs(degrees(m, n, f, h)[2], 3)
            motor(4, qnum(col), 0)


            if m + a < 0:
                m += a + 360
            elif m + a > 360:
                m += a-360
            else:
                m += a
            n += b
            f += c

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
                  f' поворачиваемся на '
                  f'{degrees(m, n, f, blocks[2].index(second) + 1)[0]},'
                  f' {degrees(m, n, f, blocks[2].index(second) + 1)[1]}, '
                  f'{degrees(m, n, f, blocks[2].index(second) + 1)[2]}, '
                  f'{cnum(blocks[2].index(second))}')

            Thread(target=motor, args=(2, degrees(m, n, f, blocks[2].index(second) + 1)[1], 0)).start()
            Thread(target=motor, args=(3, degrees(m, n, f, blocks[2].index(second) + 1)[2], 0)).start()
            motor(1, degrees(m, n, f, blocks[2].index(second) + 1)[0], 0)
            a=abcs(degrees(m, n, f, blocks[2].index(second) + 1)[0], 1)
            b=abcs(degrees(m, n, f, blocks[2].index(second) + 1)[1], 2)
            c=abcs(degrees(m, n, f, blocks[2].index(second) + 1)[2], 3)
            motor(4, cnum(blocks[2].index(second)), 1)

            if m + a < 0:
                m += a + 360
            elif m + a > 360:
                m += a - 360
            else:
                m += a
            n += b
            f += c

            made[col].append(blocks[2][blocks[2].index(second)])


            print(f'Чтобы доехать от {blocks[2].index(second) + 1} башни (маленький кубик) до столбца # '
                  f'{col + 1} поворачиваемся на '
                  f'{degrees(m, n, f, h)[0]}, '
                  f'{degrees(m, n, f, h)[1]}, '
                  f'{degrees(m, n, f, h)[2]}, '
                  f'{qnum(col)}')

            Thread(target=motor, args=(2, degrees(m, n, f, h)[1], 0)).start()
            Thread(target=motor, args=(3, degrees(m, n, f, h)[2], 0)).start()
            motor(1, degrees(m, n, f, h)[0], 0)
            a=abcs(degrees(m, n, f, h)[0], 1)
            b=abcs(degrees(m, n, f, h)[1], 2)
            c=abcs(degrees(m, n, f, h)[2], 3)
            motor(4, qnum(col), 0)


            if m + a < 0:
                m += a+360
            elif m + a > 360:
                m += a-360
            else:
                m += a
            n += b
            f += c

            blocks[2][blocks[2].index(second)] = ''

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

        print(f'Чтобы доехать до {mid + 1} башни (большой кубик) поворачиваемся на '
              f'{degrees(m, n, f, mid + 1)[0]}, '
              f'{degrees(m, n, f, mid + 1)[1]}, '
              f'{degrees(m, n, f, mid + 1)[2]}, '
              f'{cnum(mid)}')

        Thread(target=motor, args=(2, degrees(m, n, f, mid + 1)[1], 0)).start()
        Thread(target=motor, args=(3, degrees(m, n, f, mid + 1)[2], 0)).start()
        motor(1, degrees(m, n, f, mid + 1)[0], 0)
        a=abcs(degrees(m, n, f, mid + 1)[0], 1)
        b=abcs(degrees(m, n, f, mid + 1)[1], 2)
        c=abcs(degrees(m, n, f, mid + 1)[2], 3)
        motor(4, cnum(mid), 1)

        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m += a - 360
        else:
            m += a
        n +=b
        f += c
        made[col].append(blocks[0][mid])

        print(f'Чтобы доехать от {mid + 1} большого кубика до столбца # {col + 1} поворачиваемся на '
              f'{degrees(m, n, f, h)[0]}, '
              f'{degrees(m, n, f, h)[1]}, '
              f'{degrees(m, n, f, h)[2]}, '
              f'{qnum(col)}')

        Thread(target=motor, args=(2, degrees(m, n, f, h)[1], 0)).start()
        Thread(target=motor, args=(3, degrees(m, n, f, h)[2], 0)).start()
        motor(1, degrees(m, n, f, h)[0], 0)
        a=abcs(degrees(m, n, f, h)[0], 1)
        b=abcs(degrees(m, n, f, h)[1], 2)
        c=abcs(degrees(m, n, f, h)[2], 3)
        motor(4, qnum(col), 0)


        if m + a < 0:
            m += a + 360
        elif m +a > 360:
            m += a - 360
        else:
            m += a
        n += b
        f += c

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
              f'{degrees(m, n, f, mid + 1)[0]}, '
              f'{degrees(m, n, f, mid + 1)[1]}, '
              f'{degrees(m, n, f, mid + 1)[2]}, '
              f'{cnum(mid)}')

        Thread(target=motor, args=(2, degrees(m, n, f, mid + 1)[1], 0)).start()
        Thread(target=motor, args=(3, degrees(m, n, f, mid + 1)[2], 0)).start()
        motor(1, degrees(m, n, f, mid + 1)[0], 0)
        a=abcs(degrees(m, n, f, mid + 1)[0], 1)
        b=abcs(degrees(m, n, f, mid + 1)[1], 2)
        c=abcs(degrees(m, n, f, mid + 1)[2], 3)
        motor(4, cnum(mid), 1)

        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m += a - 360
        else:
            m += a
        n += b
        f += c

        print(f'Чтобы доехать от {mid + 1} башни (маленький кубик) до башни # {tmp + 1} '
              f'поворачиваемся на '
              f'{degrees(m, n, f, tmp + 1)[0]}, '
              f'{degrees(m, n, f, tmp + 1)[1]}, '
              f'{degrees(m, n, f, tmp + 1)[2]}, '
              f'{cnum(tmp)}')

        Thread(target=motor, args=(2, degrees(m, n, f, tmp + 1)[1], 0)).start()
        Thread(target=motor, args=(3, degrees(m, n, f, tmp + 1)[2], 0)).start()
        motor(1, degrees(m, n, f, tmp + 1)[0], 0)
        a=abcs(degrees(m, n, f, tmp + 1)[0], 1)
        b=abcs(degrees(m, n, f, tmp + 1)[1], 2)
        c=abcs(degrees(m, n, f, tmp + 1)[2], 3)
        motor(4, cnum(tmp), 0)

        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m += a - 360
        else:
            m +=a
        n += b
        f += c

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
              f'{degrees(m, n, f, mid + 1)[0]}, '
              f'{degrees(m, n, f, mid + 1)[1]}, '
              f'{degrees(m, n, f, mid + 1)[2]}, '
              f'{cnum(mid)}')

        Thread(target=motor, args=(2, degrees(m, n, f, mid + 1)[1], 0)).start()
        Thread(target=motor, args=(3, degrees(m, n, f, mid + 1)[2], 0)).start()
        motor(1, degrees(m, n, f, mid + 1)[0], 0)
        a=abcs(degrees(m, n, f, mid + 1)[0], 1)
        b=abcs(degrees(m, n, f, mid + 1)[1], 2)
        c=abcs(degrees(m, n, f, mid + 1)[2], 3)
        motor(4, cnum(mid), 1)


        if m + a < 0:
            m += a + 360
        elif m +a> 360:
            m +=a - 360
        else:
            m += a
        n += b
        f += c

        made[col].append(blocks[0][mid])


        print(f'Чтобы доехать от {mid + 1} башни (большой кубик) до столбца # {col + 1} '
              f'поворачиваемся на '
              f'{degrees(m, n, f, h)[0]}, '
              f'{degrees(m, n, f, h)[1]}, '
              f'{degrees(m, n, f, h)[2]}, '
              f'{qnum(col)}')

        Thread(target=motor, args=(2, degrees(m, n, f, h)[1], 0)).start()
        Thread(target=motor, args=(3, degrees(m, n, f, h)[2], 0)).start()
        motor(1, degrees(m, n, f, h)[0], 0)
        a=abcs(degrees(m, n, f, h)[0], 1)
        b=abcs(degrees(m, n, f, h)[1], 2)
        c=abcs(degrees(m, n, f, h)[2], 3)
        motor(4, qnum(col), 0)


        if m + a < 0:
            m +=a + 360
        elif m + a > 360:
            m += a - 360
        else:
            m +=a
        n += b
        f += c


        blocks[0][mid] = ''

    if third in blocks[1]: # Если один из элементов 3 столбца есть в колоде на 2 ряду, то перемещаеам его в нужный столбец

        algo.append(f'{blocks[1].index(third) + 1} small1 from blocks to column # {col + 1}')

        if col + 1 == 1:
            h = 8
        elif col + 1 == 2:
            h = 6
        elif col + 1 == 3:
            h = 7

        print(f'Чтобы доехать до {blocks[1].index(third) + 1} башни (маленький кубик) поворачиваемся на'
              f' {degrees(m, n, f, blocks[1].index(third) + 1)[0]}, '
              f'{degrees(m, n, f, blocks[1].index(third) + 1)[1]},'
              f' {degrees(m, n, f, blocks[1].index(third) + 1)[2]}, '
              f'{cnum(blocks[1].index(third))}')

        Thread(target=motor, args=(2, degrees(m, n, f, blocks[1].index(third) + 1)[1], 0)).start()
        Thread(target=motor, args=(3, degrees(m, n, f, blocks[1].index(third) + 1)[2], 0)).start()
        motor(1, degrees(m, n, f, blocks[1].index(third) + 1)[0], 0)

        a=abcs(degrees(m, n, f, blocks[1].index(third) + 1)[0], 1)
        b=abcs(degrees(m, n, f, blocks[1].index(third) + 1)[1], 2)
        c=abcs(degrees(m, n, f, blocks[1].index(third) + 1)[2], 3)
        motor(4, cnum(blocks[1].index(third)), 1)

        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m +=a - 360
        else:
            m += a
        n += b
        f += c

        made[col].append(blocks[1][blocks[1].index(third)])


        print(f'Чтобы доехать от {blocks[1].index(third) + 1} башни (маленький кубик) до столбца # {col + 1} '
              f'поворачиваемся на '
              f'{degrees(m, n, f, h)[0]}, '
              f'{degrees(m, n, f, h)[1]}, '
              f'{degrees(m, n, f, h)[2]}, '
              f'{qnum(col)}')

        Thread(target=motor, args=(2, degrees(m, n, f, h)[1], 0)).start()
        Thread(target=motor, args=(3, degrees(m, n, f, h)[2], 0)).start()
        motor(1, degrees(m, n, f, h)[0], 0)
        a=abcs(degrees(m, n, f, h)[0], 1)
        b=abcs(degrees(m, n, f, h)[1], 2)
        c=abcs(3,degrees(m, n, f, h)[2], 3)
        motor(4, qnum(col), 0)

        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m += a - 360
        else:
            m += a

        n +=b
        f +=c
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
              f' {degrees(m, n, f, blocks[2].index(third) + 1)[0]}, '
              f'{degrees(m, n, f, blocks[2].index(third) + 1)[1]}, '
              f'{degrees(m, n, f, blocks[2].index(third) + 1)[2]}, '
              f'{cnum(blocks[2].index(third))}')

        Thread(target=motor, args=(2, degrees(m, n, f, blocks[2].index(third) + 1)[1], 0)).start()
        Thread(target=motor, args=(3, degrees(m, n, f, blocks[2].index(third) + 1)[2], 0)).start()
        motor(1, degrees(m, n, f, blocks[2].index(third) + 1)[0], 0)
        a=abcs(degrees(m, n, f, blocks[2].index(third) + 1)[0], 1)
        b=abcs(degrees(m, n, f, blocks[2].index(third) + 1)[1], 2)
        c=abcs(degrees(m, n, f, blocks[2].index(third) + 1)[2], 3)
        motor(4, cnum(blocks[2].index(third)), 1)

        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m +=a - 360
        else:
            m += a
        n += b
        f += c

        made[col].append(blocks[2][blocks[2].index(third)])

        print(f'Чтобы доехать от {blocks[2].index(third) + 1} башни (маленький кубик) до столбца # {col + 1} '
              f'поворачиваемся на '
              f'{degrees(m, n, f, h)[0]}, '
              f'{degrees(m, n, f, h)[1]}, '
              f'{degrees(m, n, f, h)[2]}, '
              f'{qnum(col)}')

        Thread(target=motor, args=(2, degrees(m, n, f, h)[1], 0)).start()
        Thread(target=motor, args=(3, degrees(m, n, f, h)[2], 0)).start()
        motor(1, degrees(m, n, f, h)[0], 0)

        a=abcs(degrees(m, n, f, h)[0], 1)
        b=abcs(degrees(m, n, f, h)[1], 2)
        c=abcs(degrees(m, n, f, h)[2], 3)
        motor(4, qnum(col), 0)

        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m += a - 360
        else:
            m += a
        n += b
        f += c
        blocks[2][blocks[2].index(third)] = ''



