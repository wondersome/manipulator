
from motor_control.motors import motor
from motor_control.degrees import degrees
from threading import Thread
import time
from num import qnum, cnum, abcs
m = 90
n =0
f = 0
while 1:
    h = int(input())
    motor(1, degrees(m, n, f, h)[0], 0)
    motor(2, degrees(m, n, f, h)[1], 0)
    motor(3, degrees(m, n, f, h)[2], 0)
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
