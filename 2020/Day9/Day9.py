# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 9
"""
#PART 1

#define length of preamble
preamble_length=25

#read in data file, strip new line characters out
Lines = [int(line.rstrip()) for line in open('Day9.txt')]


sum_exists=0

def two_sum(pre, value):
    global sum_exists
    #two sum
    for i in pre:
        for j in pre:
            if i+j==value and i!=j:
                sum_exists=1

index=0 #starting index

for line in Lines:
    sum_exists=0
    
    preamble=Lines[index:index+preamble_length] #define preamble list

    remainder=Lines[index+preamble_length:] #list containing all following the preamble (which will move)
    
    
    two_sum(preamble, remainder[0])
    
    if sum_exists==0:
        print('No Sum Found: '+str(remainder[0])) #answer to Part 1
        break
    
    index+=1
    
invalid= remainder[0]

#PART 2

index=0
minmax=[]

for line in Lines:
    addlist=[]
    for i in Lines[index+1:]:
        addlist.append(i)
        if sum(addlist)==invalid and len(addlist)>1:
            print("List found!")
            print(addlist)
            minmax=[min(addlist), max(addlist)]
    index+=1
    
print(sum(minmax)) #answer to part 2
            
        