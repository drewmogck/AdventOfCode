# -*- coding: utf-8 -*-
"""
Advent of Code 2022
Day 1
"""
#PART 1#

#import raw datas
with open('Day1.txt') as f:
    lines = [line.rstrip() for line in f]

calories = {}

elf = 0
cal_val=0

for l in lines:
    
    if l!='':
        cal_val+=int(l)
    else: #next elf
        calories[elf]=cal_val
        cal_val=0 #reset calorie counter
        elf+=1

#Part 1 answer
print(max(calories.values()))

#Part 2
from operator import itemgetter

#initialize n
n=3

top_n = dict(sorted(calories.items(), key=itemgetter(1), reverse=True)[:n]) #itemgetter 1 says to sort by value, not key

print(str(top_n)) 

calsum = 0

for i in top_n:
    calsum+=top_n[i]

#part 2 answer
print(calsum)