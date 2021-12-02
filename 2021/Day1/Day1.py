# -*- coding: utf-8 -*-
"""
Advent of Code 2021
Day 1
"""
#PART 1#

#import raw datas
Lines = [int(line.rstrip()) for line in open('Day1.txt')]

def count_increase(input_list):
    lastval=input_list[0]
    counter = 0 #count of number that increase

    for l in input_list[1:]: #skip first row since there is no previous value
        #test if value is larger than previous
        if l>lastval:
            counter+=1

        lastval=l #store last item for next round

    return(counter)

#answer to part 1
print(count_increase(Lines))

#PART 2#

# Store sectional subset sum in list 
sec_sum = [sum(Lines[x : x + 3]) for x in range(0, len(Lines)-2, 1)]

#answer to part 2
print(count_increase(sec_sum))
