import RPi.GPIO as GPIO
import time
from motor_control.motors import motor
from motor_control.height import height
from motor_control.degrees import degrees
from threading import Thread
from num import abcs
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.output(22, 0)
GPIO.output(12,1)
m = 0
n = 0
f = 0
while 1:
    #h = int(input()) 
    #p1 = Thread(target=motor, args=(1, n, 0))
    #p2 = Thread(target=motor, args=(2, m, 0))
    #p3 = Thread(target=motor, args=(3, k, 0))
    #p1.start()
    #motor(1, degrees(m, n, f, h)[0], 0)
    #motor(2, degrees(m, n, f, h)[1], 0)
    #motor(3, degrees(m, n, f, h)[2], 0)
    #a=abcs(degrees(m, n, f, h)[0], 1)
    #b=abcs(degrees(m, n, f,h)[1], 2)
    #c=abcs(degrees(m, n, f, h)[2], 3)
    """if m + a < 0:
        m += a + 360
    elif m + a > 360:
        m += a - 360
    else:
        m += a
    n += b
    f += c
    #p2.start()
    #p3.start()
    #while p2.isAlive()==1 and p3.isAlive() == 1:
        #time.sleep(0.1)
    """
    m = int(input())
    n = int(input())
    k = int(input())
    motor(1, m, 0)
    motor(2, n, 0)
    motor(3, k, 0)
