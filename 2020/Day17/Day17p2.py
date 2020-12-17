# -*- coding: utf-8 -*-
"""
Advent of Code 2020

Day 17
"""


Lines = [line.rstrip() for line in open('Day17.txt')]

space={} #dict to store values in cube space

#initial values
zi=0
wi=0
#row, column = x, y
#space[x,y,z]

xi=0 #row starts at 0
for line in Lines:
    yi=0
    for i in line:
        space[(xi,yi,zi, wi)]=[i, 0] #record location. 2nd part is change state place holder - will use this to flip on/off
        yi+=1
    xi+=1
    
#need to define counter function:

def count_surround(x,y,z,w):
    act_count=0
    for xa in [x-1, x, x+1]:
        for ya in [y-1, y, y+1]:
            for za in [z-1, z, z+1]:
                for wa in [w-1, w, w+1]:
                    if [xa,ya,za,wa] !=[x,y,z,w]:
                        try:
                            if space[(xa,ya,za,wa)][0]=='#':
                                act_count+=1
                        except KeyError: #key doesn't exist - inactive cube space
                            pass
    return(act_count)
    
#check if 2 or 3 neighbors are active and if not then deactivate
def active_switch(x,y,z,w):
    if count_surround(x,y,z,w) not in [2,3]:
        space[x,y,z,w]=['#', -1]
        #print(x,y,z)

#check all neighbors (including inactive) to see if any have 3 active neighbors and activate them
def check_surround(x,y,z,w):
    for xa in [x-1, x, x+1]:
        for ya in [y-1, y, y+1]:
            for za in [z-1, z, z+1]:
                for wa in [w-1, w, w+1]:
                    if [xa,ya,za,wa] !=[x,y,z,w]:
                        #check if recorded, if not, add to dict
                        try:
                            space[xa,ya,za,wa]
                        except KeyError:
                            space[xa,ya,za,wa]=['.',0] #add inactive
                            pass
                        
                     
                        if space[xa,ya,za,wa]==['.',0] and count_surround(xa,ya,za,wa)==3: #then make active
                            space[xa,ya,za,wa]=['.', 1]

#function to check if cell is active
def active(x,y,z,w):
    try:
        if space[(x,y,z,w)][0]=='#':
            return True
        elif space[x,y,z,w][0]=='.':
            return False
    except KeyError: #if key doesn't exist, it is also inactive, so return false
        return False
        pass

#loop through all cells in dict and activate or deactivate accordingly
def set_switch():
    #first set swtich values       
    for cell in list(space):
        if active(cell[0], cell[1], cell[2], cell[3]):
            active_switch(cell[0], cell[1], cell[2], cell[3])
        else:
            if count_surround(cell[0], cell[1], cell[2], cell[3])==3:
                space[cell[0],cell[1],cell[2], cell[3]]=['.', 1]
                
        check_surround(cell[0],cell[1],cell[2], cell[3])
    #next perform the switch
    for cell in space:
        if space[cell][1]==0: 
            pass
        elif space[cell][1]==1: #make active
            space[cell]=['#',0]
        elif space[cell][1]==-1: #make inactive
            space[cell]=['.',0]
        
        
for j in range(1,7):
    print(j)
    set_switch()
            
#get count of actives
count_act=0
for cell in space:
    if active(cell[0], cell[1], cell[2], cell[3]):
        count_act+=1

print(count_act) #part2 answer
