# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 21
"""

#import data        
Lines = [line.rstrip() for line in open('Day21.txt')]

allergens={}

def flatten(listoflists):
    return [item for sublist in listoflists for item in sublist]

masteringreds=[]
allergens_list=[]

for line in Lines:
    out=line.replace(')','').split(' (contains ')
    ingreds=out[0].split()
    allers=out[1].split(', ')
    masteringreds+=ingreds
    for a in allers:
        if a not in allergens_list:
            allergens_list.append(a)
        if a in allergens:
            allergens[a].append(ingreds)
        else:
            allergens[a]=[ingreds]

food_key = {}
for f in allergens:
    flat_food=flatten(allergens[f])
    for food in flat_food:
        if flat_food.count(food)==len(allergens[f]):
            if f in food_key:
                if food not in food_key[f]:
                    food_key[f]+=[food]
            else:
                food_key[f]=[food]    
                
#get list of all possible foodkeys
allkeys = flatten(list(food_key.values()))

part1=[]
for k in masteringreds:
    if k not in allkeys:
        part1.append(k)
        
print(len(part1)) #part 1 answer

#part 2: #reuse some code from day 16

output={}
for f in allergens_list:
    output[f]=[]

while len(food_key)>0:
    matchfound=False
    for d in food_key.copy():
        if matchfound==False:
            length_key=len(food_key[d])
            #print(length_key, d)
            if length_key==1:
                output[d]=food_key[d]
                #print(food_key[d]) 
                rem=food_key[d][0]
                del food_key[d]
                matchfound=True
                for key in food_key:
                    #print(key, rem)
                    if len(food_key[key])>0:
                        try:
                            food_key[key].remove(rem)
                        except ValueError as e:
                            #print(e)
                            pass

part2=[]
for item in sorted(output):
    part2+=output[item]
    
finalp2=''
for v in part2:
    if v != part2[-1]:
        finalp2+=v+','
    else:
        finalp2+=v
print(finalp2) #part 2 answer
    
