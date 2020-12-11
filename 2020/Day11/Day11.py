# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 11
"""

import numpy as np
import math

#read in data file, strip new line characters out
Lines = [line.rstrip() for line in open('Day11.txt')]

#function to convert character to number
def conv_char(char):
    if char=='L':
        return 0
    elif char=="#":
        return 1
    elif char=='.':
        return np.nan

#function to count occupied seats for each seat
     
def seat_count(x, row,col):
    try:
        TL = x[row-1,col-1]
    except IndexError:
        TL = 0
        pass
    try:
        TM = x[row-1,col]
    except IndexError:
        TM = 0
        pass
    
    try:
        TR = x[row-1,col+1]
    except IndexError:
        TR = 0
        pass
    
    try:
        ML = x[row,col-1]
    except IndexError:
        ML = 0
        pass
    
    try:
        MR = x[row,col+1]
    except IndexError:
        MR = 0
        pass
    
    try:
        BL = x[row+1,col-1]
    except IndexError:
        BL = 0
        pass
    
    try:
        BM = x[row+1,col]
    except IndexError:
        BM = 0
        pass
    
    try:
        BR = x[row+1,col+1]
    except IndexError:
        BR = 0
        pass
    
    if col==0:
        TL=0
        ML=0
        BL=0
    if row==0:
        TL=0
        TM=0
        TR=0
        
    
    #print(TL,TM,TR,ML,MR,BL,BM,BR)
    return(np.nansum([TL,TM,TR,ML,MR,BL,BM,BR]))

#function to check if seat is already filled or not
def occupancy(x,row,col):
    if  x[row,col]==1:
        return(1)
    else:
        return(0)



#set rules
def rules(x, row,col, maxocup):
    if math.isnan(x[row,col]):
        return(0)
    elif seat_count(x, row,col)==0 and occupancy(x, row,col)==0:
        return(1) #fill seat if not filled
    elif seat_count(x, row,col)>=maxocup and occupancy(x, row,col)==1:
        return(-1) #make empty if filled
    else:
        return(0) #no change in status


#convert data structure to a matrix
data=np.empty((len(Lines), len(Lines[0])))

r=0 #row counter
for line in Lines:
    c=0 #col counter
    for char in line:
        data[r][c]=conv_char(char)
        c+=1
    r+=1


#function to return change data frame:


def make_change(x, maxocup):
    global end
    #data to store change values in so it can be applied simultaneously
    change=np.empty((len(Lines), len(Lines[0])))
    
    r=0
    for row in x:
        c=0
        for col in row:
            change[r][c]=x[r][c]+rules(x, r,c,maxocup)
            c+=1
        r+=1
    if np.allclose(change ,x, equal_nan=True):
        print('DONE')
        end=True
    return(change)
    


end=False


while end==False:
    data=make_change(data, 4)


    
#part 1 answer
part1=np.nansum(data)    
    
print(part1)
        
#PART 2 - need to define new seat count

#convert data structure to a matrix
data=np.empty((len(Lines), len(Lines[0])))

r=0 #row counter
for line in Lines:
    c=0 #col counter
    for char in line:
        data[r][c]=conv_char(char)
        c+=1
    r+=1

def direction(x, row,col,rowdir,coldir): #rowdir, coldir =-1,0,or1 depending on direction
    rowdir_orig=rowdir
    coldir_orig=coldir
    if math.isnan(x[row+rowdir][col+coldir]): #iterate to find first non floor seat in given direction
        while math.isnan(x[row+rowdir][col+coldir]):
            rowdir=rowdir+rowdir_orig
            coldir=coldir+coldir_orig
            #print('change')
    if row==0 and rowdir_orig==-1:
        rowdir=rowdir_orig
    if col==0 and coldir_orig==-1:
        coldir=coldir_orig
    if row+rowdir<0 or col+coldir<0:
        return([999999,999999])# indicates its edge case row error
    else:
        return([rowdir, coldir])

def get_loc(x, row,col, rowdir, coldir):
    checkdir=direction(x, row, col, rowdir, coldir)
    if checkdir[0]==999999:
        return(0)
    else:
        return(x[row+direction(x, row,col, rowdir, coldir)[0],col+direction(x, row, col, rowdir, coldir)[1]])

#modified function to count occupied seats for each seat
def seat_count(x, row,col):
    try:
        TL = get_loc(x, row,col, -1, -1)
    except IndexError:
        TL = 0
        pass
    try:
        TM = get_loc(x, row,col, -1, 0)
    except IndexError:
        TM = 0
        pass
    
    try:
        TR = get_loc(x, row,col, -1, 1)
    except IndexError:
        TR = 0
        pass
    
    try:
        ML = get_loc(x, row,col, 0, -1)
    except IndexError:
        ML = 0
        pass
    
    try:
        MR = get_loc(x, row,col, 0, 1)
    except IndexError:
        MR = 0
        pass
    
    try:
        BL = get_loc(x, row,col, 1, -1)
    except IndexError:
        BL = 0
        pass
    
    try:
        BM = get_loc(x, row,col, 1, 0)
    except IndexError:
        BM = 0
        pass
    
    try:
        BR = get_loc(x, row,col, 1, 1)
    except IndexError:
        BR = 0
        pass
    
    if col==0:
        TL=0
        ML=0
        BL=0
    if row==0:
        TL=0
        TM=0
        TR=0
        
    
    #print(TL,TM,TR,ML,MR,BL,BM,BR)
    return(np.nansum([TL,TM,TR,ML,MR,BL,BM,BR]))


end=False

while end==False:
    data=make_change(data, 5)


    
#part 2 answer
part2= np.nansum(data)


print('DONE WITH BOTH PARTS!')
print(part2)

