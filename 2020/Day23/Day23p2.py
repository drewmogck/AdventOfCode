# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 23
"""

#inspiration from https://pastebin.com/RFqCydrB

#starting='389125467' #test data
starting='624397158'

cups=[]
for i in starting:
    cups.append(int(i))
    
moves=10000000

lowval= min(cups)
highval=max(cups)

cups = cups+list(range(highval+1,1000001))
highval=max(cups)

d={}

for i in range(0, len(cups)):
    if i==0:
        d[-1]= cups[0] #set first cup
    else:
        d[cups[i-1]] = cups[i] #each cup points to next cup

d[cups[i]]=cups[0] #last cup points to first cup



working_cup_lab=-1 #starting cup
    
for move in range(moves):
    if (move+1)%1000000==0:
        print('-- move ', move+1, ' --')
        
        
    working_cup= d[working_cup_lab]    #first=d[start]
        
    #remove next three cups
    next3a = d[working_cup] #x
    next3b = d[next3a] #y
    next3c = d[next3b] #z
    
    # print(next3a, next3b, next3c)
    
    next_cup = d[next3c] #pointer to next cup after removing next 3 #firstnext
    
    dest_cup_lab= working_cup-1
      
    dest_cup_index=''
    found=False
    
    while found==False:
        if dest_cup_lab<lowval:
            dest_cup_lab=highval
        if dest_cup_lab not in [next3a, next3b, next3c]: 
            current_pointer = d[dest_cup_lab] #store value currently in dest
            d[dest_cup_lab] = next3a #insert the next cups into place
            d[next3c] = current_pointer #replace pointer to exisiting value
            found = True
        else:
            found = False
            dest_cup_lab -= 1
                
    d[working_cup]=next_cup #point working cup to next cup
    working_cup_lab=working_cup
    
    #print(working_cup, next3a,next3b,next3c, next_cup, dest_cup_lab)
    


                
after1a=d[1]
after1b=d[after1a]

print('Part 2 answer:', after1a*after1b)
    
    
