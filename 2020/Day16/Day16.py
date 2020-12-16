# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 16
"""

#loop through file, read in rules, then your ticket number, then nearby tickets
#map rules  to dict with list eg. rules[class:[1-3], [5-7]]
#but expand them so that it is like [1,2,3, 5,6,7]

Lines = [line.rstrip() for line in open('Day16.txt')]

#parse file
infotype=['rule', 'myticket', 'otherticket']
infocount=0

tickets=[]
rules={}

for line in Lines:
    if line=='':
        infocount+=1
        infotrack_type=infotrack_type=infotype[infocount]#determines which type of data we are dealing with
        
    infotrack_type=infotype[infocount]
    
    if line not in ['', 'your ticket:', 'nearby tickets:']:
        if infotrack_type=='rule':
            rulesplit=line.split(': ')
            ruletype=rulesplit[0]
            rulevalues=rulesplit[1]
            rulevalues=rulevalues.split(' or ')
            rulerange=[]
            for r in rulevalues:
                min=int(r.split('-')[0])
                max=int(r.split('-')[1])+1
                rulerange.append(list(range(min, max)))
            
                      
            concat_rng = rulerange[0]+rulerange[1]

            rules[ruletype]=concat_rng
            
        elif infotrack_type=='myticket':
            myticket=line.split(',')
        elif infotrack_type=='otherticket':
            tickets.append(line.split(','))
        

#loop through tickets looking for invalid and sum
            
sum_invalid=0         
valid=[]   
for t in tickets:
    ticket_valid=True
    for f in t:
        found=False
        for rul in rules:
            if int(f) in rules[rul]:
                found=True
                #print('found')
        
        if found==False:
            sum_invalid+=int(f)
            ticket_valid=False
            #print(f)
    if ticket_valid==True:
        valid.append(t)
            
print(sum_invalid) #answer to part 1

#part 2 - 
#valid tickets stored in valid above

#create dict to store field values in
field_vals={}
for f in range(0, len(myticket)):
    field_vals[f]=[]

for vtic in valid:
    fieldno=0
    for field in vtic:
        field_vals[fieldno].append(int(field))
        fieldno+=1
        
#dict to store possible matches
matches={}
for f in range(0, len(myticket)):
    matches[f]=[]

#check which fields match which rules
for rul in rules:
    #print(rul)
    for fld in field_vals:
        #print(rules[rul], field_vals[fld])
        if all(item in rules[rul] for item in field_vals[fld]):
            #print(fld, rul)
            matches[fld].append(rul)

#dict to store answer
output={}
for f in range(0, len(myticket)):
    output[f]=[]

while len(matches)>0:
    matchfound=False
    for d in matches.copy():
        if matchfound==False:
            length_key=len(matches[d])
            #print(length_key, d)
            if length_key==1:
                output[d]=matches[d]
                #print(matches[d]) 
                rem=matches[d][0]
                del matches[d]
                matchfound=True
                for key in matches:
                    #print(key, rem)
                    if len(matches[key])>0:
                        try:
                            matches[key].remove(rem)
                        except ValueError as e:
                            print(e)
                            pass

                
#define dictionary for my ticket
mytick_dict = {}

i=0
for f in myticket:
    mytick_dict[output[i][0]]=f
    i+=1
    
#find fields that start with depature and add together
productdepart=0
for j in mytick_dict:
    if 'departure' in j:
        if productdepart==0:
            productdepart+=int(mytick_dict[j])
        else:
            productdepart*=int(mytick_dict[j])
        
print(productdepart) #answer to part 2
