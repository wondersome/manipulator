import math
import RPi.GPIO as GPIO
import time


def motor(m, n):

    if m == 1:
        dir = 19
        step = 21
        coef = 1.2
    elif m == 2:
        dir = 20
        step = 26
        coef = 1.8
    elif m == 4:
        dir = 12
        step = 16
        coef = 0.9
    elif m == 3:
        dir = 6
        step = 13
        coef = 0.9

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dir, GPIO.OUT)
    GPIO.setup(step, GPIO.OUT)
    if n < 0:
        GPIO.output(dir, False)
    else:
        GPIO.output(dir, True)
    i = int(0)
    first = int(n/coef)
    while i < first:
        GPIO.output(step, True)
        time.sleep(0.01)
        GPIO.output(step, False)
        time.sleep(0.01)
        i = i + 1

    if m == 4:
        GPIO.output(dir, False)
        i = int(0)
        while i < first:
            GPIO.output(step, True)
            time.sleep(0.01)
            GPIO.output(step, False)
            time.sleep(0.01)
            i = i + 1
    GPIO.cleanup()


# 4 мотор - высота