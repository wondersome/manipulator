from motor_control.degrees import degrees
from pprint import pprint
from motor_control.height import height
from camera import scheme, blocks35, blocks13
from rec import recognize
from algo_func import algo
import time
import collections
import RPi.GPIO as GPIO
from algorithm import algorithm
from motor_control.motors import motor
scheme()

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
GPIO.output(16,0)

motor(1,140,0)
blocks35()

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
file.write('200'+'\n')
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
