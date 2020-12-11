# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 10
"""

import numpy as np
import pandas as pd


Lines = [int(line.rstrip()) for line in open('Day10.txt')]

#add charging adaptor and outlet +3 from max and 0 Jolts resepectively
adaptor=max(Lines)+3
outlet=0

Lines.append(adaptor)
Lines.append(outlet)

sortlist=Lines.copy()

sortlist.sort(reverse=True)

diff=[] #list to store diffs in
index=1
for s in sortlist[1:]:
    diff.append(s-sortlist[index-1])
    index+=1

#What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
print(diff.count(1)*(diff.count(3)))


#part 2

ones=[]
twos=[]
threes=[]

#function to test if value has a adaptor within x jolts of it
def within_x(input,x, output=[]):
    for item in input:
        #print('item='+ str(item))
        
        if item-x in input:
            output.append(1)
        else:
            output.append(0)
    return(output)

            
ones=within_x(sortlist,1, output=[])
twos=within_x(sortlist,2, output=[])
threes=within_x(sortlist,3, output=[])

# # creating an empty dictionary
dict = {}
# # updating `converted_dict` with keys for each element (i) in `result`
for i in sortlist:
  dict.update({i:0})
  
print(dict)
    
matrix=np.array([sortlist, ones,twos,threes]).transpose()

for i in range(0,len(sortlist)):
    val=1
    output=[]
    a=[]
    b=[]
    c=[]
    for j in matrix[i][1:]:
        datain=matrix[i][0]
        out = [datain-val]*j
        
        output=output+out
        
        dict[matrix[i][0]]=output
        
        val+=1 #iterates 1,2,3 for each column

inputs=[]
inputs.append(sortlist[0])

count=0
# for line in inputs:
#     output=[]
#     output=dict[line]
#     for o in output:
#         #print(o)
#         inputs.append(o)
#         if o==0:
#             count+=1

# print(count)

#my code worked for test files but main file was too long for this method. Finally needed some help... really impressed by the elegance of the solution below.

##solution below with help from: https://dev.to/qviper/advent-of-code-2020-python-solution-day-10-30kd

with open("Day10.txt", "r") as fp:
    lines = [int(line.rstrip()) for line in open('Day10.txt')]

lines.append(max(lines)+3)

sol = {0:1}
for line in sorted(lines):
    sol[line] = 0

    if line - 1 in sol:
        sol[line]+=sol[line-1]
    if line - 2 in sol:
        sol[line]+=sol[line-2]
    if line - 3 in sol:
         sol[line]+=sol[line-3]
    

print(sol[max(lines)])



    
    