# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 14
"""

import re

#read in data file, strip new line characters out
Lines = [line.rstrip() for line in open('Day14.txt')]

#set up dict for binary data

bits=range(0,36)

bits_dict = {}
for bit in bits: 
    bits_dict[bit]=2**bit

#initialize dict to store mem values
mem_dict={}

#initial mask (none)
mask='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

#function for mask replacement
def char_replace(string, position, new_char):
    return(string[:position] + new_char + string[position+1:])

#split input data
for line in Lines:
    linesplit=line.split(' = ')
    action=linesplit[0]
    value=linesplit[1]
    
    if action=='mask': #overwrite current mask
        mask=value
        
    elif action.startswith('mem'):
        action = [int(action) for action in re.findall(r'-?\d+\.?\d*', action)][0]
        value=bin(int(value))[2:].zfill(36) #convert to binary, remove the 0b indicator from string
        
        #apply mask
        for i in range(0,36):
            if mask[i]!='X':
                value=char_replace(value, i, mask[i])
        #write to memory
        mem_dict[action]=value
            
    
    #print(action, value)
    
mem_vals = list(mem_dict.values())

mem_int=[]
for mem in mem_vals:
    mem_int.append(int(mem,2))
    
print(sum(mem_int))


print('part2')
#part 2



#initial mask (none)
mask='000000000000000000000000000000000000'
mem_dict2={}

#split input data
for line in Lines:
    linesplit=line.split(' = ')
    action=linesplit[0]
    value=linesplit[1]
    
    if action=='mask': #overwrite current mask
        mask=value
        
    elif action.startswith('mem'):
        action = [int(action) for action in re.findall(r'-?\d+\.?\d*', action)][0]
        
        # print(action)
        
        address=bin(int(action))[2:].zfill(36) #convert to binary, remove the 0b indicator from string
        
        # print('start', address)
        
        value=bin(int(value))[2:].zfill(36) #convert to binary, remove the 0b indicator from string
        
        #apply mask
        for i in range(0,36):
            if mask[i]!='0':
                address=char_replace(address, i, mask[i])
        # print('masked', address)
                
        #create all possible addresses
        address_list=[address]
        for add in address_list:
            xfound=False
            j=0
            while xfound==False and j<=35:
                    if add[j]=='X':
                        add_subA=char_replace(add, j, '0')
                        add_subB=char_replace(add, j, '1')
                        # print('xfoundA', add_subA)
                        # print('xfoundB', add_subB)
                        address_list.append(add_subA)
                        address_list.append(add_subB)
                        xfound=True
                    j+=1

                        
                        
        address_clean= [address_clean for address_clean in address_list if not 'X' in address_clean]  #get only addresses without X
        
        for a in address_clean:
            mem_dict2[int(a,2)]=value #write to memory
    

mem2_vals = list(mem_dict2.values())

mem2_int=[]
for mem in mem2_vals:
    mem2_int.append(int(mem,2))
    
print(sum(mem2_int))




