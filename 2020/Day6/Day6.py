# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 6
"""
#Part 1

#read in data file
file = open('Day6.txt', 'r') 
Lines = file.readlines() 


form_master=[] #list to store results of declaration forms
form_list='' #initialize blank string for form results

#loop through each groups and create string containing all form answers
for line in Lines:
    if line!='\n':
        form_list = form_list +line.rstrip('\n')
    else:
        form_master.append(form_list)
        form_list=''
        
form_master.append(form_list) #handles last line

sum_list = [] #stores sum of each group

for group in form_master:
    char_track=[] #tracks which values have been read
    for char in group:
        if char not in char_track:
            char_track.append(char)
    sum_list.append(len(char_track)) #store length of unique characters to list
    
print(sum(sum_list)) #sum values in list and print as answer to part 1

#Part 2

form_master=[] #master list of lists for forms
form_list=''

groupsize=0
sumcount=0
sumcount_master=[]

for line in Lines:
    if line!='\n':
        form_list = form_list +line.rstrip('\n')
        groupsize+=1 #counter for group members
    else:
        form_master.append(form_list)
        char_track=[]
        
        for char in form_list:
            if char not in char_track:
                char_track.append(char)
                occurance=form_list.count(char)
                if occurance/groupsize==1:
                    sumcount+=1
        
        sumcount_master.append(sumcount)
        
        #reset values for next group
        form_list=''
        groupsize=0
        sumcount=0

#handles last line of file
sumcount=0
char_track=[]
for char in form_list:
            if char not in char_track:
                char_track.append(char)
                occurance=form_list.count(char)
                if occurance/groupsize==1:
                    sumcount+=1
sumcount_master.append(sumcount)
        
print(sum(sumcount_master))


