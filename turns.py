import math
n = int(input())
first = int(n / 1.2)
second = int((n - first*1.2) / 0.6)
third = int((n -first*1.2 - second*0.6) / 0.3)
forth = int((n -first*1.2 - second*0.6 - third*0.3) / 0.15)
fifth = int((n -first*1.2 - second*0.6 - third*0.3 - forth*0.15) / 0.075)
sixth = int((n -first*1.2 - second*0.6 - third*0.3 - forth*0.15 - fifth * 0.075) / 0.0375)
print(first)
print(second)
print(third)
print(forth)
print(fifth)
print(sixth)



