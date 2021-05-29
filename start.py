import math
import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, True)
while GPIO.input(27)==False:
    pass
print("--")
time.sleep(1000)
"""while(GPIO.input(27) == False):
    time.sleep(1)
print("hgghh")
"""
