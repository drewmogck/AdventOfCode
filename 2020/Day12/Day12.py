# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 12
"""

#read in data file, strip new line characters out
Lines = [line.rstrip() for line in open('D:/OneDrive - Halliburton/Reference/Advent of Code/2020/Day12/Day12.txt')]

#position and direction initialize    
loc = {'x':0, 'y':0, 'dir':90}

    
dirdict ={"E":90, "W":270, "S":180, "N":0}

#define function for moving forward
def move(count, direction): #direction =[x,y] unit direction (+-1)
    loc['x']=loc['x']+count*direction[0]
    loc['y']=loc['y']+count*direction[1]
    
def cardinal(heading): #function to change direction
    if heading==0:
        return[0,1]
    elif heading==90:
        return[1,0]
    elif heading==180:
        return[0,-1]
    elif heading==270:
        return[-1,0]
    
#function for getting direction    
def degree(deg):
    return(deg%360)

for line in Lines:
    ins=line[0:1]
    val=int(line[1:])
    
    if ins in ["N","E","S","W"]:
        move(val ,cardinal(dirdict[ins]))
    elif ins=="F":
        move(val ,cardinal(loc['dir']))
    elif ins=="L":
        loc['dir']= degree(loc['dir']-val)
    elif ins=="R":
        loc['dir']=degree(loc['dir']+val)
    
    
    # print(loc)
    
print(abs(loc['x'])+abs(loc['y'])) #part 1 answer

#PART 2

#position and direction initialize    
shiploc = {'x':0, 'y':0, 'dir':90}
waypointloc= {'x':10, 'y':1}
    
dirdict ={"E":90, "W":270, "S":180, "N":0}

#define function for moving forward
def moveship(count): #direction =[x,y] unit direction (+-1)
    shiploc['x']=shiploc['x']+count*waypointloc['x']
    shiploc['y']=shiploc['y']+count*waypointloc['y']
    
def movewaypoint(count, direction):
    waypointloc['x']=waypointloc['x']+count*direction[0]
    waypointloc['y']=waypointloc['y']+count*direction[1]
     
def rotate(deg):
    if deg==0:
        newx=waypointloc['x']
        newy=waypointloc['y']
        waypointloc['x']=newx
        waypointloc['y']=newy
    elif deg==90:
        newx=waypointloc['y']
        newy=-waypointloc['x']
        waypointloc['x']=newx
        waypointloc['y']=newy
    elif deg==180:
        newx=-waypointloc['x']
        newy=-waypointloc['y']
        waypointloc['x']=newx
        waypointloc['y']=newy
    elif deg==270:
        newx=-waypointloc['y']
        newy=waypointloc['x']
        waypointloc['x']=newx
        waypointloc['y']=newy
    
    
def cardinal(heading): #function to change direction
    if heading==0:
        return[0,1]
    elif heading==90:
        return[1,0]
    elif heading==180:
        return[0,-1]
    elif heading==270:
        return[-1,0]
    
#function for getting direction    
def degree(deg):
    return(deg%360)

for line in Lines:
    ins=line[0:1]
    val=int(line[1:])
    
    if ins in ["N","E","S","W"]:
        movewaypoint(val ,cardinal(dirdict[ins]))
    elif ins=="F":
        moveship(val)
    elif ins=="L":
        rotate(degree(-val))
    elif ins=="R":
        rotate(degree(val))
    
    # print('ship')
    # print(shiploc)
    # print('waypoint')
    # print(waypointloc)

print(abs(shiploc['x'])+abs(shiploc['y'])) #part 2 answer
    