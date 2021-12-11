"""
Advent of Code 2021
Day 11
"""
#PART 1#

#import raw data
inputfile='Day11.txt'

Lines = [line.rstrip() for line in open(inputfile)]

#store data in dict of locations. r, c = locations in row, column
grid = {}

r=0 #initialize rows to 0
for line in Lines:
    c=0 #initialize columns to 0
    for char in line:
        grid[(r,c)]={'lev':int(char)}
        c+=1
    r+=1

#print(grid)

#function for taking a step
def step(my_dict):
    flash=[]
    for key, value in my_dict.items():
        value['lev']+=1
        if value['lev']==10:
            flash.append(key)
    return flash

#function to reset flashed to 0:
def reset(my_dict):
    for key, value in my_dict.items():
        if value['lev']>9:
            value['lev']=0

#function to handle flash
def on_flash(locs):

    def dir_loc(r_,c_, dir): #function to handle location testing
        if dir=="R":
            cshift = 1
            rshift = 0
        elif dir=="L":
            cshift = -1
            rshift = 0
        elif dir=="U":
            cshift = 0
            rshift = -1
        elif dir=="D":
            cshift = 0
            rshift = 1
        elif dir=="UL":
            cshift = -1
            rshift = -1
        elif dir=="UR":
            cshift = 1
            rshift = -1
        elif dir=="DL":
            cshift = -1
            rshift = 1
        elif dir=="DR":
            cshift = 1
            rshift = 1

        return (r_+rshift, c_+cshift)


    flash2=[]
    for l in locs:
        l_row=l[0]
        l_col=l[1]



        if l_col<len(line)-1: #right
            loc_=dir_loc(l_row, l_col, "R")
            grid[loc_]['lev']+=1
            if grid[loc_]['lev']==10:
                flash2.append(loc_)
        if l_col>0: #left
            loc_=dir_loc(l_row, l_col, "L")
            grid[loc_]['lev']+=1
            if grid[loc_]['lev']==10:
                flash2.append(loc_)
        if l_row>0: #Up
            loc_=dir_loc(l_row, l_col, "U")
            grid[loc_]['lev']+=1
            if grid[loc_]['lev']==10:
                flash2.append(loc_)

            if l_col<len(line)-1: #up right
                loc_=dir_loc(l_row, l_col, "UR")
                grid[loc_]['lev']+=1
                if grid[loc_]['lev']==10:
                    flash2.append(loc_)
            if l_col>0: #up left
                loc_=dir_loc(l_row, l_col, "UL")
                grid[loc_]['lev']+=1
                if grid[loc_]['lev']==10:
                    flash2.append(loc_)

        if l_row<len(Lines)-1: #down
            loc_=dir_loc(l_row, l_col, "D")
            grid[loc_]['lev']+=1
            if grid[loc_]['lev']==10:
                flash2.append(loc_)

            if l_col<len(line)-1: #down right
                loc_=dir_loc(l_row, l_col, "DR")
                grid[loc_]['lev']+=1
                if grid[loc_]['lev']==10:
                    flash2.append(loc_)
            if l_col>0: #down left
                loc_=dir_loc(l_row, l_col, "DL")
                grid[loc_]['lev']+=1
                if grid[loc_]['lev']==10:
                    flash2.append(loc_)

    return(flash2)


flashcounter=0
for n in range(100):
    flash=step(grid)
    i=len(flash)
    flashcounter+=i

    while i>0:
        flash=on_flash(flash)
        i=len(flash)
        flashcounter+=i
        #print(flash)

    #reset any that have flashed to 0
    reset(grid)


print(flashcounter) #part 1 answer

#part 2#

#reinitialize grid
grid = {}

r=0 #initialize rows to 0
for line in Lines:
    c=0 #initialize columns to 0
    for char in line:
        grid[(r,c)]={'lev':int(char)}
        c+=1
    r+=1

#function to check for simulflash
def check(my_dict):
    for key, value in my_dict.items():
        if value['lev']==0:
            continue
        else:
            return False
        
    return True


flashcounter=0
n=0

while check(grid)==False:
    flash=step(grid)
    i=len(flash)
    flashcounter+=i

    while i>0:
        flash=on_flash(flash)
        i=len(flash)
        flashcounter+=i
        #print(flash)

    #reset any that have flashed to 0
    reset(grid)
    n+=1


print(n)








