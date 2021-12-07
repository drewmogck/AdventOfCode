"""
Advent of Code 2021
Day 7
"""
import numpy as np

#PART 1#

#import raw datas
Lines = [line.rstrip() for line in open('Day7.txt')]

data = np.asarray(list(map(int, Lines[0].split(sep=","))))

#initialize list to store results for part 1
costs=[]

for i in range(min(data), max(data)+1):
    costs.append(sum(abs(data-i)))

print("Part 1 answer is: " + str(min(costs)))

#part 2 - brute force, there is probably a more optimal way to do this

#list to store results for part 2:
costs =[]

for i in range(min(data), max(data)+1):
    distance = abs(data-i) #array with distances
    
    totcost_list=[]

    for d in distance:
        totcost=0
        cost=0
        for j in range(d):
            cost+=1
            totcost+=cost
        totcost_list.append(totcost)
    
    costs.append(sum(totcost_list))
    
print("Part 2 answer is: " + str(min(costs)))