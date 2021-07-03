import datetime
from motor_control.degrees import degrees
from pprint import pprint
from motor_control.height import height
from camera import block, scheme, blocks35, blocks13
from rec import recognize
from algo_func import algo
import time
import collections
import RPi.GPIO as GPIO
from algorithm import algorithm
from motor_control.motors import motor
from num import abcs





GPIO.setwarnings(False)
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
scheme()
GPIO.output(16,0)
a=abcs(140, 1)
motor(1,140,0)
blocks35()
a += abcs(60, 1)
motor(1,60,0)
blocks13()

scheme = recognize()[0]
pprint(scheme)
blocks = recognize()[1]
pprint(blocks)

db = []
made = [[], [], []]
dic = {}
file = open("shance.txt","w")
file.write(str(a)+'\n')
file.write('121'+'\n')
file.write('-31')
file = open("sum.txt","w")
file.write(str(a)+'\n')
file.write('0'+'\n')
file.write('0')
file.close()
a = algorithm(0)
b = algorithm(1)
c = algorithm(2)

dic[round(a)] = 0
dic[round(b)] = 1
dic[round(c)] = 2
dic = collections.OrderedDict(sorted(dic.items()))
dic = dict(collections.OrderedDict(sorted(dic.items())))
for key in dic:
    print(dic[key])
    algo(scheme, blocks, db, made, dic[key])


pprint(db)


with open('sum.txt') as file:
    content= file.readlines()
content = [x.strip() for x in content]
d=float(content[0])
s=float(content[1])
t=float(content[2])
file.close()
motor(1,-d, 0)
motor(3, -t, 0)
motor(2, -s, 0)
GPIO.setup(26, GPIO.OUT)

t_end = time.time() + 4
while time.time() < t_end:
    GPIO.output(26, 1)
    time.sleep(0.001)
    GPIO.output(26, 0)
    time.sleep(0.001)
