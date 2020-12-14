# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 13
"""

import numpy as np
import math

#read in data file, strip new line characters out
Lines = [line.rstrip() for line in open('Day13.txt')]

timestamp=int(Lines[0])

busids=Lines[1]

#get just active busids
bus_active=[]
bus_offset=[]

for bus in busids.split(','):
    if bus=='x':
        next
    else:
        bus_active.append(int(bus))
        offset=busids.split(',').index(bus)
        bus_offset.append(offset)
        

bus_dict={}
for bus in bus_active:
    bus_dict[bus]=bus-timestamp%bus

#minimum wait time
time=min(bus_dict.values())
#bus with that time
bus_no = [key for key in bus_dict if bus_dict[key] == time]

print(bus_no[0]*time) #answer to part 1

print('PART 2')

#part 2

#initialize starting values
brute_force=False

if brute_force==True:
    np_bus_active=np.array(bus_active)
    np_bus_offset=np.array(bus_offset)
    
    timestamps=np_bus_active.copy()+np_bus_offset
    
    i=1
    while sum(timestamps%bus_active)!=0:
        timestamps = np_bus_active[0]*i+np_bus_offset
        i+=1
        print(i)
        
    print(timestamps[0])

#above is brute force and doesnt' work for actual data
    
    
    
#part 2 attempt 2 - with inspiration from https://topaz.github.io/paste/#XQAAAQDrAQAAAAAAAAARiAinOloyihUu1b5x+73YwmpOl2G0L3PuEQPXiO3gBNVXod4NnFOiocbPfqFlOUDj4C0xggeOKoR+Ro2i/QPgQ4oYPEYS8R3Gp6juP9HdOeGPbDvXpOZ1TWtDap9oMclY77nr4lwBeSphR9kI77Ct9tD1Jmy5lnQOFGrB6/Pw4naHHFnaZFFUi5/9kZXhHOjRsBdgQyyBQmyB0tKWMVyNWi6/eWGHM4uSa6aNkMawOhVndGwPO5xyellliw/Em+pGCbvxdrstXyVZWIsGKXfErUWMI/LsLQlreQSKpJLqlIzYfkeOJZyV0jwk5YKQlD3gTmZgF6KtywICGK+xRsoMnDncZlBRFssldPWS7kikdkQd1EbaOsBINL/950LX8LS70SUg9n4Y/UaVCq1eGMrdYNe+AoGSNZ3eZ31RkeyowsTw//DhjKA=


offset_dict =  dict(zip(bus_active, bus_offset))

step=bus_active[0]
start=0

for bus in bus_active[1:]:
    #print('next bus')
    offset=offset_dict[bus]
    for i in range(start, step*bus, step):
        #print(i)
        if (i+offset)%bus==0:
            step = step*bus
            start=i
            
print(start)
    
















