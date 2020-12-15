# -*- coding: utf-8 -*-
"""
Advent of Code 2020

Day 15
"""
#part 1
data_in=[9,12,1,4,17,0,18]

datalength=len(data_in)

last=data_in[-1]

countstart=[]
for i in range(0,len(data_in)):
    countstart.append(i+1)

mem=dict(zip(data_in, countstart))

global_count=datalength+1 #total number of turns counter (start at 4 on example)

while global_count<=2020:

    if last in mem:    
        out=global_count-1-mem[last]
    else: 
        out=0

    # print(global_count, last, out)

    mem[last]=global_count-1
    
    last=out
    

    global_count+=1

print(out)

#part 2 below



data_in=[9,12,1,4,17,0,18]

datalength=len(data_in)

last=data_in[-1]

countstart=[]
for i in range(0,len(data_in)):
    countstart.append(i+1)

mem=dict(zip(data_in, countstart))

global_count=datalength+1 #total number of turns counter (start at 4 on example)

while global_count<=30000000:

    if last in mem:    
        out=global_count-1-mem[last]
    else: 
        out=0

    # print(global_count, last, out)

    mem[last]=global_count-1
    
    last=out
    

    global_count+=1

print(out)
    

        

        
    
    
    


