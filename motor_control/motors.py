import math
import RPi.GPIO as GPIO
import time


def motor(m, n, l):
    if m == 1:
        dir = 23
        step = 24
        coef = 0.075
        k = 0.002
    elif m == 2:
        dir = 20
        step = 21
        coef = 0.1125
        k = 0.001
    elif m == 4:
        dir = 5
        step = 6
        coef = 0.225
        n = -n
        k = 0.0001
    elif m == 3:
        dir = 18
        step = 17
        coef = 0.225
        k = 0.003
        n = -n
    za_warudo=0
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dir, GPIO.OUT)
    GPIO.setup(step, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT) 
    GPIO.setup(12, GPIO.OUT)
    if int(n) < 0:
        GPIO.output(dir, False)
        n = math.fabs(n)

    else:
        GPIO.output(dir, True)
    i = int(0)
    first =round( int(n/coef),0)
    u = 0
    while i < first:
        GPIO.output(step, True)
        time.sleep(k)
        GPIO.output(step, False)
        time.sleep(k)
        i = i + 1
        za_warudo+=k*2
        if za_warudo>0.2 and m==1:
            za_warudo=0
            if  i < 0.48*first:
                if k>0.0003:
                    u = i
                    k=round(k-0.0001, 4)
            else:
                if k<0.002 and i >= first - u-80:
                    k=round(k+0.0001, 4)
    if m == 4:
        time.sleep(0.1)
        GPIO.output(dir, True)
        i = int(0)
        if l==1:
            GPIO.output(22, 1)
            GPIO.output(12, 0)
        else:
            GPIO.output(22, 0)
            GPIO.output(12, 1)
        time.sleep(0.5)
        while i < first:
            GPIO.output(step, True)
            time.sleep(0.0002)
            GPIO.output(step, False)
            time.sleep(0.0002)
            i = i + 1
    


