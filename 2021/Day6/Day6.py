"""
Advent of Code 2021
Day 6
"""
#solution inspired by https://www.reddit.com/r/adventofcode/comments/r9z49j/comment/hnfis0v/?utm_source=share&utm_medium=web2x&context=3

#PART 1#

#import raw datas
Lines = [line.rstrip() for line in open('Day6.txt')]

data = list(map(int, Lines[0].split(sep=",")))

n=80

#function to run a single day calculation
def day(data):
  for d in range(len(data)):
    if data[d]==0: data.append(8); data[d]=6
    else: data[d]-=1

def runDays(data, n):
  x=data.copy()
  for i in range(n):
    day(x)
  return len(x)

print("Part 1:",runDays(data, 80))

#PART 2#

n=256

def group_runDays(data, n):
  s={} #dict to store counts for each group
  for i in range(9): s[i]=data.count(i) # store counts for each group
  for day in range(n):
    newFish = s[0]
    for i in range(8):
        s[i]=s[i+1] #cycle each up a count
    s[6]+=newFish
    s[8]=newFish
  return sum(s.values())

print("Part 2:",group_runDays(data, 256))
