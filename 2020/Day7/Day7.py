# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 7
"""

#Part 1

#read in data file
# file = open('Day7_test.txt', 'r') 
file = open('Day7.txt', 'r') 
Lines = file.readlines() 

d = {} #dictionary for storing bags in each bag type

for line in Lines:
    s = line.rstrip()
    s = s.replace('bags','')
    s = s.replace('bag','')
    s = s.replace('.', '')
    s = s.replace('no other', '0')
    s_split=s.split('contain')
    bag_type = s_split[0].strip()
    bag_contents = s_split[1].strip()
    bag_contents_split = bag_contents.split(',')
    
    all_contents=[]
    
    for bag in bag_contents_split:
        sub_bag_count = int("".join(filter(str.isdigit, bag)))
        sub_bag_type= ''.join([i for i in bag if not i.isdigit()]).strip() 
        # print(sub_bag_count)
        # print([sub_bag_type]*sub_bag_count)
        net_contents=[sub_bag_type]*sub_bag_count
        all_contents.append(net_contents)
        
    flat_list = [item for sublist in all_contents for item in sublist]#flattens list from nested structure
    
    #print(flat_list)
    
    #store results to dictionary
    d[bag_type]=flat_list
    
 
    #loop through keys and see which ones eventually contain at least 1 shiny gold bag
master_list =[]
bagsum_list = []
    
for key, value in d.items():
    print(key, value)
    #calculate number of bags
    bagcountsum = len(value)
    # print(bagcountsum)
    vtot=value.copy()#CAREFUL - without copy modifies list in place
    vsub=value.copy()
    while len(vsub)>0:
        vsub_i=[]
        for v in vsub:
            expand = d[v] #add value from dictionary
            bagcountsum+=len(expand)
            print(bagcountsum)
            for j in expand:
                if j not in vtot:
                    vtot.append(j)#append to master total if not already in there
                if j not in vsub_i:
                    vsub_i.append(j)#if not already in there
            
        vsub=vsub_i.copy()

    master_list.append(vtot)
    bagsum_list.append(bagcountsum)        

count=0
for bag in master_list:
    if 'shiny gold' in bag: 
        print('TRUE')
        count+=1
    else:
        print('FALSE')
        
print(count)
#print(bagsum_list[384])


#part2

def getDict(bagtype):
    start=d[bagtype]
    output=[]
    for x in start:
        output.append(x)
    return(output)

initial='shiny gold'

master_list =[]
bagsum_list = []
 
vsub=[]
vsub=getDict(initial)
bagcountsum = len(vsub)
while len(vsub)>0:
    vsub_i=[]
    for v in vsub:
        expand = d[v] #add value from dictionary
        bagcountsum+=len(expand)
        print(bagcountsum)
        for j in expand:
            print(j)
            #if j not in vtot:
            vtot.append(j)#append to master total if not already in there
            #if j not in vsub_i:
            vsub_i.append(j)#if not already in there
        
    vsub=vsub_i.copy()

    master_list.append(vtot)
    bagsum_list.append(bagcountsum)  


    
