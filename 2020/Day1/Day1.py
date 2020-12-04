# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 1
"""
file = open('Day1.txt', 'r') 
Lines = file.readlines() 
Lines = [int(i) for i in Lines] #convert text list to integer list

# Part 1
def two_sum(data):
    #two sum
    for i in data:
        for j in data:
            if i+j==2020:
                return(i*j)

print('Part1: '+str(two_sum(Lines)))

# Part 2
                
def three_sum(data):
    #three sum
    for i in data:
        for j in data:
            for k in data:
                if i+j+k==2020:
                    return(i*j*k)

print('Part2: '+str(three_sum(Lines)))
