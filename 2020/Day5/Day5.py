# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 5
"""

import pandas as pd

file = open('Day5.txt', 'r') 
Lines = file.readlines() 


###PART 1 ###
#initialize starting ranges
rowsmin=0
rowsmax=127 #keep in mind they need to be indexed to 0

colsmin=0
colsmax=7 #keep in mind they need to be indexed to 0


def iter(code, min_, max_):
    if code=='F' or code=='L':
        min=min_
        max=((max_-1)+(min_))/2
    elif code=='B' or code=='R':
        max=max_
        min=((max_+1)+(min_))/2
    return([min, max])



output=[]

for line in Lines:
    out=[]
    row_code=line[:7]
    for rc in row_code:
        rowscalc = iter(rc, rowsmin, rowsmax)
        rowsmin=rowscalc[0]
        rowsmax=rowscalc[1]
    
           
    col_code=line[7:].rstrip()
    for cc in col_code:
        colscalc = iter(cc, colsmin, colsmax)
        colsmin=colscalc[0]
        colsmax=colscalc[1]

    row=rowsmin
    col=colsmin
    seatID=row*8+col
    
    out=[row, col, seatID]
    print(out)
    
    output.append(out)
     
    #reset values
    rowsmin=0
    rowsmax=127
    colsmin=0
    colsmax=7
        
        
df = pd.DataFrame(output, columns = ['row', 'column', 'seatID'])  

print(df["seatID"].max())

###PART 2###

df = df.sort_values(by=["seatID"])

minid=int(df["seatID"].min())
seatrange=list(range(minid, minid+len(df)))

df['seatrange']=seatrange

df['seatchecker'] = df['seatrange']-df['seatID'] # find first row where  seatchecker is negative

