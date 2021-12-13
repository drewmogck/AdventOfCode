"""
Advent of Code 2021
Day 12
"""
#PART 1#

#import raw data
inputfile='Day12ex.txt'

Lines = [line.rstrip() for line in open(inputfile)]

#function to determine small or big cave and return allowed visits
def cave_size(cave_name):
    if cave_name.isupper():
        return(float('inf'))
    elif cave_name.islower():
        return 1


#dict for map
cavemap = {}

#create the map
for line in Lines:
    node=line.split(sep='-')
    
    for (i,j) in [(0,1),(1,0)]:
        if node[j]!='start':
            if node[i] in cavemap:
                if node[j] not in cavemap[node[i]]:
                    cavemap[node[i]].append(node[j])
            else:
                cavemap[node[i]]=[node[j]]

#define dict to store visits
visits_clean={}
for c in cavemap:
    visits_clean[c]={'visits':0, 'max_visits':cave_size(c)}

#initialize at beginning:
pos='start'
count=0 #count successful paths
i=0 #path tracker new instance of i initiates for each possible path
visits=[] #list to store visits dictionaries as i is iterated

#define function to follow a path
def get_nextsteps(cave, v):
    if cave=='end':
        count+=1
        return [], v, count
    
    #add count since we have visited cave
    v[cave]['visits']+=1

    if v[cave]['visits']>v[cave]['max_visits']:
        #print('not a valid path')
        return [], v, count #move to next path

    nextstep = cavemap[cave] #gets next possible steps

    return nextstep, v, count

move = cavemap[pos] #gets first paths to move

for m in move:
    visits[i]=visits_clean #resets to clean number of visits for path
    
    nextstep, visits[i], count = get_nextsteps(m, i, visits[i])
    test = nextstep.copy()

    while len(test)>0:
        for n in nextstep:
            nextstep, visits[i], count = get_nextsteps(m, i, visits[i])
            test = nextstep.copy()



