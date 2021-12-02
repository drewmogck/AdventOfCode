# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 25
"""

#import data        
Lines = [int(line.rstrip()) for line in open('Day25.txt')]

cardkey=Lines[0]
doorkey=Lines[1]

# cardkey=5764801
# doorkey=17807724

def transform(sub_num, val):
    val=val*sub_num
    val=val%20201227
    return val

#determine loop size
val = transform(7, 1)
i=1
while val!=cardkey:
    val = transform(7, val)
    #print(val)
    i+=1

card_loopsize=i    
print(card_loopsize)

val = transform(7, 1)
i=1
while val!=doorkey:
    val = transform(7, val)
    #print(val)
    i+=1

door_loopsize=i
print(door_loopsize)

def encryption_key(loopsize, key):
    val = transform(key, 1)
    for i in range(loopsize-1):
        val=transform(key, val)
    return val

print(encryption_key(card_loopsize, doorkey)) #part 1 answer