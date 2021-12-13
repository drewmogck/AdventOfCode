#solution from reddit thread. Link below.
#https://www.reddit.com/r/adventofcode/comments/rehj2r/comment/ho7x83o/?utm_source=share&utm_medium=web2x&context=3

#import raw data
inputfile='Day12.txt'

from collections import defaultdict
neighbours = defaultdict(list)

for line in open(inputfile):
    a, b = line.strip().split('-')
    neighbours[a] += [b]
    neighbours[b] += [a]

def search(part, seen=set(), a='start'):
    if a == 'end': return 1
    if a in seen:
        if a == 'start': return 0
        if a.islower():
            if part==1: return 0
            else: part = 1

    return sum(search(part, seen|{a}, b)
                 for b in neighbours[a])

print(search(part=1), search(part=2))