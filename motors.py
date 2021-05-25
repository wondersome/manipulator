import math 

def motor(m):
    if m > 0:
        GPIO.output(24, True)
    else:
        GPIO.output(24, False)
        m = fabs(m)
i=int(0)
first=int(m/1.2)
while(i<first):
    GPIO.output(23, True)
    time.sleep(0.01)
    GPIO.output(23, False)
    time.sleep(0.01)
    i=i+1
GPIO.cleanup()