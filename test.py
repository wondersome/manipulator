from height import height
from degrees import degrees
from motors import motor
import time
n=int(input())
while 1:
    p=motor(4,n, 0)
    time.sleep(1)
    p=motor(4,n,0)
    time.sleep(1)
"""
motor(1,-3.9734)
motor(2,71.2861)
motor(3,-37.3127)
"""
