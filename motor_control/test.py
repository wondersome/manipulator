from degrees import degrees
from height import height
from motors import motor
import RPi.GPIO as GPIO
import time
"""GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, 1)
GPIO.output(22, 0)
GPIO.output(12, 1)
GPIO.setup(27, GPIO.IN)
while GPIO.input(27)==1 :
    time.sleep(0.1)
GPIO.output(16,0)
motor(1,720,0)
motor(3,29,0)
motor(1,degrees(90,0,0,7)[0],0)
motor(2,degrees(90,0,0,7)[1],0)
motor(3,degrees(90,0,0,7)[2],0)
"""
while 1:
	n = int(input())
	m = int(input())
	motor(m, n, 0)
