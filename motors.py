import math
import RPi.GPIO as GPIO
import time


def motor(m, n, l):
    u=int(0)
    k = 0
    if m == 1:
        dir = 23
        step = 24
        coef = 1.2
        k = 0.0012        
    elif m == 2:
        dir = 20
        step = 21
        coef = 1.8
        k = 0.0005
    elif m == 4:
        dir = 5
        step = 6
        coef = 0.9
        n = -n
        k = 0.00012
    elif m == 3:
        dir = 18
        step = 17
        coef = 0.9
        k = 0.00012
        n = -n
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dir, GPIO.OUT)
    GPIO.setup(step, GPIO.OUT)
    if int(n) < 0:
        u=1
        GPIO.output(dir, False)
        n = math.fabs(n)
    else:
        GPIO.output(dir, True)
    i = int(0)
    first =round( int(n*16/coef),0)
    while i < first:
        GPIO.output(step, True)
        time.sleep(k)
        GPIO.output(step, False)
        time.sleep(k)
        i = i + 1
    if m == 4:
        if l==0:
            print("отпускаем")
        else:
            print("берём")
        time.sleep(0.5)
        GPIO.output(dir, True)
        i = int(0)
        while i < first:
            GPIO.output(step, True)
            time.sleep(k)
            GPIO.output(step, False)
            time.sleep(k)
            i = i + 1
    GPIO.cleanup()
    time.sleep(0.5)
    if m!=4 and m!=3:
        if u==1 :
            return(first*coef/16*-1)
        else:
            return(first*coef/16)
    else:
        if m!=4:
            if u==1:
                return(first*coef/16)
            else:
                return(first*coef/16*(-1))

