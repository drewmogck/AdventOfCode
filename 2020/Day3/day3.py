# -*- coding: utf-8 -*-
"""
Advent of Code 2020

Day 3
"""

import pandas as pd
import numpy as np

##PART 1

# Using readlines() 
file = open('Day3.txt', 'r') 
Lines = file.readlines() 
  

# Strips the newline character
count=0 
for line in Lines: 
    Lines[count]=line.strip()*500
    print(Lines[count])
    count+=1
    
col=0
trees=0 #initialize number of trees
for line in Lines:
    if line[col]=='#':
        trees+=1
    col+=3

var_1_3= trees    
print(trees)

#part 2
#Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

# Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

# What do you get if you multiply together the number of trees encountered on each of the listed slopes?

col=0
trees=0 #initialize number of trees
for line in Lines:
    if line[col]=='#':
        trees+=1
    col+=1

var_1_1= trees  
print(trees)


col=0
trees=0 #initialize number of trees
for line in Lines:
    if line[col]=='#':
        trees+=1
    col+=5

var_1_5= trees  
print(trees)


col=0
trees=0 #initialize number of trees
for line in Lines:
    if line[col]=='#':
        trees+=1
    col+=7

var_1_7= trees  
print(trees)

col=0
row=0
trees=0 #initialize number of trees
for row in pd.Series(np.arange(0,len(Lines),2)):
    if Lines[row][col]=='#':
        trees+=1
    col+=1

var_2_1= trees  
print(trees)

print(var_1_1*var_1_3*var_1_5*var_1_7*var_2_1)