"""
Advent of Code 2020

Day 18
"""
import re

Lines = [line.rstrip().replace(' ','') for line in open('Day18.txt')]


#define calculation
def calc(last, numeric, op):
    if op=='+':
        return last+numeric
    elif op=='*':
        return last*numeric


sumvals=0

for l in Lines:
    
    #dict to store values in
    position={}
    ind=0
    for char in l:
        position[ind]=char
        ind+=1
     
    #initialize
    lastval=0
    lastop='+'
    parcount = 0#count for open parentheses
    
    subval={} #store values for calculation with parentheses
    
    for i in range(0,len(position)):
        val = position[i]
        if re.match("[\d]$", val):
            lastval=calc(lastval, int(val),lastop)
        elif re.match("[+*]$", val):
            lastop=val
        elif re.match("[(]$", val):
            subval[parcount]=[lastval, lastop]
            lastval=0
            lastop='+'
            parcount+=1
            
        elif re.match("[)]$", val):
            lastval=calc(lastval, subval[parcount-1][0], subval[parcount-1][1])
            parcount-=1
    
    sumvals+=lastval
    #print(lastop, lastval, parcount)

print(sumvals)



