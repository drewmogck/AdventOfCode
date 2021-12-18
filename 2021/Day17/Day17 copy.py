"""
Advent of Code 2021
Day 17
"""
#PART 1#

#import raw data
from numpy import bitwise_not


inputfile='Day17.txt'

Lines = [line.rstrip() for line in open(inputfile)]

#first parse target range:
target_x, target_y = Lines[0][13:].split(sep=', ')

#target area: x=20..30, y=-10..-5
print(target_x, target_y)
xmin, xmax= map(int, target_x[2:].split(sep='..'))
ymin, ymax= map(int, target_y[2:].split(sep='..'))

print(xmin, xmax)
print(ymin, ymax)

# xvel, yvel = [17,-4]

def xvel_change(x, xvel):
    if xvel>0:
        xvel-=1
    elif xvel<0:
        xvel+=1
    elif xvel==0:
        xvel=0
    return xvel

def yvel_change(yvel):
    yvel-=1
    return yvel

def target_in_range(x,y):
    global xmin, xmax, ymin, ymax, highest, maxheight, xvel, yvel,solutions, xvel_init, yvel_init
    if x in range(xmin, xmax+1):
        if y in range(ymin, ymax+1):
            #print('TARGET HIT!')
            if maxheight>highest:
                    highest=maxheight
                    #print('highest', highest)
                    #print('velocities', xvel, yvel)
            

            return True
    return False

def overshot(x,y):
    global xmax, ymin
    if x > xmax or y<ymin:
        #print('TARGET OVERSHOT!', x,y, xmax)
        return True
    return False

highest = 0
solutions=0

for xvel_init in range(0, xmax+10):
    for yvel_init in range(-abs(ymin)-100,abs(ymax)+100):
        #initialize position
        xvel=xvel_init
        yvel=yvel_init

        x=0
        y=0
        maxheight=0

        while target_in_range(x,y) is False and overshot(x,y) is False: #keep doing until reach target or overshoot
            x+=xvel
            y+=yvel

            #print('xy',x, y)

            #record max height
            if y>maxheight:
                maxheight=y

            xvel=xvel_change(x,xvel)
            yvel=yvel_change(yvel)
            #print("positions ", x,y)
            #print("velocities", xvel, yvel)

        if target_in_range(x,y)==True:
            solutions+=1
            #print(xvel_init, yvel_init)

print(highest)
#print(len(solutions))
print(solutions)
    
