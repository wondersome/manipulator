from threading import Thread
from motor_control.degrees import degrees
from motor_control.height import height
import math
import RPi.GPIO as GPIO
import time
from motor_control.motors import motor
from num import qnum, cnum, abcs
def algo(value, value1, value2, made, col):

    def morgenshtern(deg1, deg2, deg3):
        # p1 = Thread(target=motor, args=(1, deg1, 0))
        # p2 = Thread(target=motor, args=(2, deg2, 0))
        # p3 = Thread(target=motor, args=(3, deg3, 0))
        # p1.start()
        # p2.start()
        # p3.start()
        # while p1.isAlive()==1 or p2.isAlive()==1 or  p3.isAlive() == 1:
        #     time.sleep(0.1)
        motor(1, deg1, 0)
        motor(2, deg2, 0)
        motor(3, deg3, 0)
        


 
 
 
 
    global m
    global n
    global f
    indexes = []


    if col == 0:
        w = 8
    elif col == 1:
        w = 6
    elif col == 2:
        w = 7

    with open('shance.txt') as file:
        content= file.readlines()
    content = [x.strip() for x in content]
    m=float(content[0])
    n=float(content[1])
    f=float(content[2])
    file.close()
    file=open("shance.txt","r+")
    file.truncate(0)
    file.close()

    def output_to_small(value):

        global n, f, m
        print(f'Чтобы доехать до {value + 1} башни (маленький кубик) поворачивааемся на '
            f'{degrees(m, n, f, value + 1)[0]}, '
            f'{degrees(m, n, f, value + 1)[1]}, '
            f'{degrees(m, n, f, value + 1)[2]}, '
            f'{cnum(value, value1)}')
        morgenshtern(degrees(m, n, f, value + 1)[0],degrees(m, n, f, value + 1)[1],degrees(m, n, f, value + 1)[2])
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
        motor(4,cnum(value,value1),1)
    def output_to_big(value):

        global n, f, m
        print(f'Чтобы доехать до {value + 1} башни (большой кубик) поворачивааемся на '
            f'{degrees(m, n, f, value + 1)[0]}, '
            f'{degrees(m, n, f, value + 1)[1]}, '
            f'{degrees(m, n, f, value + 1)[2]}, '
            f'{cnum(value, value1)}')
        morgenshtern(degrees(m, n, f, value + 1)[0],degrees(m, n, f, value + 1)[1],degrees(m, n, f, value + 1)[2])
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
        motor(4,cnum(value,value1),1)

    def output_from_small(val):

        global n, f, m
        h = w
        print(f'Чтобы доехать от {val + 1} башни (маленький кубик) до столбца # {col + 1} поворачиваемся на '
            f'{degrees(m, n, f, h)[0]}, '
            f'{degrees(m, n, f, h)[1]}, '
            f'{degrees(m, n, f, h)[2]}, '
            f'{qnum(col, made)}')
        morgenshtern(degrees(m, n, f, h)[0],degrees(m, n, f, h)[1],degrees(m, n, f, h)[2])
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

        motor(4,qnum(col,made),0)

    def output_from_big(val):

        global n, f, m
        h = w
        print(f'Чтобы доехать от {val + 1} башни (большой кубик) до столбца # {col + 1} поворачиваемся на '
            f'{degrees(m, n, f, h)[0]}, '
            f'{degrees(m, n, f, h)[1]}, '
            f'{degrees(m, n, f, h)[2]}, '
            f'{qnum(col, made)}')
        morgenshtern(degrees(m, n, f, h)[0],degrees(m, n, f, h)[1],degrees(m, n, f, h)[2])
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
        motor(4,qnum(col,made),0)

    def same(value, value2):

        global n, f, m
        print(f'Чтобы доехать от {value + 1} башни (маленький кубик) до башни # {value2 + 1} поворачиваемся на '
                    f'{degrees(m, n, f, value2 + 1)[0]}, '
                    f'{degrees(m, n, f, value2 + 1)[1]}, '
                    f'{degrees(m, n, f, value2 + 1)[2]}, '
                    f'{cnum(value2, value1)}')
        morgenshtern(degrees(m, n, f, value2 + 1)[0],degrees(m, n, f, value2 + 1)[1],degrees(m, n, f, value2 + 1)[2])
        a=abcs(degrees(m, n, f, value2 + 1)[0], 1)
        b=abcs(degrees(m, n, f, value2 + 1)[1], 2)
        c=abcs(degrees(m, n, f, value2 + 1)[2], 3)
        if m + a < 0:
            m += a + 360
        elif m + a > 360:
            m += a - 360
        else:
            m += a
        n += b
        f += c
        motor(4,cnum(value2,value1),0)
    am = []



    for x in value1[1]:
        if x not in value[0] + value[1] + value[2]:
            if value1[0][value1[1].index(x)] in value[0] + value[1] + value[2]:
                value2.append(f'{value1[1].index(x) + 1} throw from blocks')
                print(f'выкидываем кубик {value1[1].index(x) + 1} поворачиваясь на градус",'
                f' {degrees(m, n, f, value1[1].index(x) + 1)[0]}, '
                f'{degrees(m, n, f, value1[1].index(x) + 1)[1]}, '
                f'{degrees(m, n, f, value1[1].index(x) + 1)[2]}, {height(1, 1)}')
                morgenshtern(degrees(m, n, f, value1[1].index(x) + 1)[0],degrees(m, n, f, value1[1].index(x) + 1)[1],degrees(m, n, f, value1[1].index(x) + 1)[2])
                a=abcs(degrees(m, n, f, value1[1].index(x) + 1)[0], 1)
                b=abcs(degrees(m, n, f, value1[1].index(x) + 1)[1], 2)
                c=abcs(degrees(m, n, f, value1[1].index(x) + 1)[2], 3)
                motor(4,height(1,1),1)

                if m + a < 0:
                    m += a+360
                elif m + a > 360:
                    m += a-360
                else:
                    m += a
                f += c
                n+=b
                if n>0:
                    b=abcs(40, 2)
                    motor(2,40,0)
                    motor(4,height(2,1),0)
                    n+=b
                    b=abcs(-40, 2)
                    motor(2,-40,0)
                    n+=b
                else:
                    b=abcs(-40, 2)
                    motor(2,-40,0)
                    motor(4,height(2,1),0)
                    n+=b
                    b=abcs(40, 2)
                    motor(2,40,0)
                    n+=b
                value1[1][value1[1].index(x)] = ''

            else:
                am.append(x)

                





 
    if col == 0:
        a = 0
        b = 1
    elif col == 1:
        a = 1
        b = 2
    elif col == 2:
        a = 2
        b = 3

    arr = []


    for col in range(a, b):

        first, second, third = value[col]

        # Если на схеме в ряду только 1 кубик, то ищем среди маленьких кубиков кубик нужного цвета
        if second == '':
            value2.append(f'{value1[1].index(first) + 1} small blocks to column # {col + 1}')

            output_to_small(value1[1].index(first))
            made[col].append(value1[1][value1[1].index(first)])
            output_from_small(value1[1].index(first))
            value1[1][value1[1].index(first)] = ''

            continue

        big = value1[0].index(first)
        if value1[1][big] == '':  # Проверяем есть ли сверху маленький кубик
            value2.append(f'{big + 1} big blocks to column # {col + 1}')  # Перемещаем если сверху нет маленького кубика
            output_to_big(big)
            made[col].append(value1[0][big])
            output_from_big(big)
            value1[0][big] = ''

        else:
            for i in range(5):
                if i != big:
                    #f value1[2][i] == '' and value1[1][i] != second and value1[0][i] != second:
                    if value1[0][i] == '' or value1[len(value1[0][i]) + len(value1[1][i]) + len(value1[2][i])-1][i] == (am[0] or am[1])  or value1[len(value1[0][i]) + len(value1[1][i]) + len(value1[2][i])-1][i].isupper() == True:
                        indexes.append(i)
                        

                    
                    
            tmp=5
            for i in range(len(indexes)):
                if abs(big-indexes[i])<tmp:
                    tmp=abs(big-indexes[i])
                    indexes[0]=indexes[i]
            if value1[1][indexes[0]] == '': # если сверху(только один кубик есть) нет кубика то перемещаем
                value2.append(f'{big + 1} small blocks to blocks # {indexes[0] + 1}')
                output_to_small(big)
                value1[1][indexes[0]] = value1[1][big]
                same(big, indexes[0])
                value1[1][big] = ''
            else:  # если наверху два кубика, то перемещаем
                value2.append(f'{big + 1} small blocks to blocks # {indexes[0] + 1}')
                output_to_small(big)
                value1[2][indexes[0]] = value1[1][big]
                same(big, indexes[0])
                value1[1][big] = ''


            value2.append(f'{big + 1} big blocks to column # {col + 1}')# после того как расчистили все сверху, всегда 1 большой кубик

            output_to_big(big)
            made[col].append(value1[0][big]) #changed
            output_from_big(big)
            value1[0][big] = ''

        if third == '':  # Если на схеме нужно построить только 2 ряда
            if second in value1[1]:  # Если маленький кубик который нам нужен находится во 2 ряду, то перемещаем его
                value2.append(f'{value1[1].index(second) + 1} small blocks to column # {col + 1}')
                output_to_small(value1[1].index(second))
                made[col].append(value1[1][value1[1].index(second)])
                output_from_small(value1[1].index(second))
                value1[1][value1[1].index(second)] = ''

            else:  # Иначе кубик находится в 3 ряду, где 2 кубика больших, перемещаем его
                value2.append(f'{value1[2].index(second) + 1} small blocks to column # {col + 1}')
                output_to_small(value1[2].index(second))
                made[col].append(value1[2][value1[2].index(second)])
                output_from_small(value1[2].index(second))
                value1[2][value1[2].index(second)] = ''

            continue

        mid = value1[0].index(second)
        if value1[1][mid] == '':  # Если сверху никаких кубиков нет, то большой кубик перемещаеам
            value2.append(f'{mid + 1} big blocks to column # {col + 1}')

            output_to_big(mid)
            made[col].append(value1[0][mid])
            output_from_big(mid)
            value1[0][mid] = ''

        else:
            for i in range(5):
                if i != mid:
                    #if value1[0][i] != '' and value1[2][i] == '' and value1[1][i] != third:
                    if value1[0][i] == '' or value1[len(value1[0][i]) + len(value1[1][i]) + len(value1[2][i])-1][i] == (am[0] or am[1])  or value1[len(value1[0][i]) + len(value1[1][i]) + len(value1[2][i])-1][i].isupper() == True:
                        tmp = i
                        indexes.append(tmp)
                    
                    # else:
                    #     if value1[0][i] != '' and value1[2][i] == '' and value1[0][i] != third:
                    #         tmp = i
                    #         indexes.append(tmp)
            tmp=5
            for i in range(len(indexes)):
                if abs(big-indexes[i])<tmp:
                    tmp=abs(big-indexes[i])
                    indexes[0]=indexes[i]
            tmp=indexes[0]
            value2.append(f'{mid + 1} small blocks to blocks # {tmp + 1}')
            output_to_small(mid)
            if value1[1][tmp] == '':
                value1[1][tmp] = value1[1][mid]
            else:
                value1[2][tmp] = value1[1][mid]
            same(mid, tmp)
            value1[1][mid] = ''
            value2.append(f'{mid + 1} big blocks to column # {col + 1}')
            output_to_big(mid)
            made[col].append(value1[0][mid])
            output_from_big(mid)
            value1[0][mid] = ''


        if third in value1[1]: # Если один из элементов 3 столбца есть в колоде на 2 ряду, то перемещаеам его в нужный столбец

            value2.append(f'{value1[1].index(third) + 1} small blocks to column # {col + 1}')

            output_to_small(value1[1].index(third))
            made[col].append(value1[1][value1[1].index(third)])
            output_from_small(value1[1].index(third))
            value1[1][value1[1].index(third)] = ''

        else:  # Если один из элементов 3 столбца есть в колоде на 3 ряду, то перемещаеам его в нужный столбец
            value2.append(f'{value1[2].index(third) + 1} small blocks to column # {col + 1}')
            output_to_small(value1[2].index(third))
            made[col].append(value1[2][value1[2].index(third)])
            output_from_small(value1[2].index(third))
            value1[2][value1[2].index(third)] = ''
    with open('shance.txt', 'w') as file:
        file.write(str(m)+'\n')
        file.write(str(n)+'\n')
        file.write(str(f))
    file.close()
