"""
Advent of Code 2021
Day 2
"""
#PART 1#

#import raw datas
Lines = [line for line in open('Day2.txt')]


#define function to move postion
def move_sub(dir, n, x, y):
    if dir=='forward':
        x+=n
    elif dir=="down":
        y+=n
    elif dir=="up":
        y-=n
    return x,y

#initialize position to 0
x=0
y=0

for line in Lines:
    lsplit=line.split()
    x,y = move_sub(lsplit[0], int(lsplit[1]), x, y)
    

print("final position is:"+str(x)+","+str(y))
print("Part 1 answer is: " + str(x*y))

#part 2

#define function to move postion
def move_sub_aim(dir, n, x, y, aim):
    if dir=='forward':
        x+=n
        y+=aim*n
    elif dir=="down":
        aim+=n
    elif dir=="up":
        aim-=n
    return x,y,aim

#initialize position to 0
x=0
y=0
aim=0

for line in Lines:
    lsplit=line.split()
    x,y,aim = move_sub_aim(lsplit[0], int(lsplit[1]), x, y, aim)


print("final position is:"+str(x)+","+str(y)+" Aim="+str(aim))
print("Part 2 answer is: " + str(x*y))