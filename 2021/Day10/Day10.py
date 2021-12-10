"""
Advent of Code 2021
Day 10
"""
#PART 1#

#import raw data
inputfile='Day10.txt'

Lines = [line.rstrip() for line in open(inputfile)]

#create dict for counter of open for each char:
counter = {}

openchar = ["(","[","{","<"]
closechar = [")","]","}",">"]
lossvals = [3,57,1197,25137]

totloss=0 #initialize loss sums
remline = []
line_no=0

for line in Lines:
    level=0

    for char in line:
        if char in openchar:
            counter[level]=openchar.index(char)
            level+=1
        elif char in closechar:
            if closechar.index(char)==counter[level-1]:
                #close out line reset levels down
                del counter[level-1]
                level-=1
            else:
                loss = lossvals[closechar.index(char)]
                totloss+=loss
                print("corrupt line : lose "+ str(loss)+"points")
                remline.append(line_no)
                break
    line_no+=1

print("Part 1 Answer is:" + str(totloss))

print("remove lines "+ str(remline) + " for part 2")

#Part 2#

#get lines for part 2 (remove incompletes)
with open(inputfile, 'r') as fp:
    # lines to not read
    line_numbers = remline.copy()
    # To store lines
    Lines = []
    for i, line in enumerate(fp):
        if i in line_numbers:
            continue
        else:
            Lines.append(line.strip())
            
#create dict for counter of open for each char:
counter = {}

openchar = ["(","[","{","<"]
closechar = [")","]","}",">"]
scorevals = [1,2,3,4]

line_no=0
totscore_list =[]

for line in Lines:
    totscore=0 #initialize score sums

    level=0

    for char in line:
        if char in openchar:
            counter[level]=openchar.index(char)
            level+=1
        elif char in closechar:
            if closechar.index(char)==counter[level-1]:
                #close out line reset levels down
                del counter[level-1]
                level-=1
        
    #end of line, finish the line next
    #print(counter)

    while level>0:
        newchar=closechar[counter[level-1]]
        score=scorevals[closechar.index(newchar)]
        totscore=5*totscore+score
        del counter[level-1]
        #print(newchar)
        level-=1

    totscore_list.append(totscore)
    line_no+=1

totscore_list.sort()

middle = int(len(totscore_list) / 2) 

print('Part 2 Answer:' + str(totscore_list[middle]))