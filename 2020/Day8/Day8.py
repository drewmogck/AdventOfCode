# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 8
"""

#read in data file
file = open('Day8.txt', 'r') 
Lines = file.readlines() 





#define actions for each item
def acc(value):
    global accumulator
    accumulator+=value
    return(1)#define line jump upon completion - goto next line

def jmp(value):
    return(value) #skips above or below line depending on sign

def nop(value):
    return(1) #goto next line upon completion

def track(index, part): #logs execution of each line
    global firstround
    global secondround
    if index not in tracker:
        tracker.append(index)
    else:
        if part==1:
            print('Round Complete')
            print(accumulator)
            firstround=1
        else:
            secondround=1



#PART 1
        
#initialize accumulator
accumulator=0
line_no=0


#start loop:
    
tracker=[] #initialize tracker for when line is repeated to stop program
firstround=0

while firstround==0:
    line=Lines[line_no]
    track(line_no, 1)
    
    
    instruction= line.split(' ')[0]
    value= int(line.split(' ')[1])
    
    if instruction=='acc':
        line_no+=acc(value)
    elif instruction=='jmp':
        line_no+=jmp(value)
    elif instruction=='nop':
        line_no+=nop(value)
    else:
        print('Error in parsing')
        firstround=1
    
    
#PART 2
    
counter=0

for l in Lines:
    #initialize accumulator
    accumulator=0
    line_no=0

    tracker=[]
    secondround=0
    if l.split(' ')[0]=='jmp':
        test_line=counter
    elif l.split(' ')[0]=='nop':
        test_line=counter
    else:
        counter+=1
        continue #skip iteration since can't change this line
    
    try:
        while secondround==0:
            line=Lines[line_no]
            track(line_no, 2)
            
            
            instruction= line.split(' ')[0]
            value= int(line.split(' ')[1])
            
            if line_no!=test_line:
                if instruction=='acc':
                    line_no+=acc(value)
                elif instruction=='jmp':
                    line_no+=jmp(value)
                elif instruction=='nop':
                    line_no+=nop(value)
                else:
                    print('Error in parsing')
                    secondround=1
            elif line_no==test_line:
                if instruction=='jmp':
                    line_no+=nop(value)
                elif instruction=='nop':
                    line_no+=jmp(value)
                else:
                    print('Error in parsing')
                    secondround=1
    except IndexError:
        print(IndexError)
        print("Line: "+ str(line_no))
        print("Accumulator: "+ str(accumulator))
        break
    
    counter+=1


