# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 23
"""

#starting='389125467' #test data
starting='624397158'

start_list=[]
for i in starting:
    start_list.append(int(i))
    
moves=100

working_list=start_list.copy()
working_cup_index=0 #starting cup
lowval= min(start_list)
highval=max(start_list)


for move in range(0, moves):
    #print('-- move ', move+1, ' --')
    working_cup=working_list[working_cup_index]
    #print('cups:', working_list, working_cup)
    #remove next three cups
    next3=working_list.copy()[working_cup_index+1:working_cup_index+4]
    if len(next3)!=3:
        for c in working_list.copy()[:3-len(next3)]:
            next3.append(c)
    
    #print('pick up:', next3)
    
    working_list = [e for e in working_list if e not in next3]
    
    if working_cup>lowval:
        dest_cup_lab= working_cup-1
    elif working_cup==lowval:
        dest_cup_lab=highval
    
    dest_cup_index=''
    found=False
    
    while found==False:
        try:
            dest_cup_index = working_list.index(dest_cup_lab)
            found=True
        except ValueError: #item has been removed
            found=False
            if dest_cup_lab>lowval:
                dest_cup_lab-=1
            elif dest_cup_lab==lowval:
                dest_cup_lab=highval
        
    #print('destination=', dest_cup_lab)
    
    #insert removed cups after destination:
    next3.reverse() #reversing so i can insert at same index every time...
    for cup in next3: 
        working_list.insert(dest_cup_index+1, cup)
           
    
    working_cup_index=working_list.index(working_cup)+1
    
    if working_cup_index==len(start_list):
        working_cup_index=0 #loop back around
    #print('workingindex', working_cup_index)
    
    #input('wait...')
    
#sort items for answer:
pos = working_list.index(1)+1

strlist_out=[]
for x in range(0, len(start_list)-1):
    strlist_out.append(str(working_list[pos]))
    pos+=1
    if pos==len(start_list):
        pos=0

print('Part 1 answer:', ''.join(strlist_out))