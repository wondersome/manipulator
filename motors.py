import math
import RPi.GPIO as GPIO
import time


def motor(m, n):


    if m == 1:
        dir = 18
        step = 17
        coef = 0.65
    elif m == 2:
        dir = 20
        step = 21
        coef = 1.8
    elif m == 4:
        dir = 5
        step = 6
        coef = 0.9
        n = n * -1
    elif m == 3:
        dir = 18
        step = 17
        coef = 0.9
        n = -n
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dir, GPIO.OUT)
    GPIO.setup(step, GPIO.OUT)
    if n < 0:
        GPIO.output(dir, False)
        n = math.fabs(n)
    else:
        GPIO.output(dir, True)
    i = int(0)
    first = int(n/coef)
    while i < first:
        GPIO.output(step, True)
        time.sleep(0.02)
        GPIO.output(step, False)
        time.sleep(0.02)
        i = i + 1

    if m == 4:
        GPIO.output(dir, True)
        i = int(0)
        while i < first:
            GPIO.output(step, True)
            time.sleep(0.02)
            GPIO.output(step, False)
            time.sleep(0.02)
            i = i + 1
   


# 4 мотор - высота
