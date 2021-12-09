"""
Advent of Code 2021
Day 9
"""
#PART 1#

#import raw data
Lines = [line.rstrip() for line in open('Day9.txt')]

#define dict to store vals in
#x,y, up, down, left, right, lowpoint
heightmap={}

basin=0 #basin indentifier
l=0 #row number
risktot=0 #initialize total risk at 0

for line in Lines:
    i=0 #column number
    for char in line:
        val=int(char)
        if i<len(line)-1:
            right = int(Lines[l][i+1])
        else:
            right=99
        if i>0:
            left = int(Lines[l][i-1])
        else:
            left=99
        if l>0:
            up = int(Lines[l-1][i])
        else:
            up = 99
        if l<len(Lines)-1:
            down = int(Lines[l+1][i])
        else:
            down = 99

        heightmap[(l,i)]={'val': val, 'left':left, 'right':right, 'up':up, "down": down, 'basin':None, 'checked': False}

        if val<right and val<left and val<up and val<down: #minimum point
            risk=val+1 #assign risk val
            risktot+=risk #add to total risk
            heightmap[(l,i)]['min']=True
            heightmap[(l,i)]['basin']=basin
            basin+=1
        else:
            heightmap[(l,i)]['min']=False

        i+=1
    l+=1

print("Part 1 answer: "+ str(risktot))

#PART 2#

#function to find any points which have been assigned a basin and haven't yet been checked

def get_basin(my_dict):
    output=[]
    for key, value in my_dict.items():
        if value['checked']==False:
            if value['basin'] != None and value['basin'] !=99:
                output.append(key)
    return output
 
    return "key doesn't exist"


#function to loop through all points that haven't been checked that have an assigned basin and check for points in the y and x directions that are also in the same basin.

def basin_loop(basinPoints, hm):
    for p in basinPoints:
        l,i= p

        if hm[(l,i)]['val']==99 or hm[(l,i)]['val']==9:
            hm[(l,i)]['basin']=99
            hm[(l,i)]['checked']==True
        elif hm[(l,i)]['basin']!=None: #initialize search
            
            basin=hm[(l,i)]['basin']

            #check right
            lastval=hm[(l,i)]['val']
            for j in range(1,len(line)+1):#ensures we check to end of line
                if i+j<=len(line)-1:
                    if hm[(l,i+j)]['val']>lastval and hm[(l,i+j)]['val']<9:
                        hm[(l,i+j)]['basin']=basin
                        lastval=hm[(l,i+j)]['val']
                    elif hm[(l,i+j)]['val']==9 or hm[(l,i+j)]['val']==99:
                        break #breaks out of row check
                else:
                    break

            #check left
            lastval=hm[(l,i)]['val']
            for j in range(1,len(line)+1):#ensures we check to end of line
                if i-j>=0:
                    if hm[(l,i-j)]['val']>lastval and hm[(l,i-j)]['val']<9:
                        hm[(l,i-j)]['basin']=basin
                        lastval=hm[(l,i-j)]['val']
                    elif hm[(l,i-j)]['val']==9 or hm[(l,i-j)]['val']==99:
                        break #breaks out of row check
                else:
                    break

            #check up
            lastval=hm[(l,i)]['val']
            for m in range(1,len(Lines)+1):#ensures we check to end of rows
                if l-m>=0:
                    if hm[(l-m,i)]['val']>lastval and hm[(l-m,i)]['val']<9:
                        hm[(l-m,i)]['basin']=basin
                        lastval=hm[(l-m,i)]['val']
                    elif hm[(l-m,i)]['val']==9 or hm[(l-m,i)]['val']==99:
                        break #breaks out of row check
                else:
                    break

            #check down
            lastval=hm[(l,i)]['val']
            for m in range(1,len(Lines)+1):#ensures we check to end of rows
                if l+m<=len(Lines)-1:
                    if hm[(l+m,i)]['val']>lastval and hm[(l+m,i)]['val']<9:
                        hm[(l+m,i)]['basin']=basin
                        lastval=hm[(l+m,i)]['val']
                    elif hm[(l+m,i)]['val']==9 or hm[(l+m,i)]['val']==99:
                        break #breaks out of row check
                else:
                    break

            hm[(l,i)]['checked']=True #mark that the surroundings (y and x directions) have been checked for this point.

    return hm


basinPoints = get_basin(heightmap) #get all points with basin assigned that haven't been checked

while i>0: #loop as long as there are still points returned from function that haven't been checked
    heightmap = basin_loop(basinPoints, heightmap)
    basinPoints= get_basin(heightmap)
    #print(basinPoints)
    i = len(basinPoints)

#function to calculate numbers of cells in each basin

def basin_count(my_dict, n):
    cnt=0
    for key, value in my_dict.items():
        if value['basin']==n:
            cnt+=1
    return cnt
 
    return "key doesn't exist"

counts = [] #list to store counts in

n=0
i = basin_count(heightmap, n)

while i > 0: #loop through each basin - when i=0 all basins have been counted
    counts.append(i)
    n+=1
    i = basin_count(heightmap, n)

top3 = sorted(counts, reverse=True)[:3] #get the top three counts per basin

print('Answer to part 2 is :' + str(top3[0]*top3[1]*top3[2]))

