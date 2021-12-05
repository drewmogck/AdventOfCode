"""
Advent of Code 2021
Day 5
"""
#PART 1#

#import raw datas
Lines = [line.rstrip() for line in open('Day5.txt')]

#function to determine all points crossed (hz and vert) based on start and endpoints
def cross(xy1, xy2, diag):
    x1=int(xy1[0])
    y1=int(xy1[1])
    x2=int(xy2[0])
    y2=int(xy2[1])

    if x1==x2: #vertical
        if y1>y2:
            ylist=list(k for k in range(y2, y1+1))
            return [x1]*len(ylist), ylist
        elif y1<y2:
            ylist= list(k for k in range(y1, y2+1))
            return [x1]*len(ylist), ylist        
    if y1==y2: #Horizontal
        if x1>x2:
            xlist=list(j for j in range(x2, x1+1))
            return xlist, [y1]*len(xlist)
        elif x1<x2:
            xlist=list(j for j in range(x1, x2+1))
            return xlist, [y1]*len(xlist)
    if diag==True:
        if abs(y2-y1)==abs(x2-x1): #diagonal
            if x1>x2:
                xlist=list(j for j in range(x2, x1+1))
                if y1>y2:
                    ylist=list(k for k in range(y2, y1+1))
                elif y1<y2:
                    ylist=list(k for k in reversed(range(y1, y2+1)))
            elif x1<x2:
                xlist=list(j for j in range(x1, x2+1))
                if y1>y2:
                    ylist=list(k for k in reversed(range(y2, y1+1)))
                elif y1<y2:
                    ylist=list(k for k in range(y1, y2+1))
            return xlist, ylist


    return [], []

#function to calculate the grid:
def grid_build(Lines, diag):
    #define dictionary to store positions and endpoints
    grid = {}
    #split lines into endpoints and store data in dictionary:

    for line in Lines:
        segments= line.split(sep=' -> ')
        xy1, xy2= segments[0].split(','), segments[1].split(',')

        x_,y_ = cross(xy1, xy2, diag) #get lines
        
        points = list(zip(x_, y_))

        for p in points:
            x=p[0]
            y=p[1]
            try: 
                grid[(x,y)]=grid[(x,y)]+1
            except KeyError: #add space to grid if it doesn't exist yet
                grid[(x,y)]=1
                pass
        
    return grid


#part 1 answer:
part1grid = grid_build(Lines, diag=False)
vals_over2 = sum(v > 1  for v in part1grid.values())
print("Answer to part 1 is:"+ str(vals_over2))


#Part 2
#edited function to account for diagonals
part2grid = grid_build(Lines, diag=True)
vals_over2 = sum(v > 1  for v in part2grid.values())
print("Answer to part 2 is:"+ str(vals_over2))