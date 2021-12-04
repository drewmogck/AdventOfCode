"""
Advent of Code 2021
Day 4
"""
#PART 1#

#import raw datas
Lines = [line.rstrip() for line in open('Day4.txt')]

#get calls
calls = Lines[0].split(sep=',')

#initialize dict to store board values
boards={}

n=0 # boardcounter #Notes: use x,y to denote postion on board in x/y space. n will represent board number
yi=0

#define boards
for line in Lines[2:]:
    if line=="":
        n+=1
        yi=0 #reset y counter to 0
        pass
    else:
        #split line by spaces to get distinct values
        linesplit=line.split()
        xi=0#initialize xi to 0

        for i in linesplit:
            boards[(xi,yi,n)]=[i, 0] #record value at position #0 reflects that the number hasn't been called yet. Change to 1 when called
            xi+=1
        yi+=1 #add 1 to yi for next row


#print(boards)

#note: boards are 5 by 5, and there are now n (pythonic counting) boards

#define function to check value and flip
def check_call(call, space):
    if space[0]==call:
        return [space[0], 1]
    else:
        return space


#define function to call bingos and flip spaces
def bingo_draw(call, boards):
    
    boards = {key: check_call(call, value) for key, value in boards.items()}

    return boards


##play bingo!
flag = False

for c in calls:
    boards = bingo_draw(c, boards)
    #check for win
    for m in range(n+1):
        for x in range(5): 
            sumx=0 #initialize sum to 0 #columns
            for y in range(5): 
                sumx+=boards[(x,y,m)][1]
                if sumx==5:
                    flag = True
                    print('WINNER Columns!!!', m, x, c)
                    break
            if flag==True:
                break
        if flag==True:
            break  
        for y in range(5): 
            sumy=0 #initialize sum to 0 #rows
            for x in range(5): 
                sumy+=boards[(x,y,m)][1]
                if sumy==5:
                    flag = True
                    print('WINNER Rows!!!', m, y, c)
                    break
            if flag==True:
                break
        if flag==True:
            break
    if flag==True:
        break


#winning number is c, winning board is m. need sum of non called numbers on board m

boardsum = 0 #initialize board sum to zero
for x in range(5):
    for y in range(5):
        if boards[(x,y,m)][1]==0: #unmarked
            boardsum+=int(boards[(x,y,m)][0]) #add value

#part 1 answer
print("Part 1 answer is: "+str(boardsum*int(c)))


##part 2 - find last board that wins##
#get calls
calls = Lines[0].split(sep=',')

#initialize dict to store board values
boards={}

n=0 # boardcounter #Notes: use x,y to denote postion on board in x/y space. n will represent board number
yi=0

#define boards
for line in Lines[2:]:
    if line=="":
        n+=1
        yi=0 #reset y counter to 0
        pass
    else:
        #split line by spaces to get distinct values
        linesplit=line.split()
        xi=0#initialize xi to 0

        for i in linesplit:
            boards[(xi,yi,n)]=[i, 0] #record value at position #0 reflects that the number hasn't been called yet. Change to 1 when called
            xi+=1
        yi+=1 #add 1 to yi for next row


#print(boards)

#note: boards are 5 by 5, and there are now n (pythonic counting) boards

#define function to check value and flip
def check_call(call, space):
    if space[0]==call:
        return [space[0], 1]
    else:
        return space


#define function to call bingos and flip spaces
def bingo_draw(call, boards):
    
    boards = {key: check_call(call, value) for key, value in boards.items()}

    return boards



##play bingo!
#define list to track which boards have won
wins=[]
for b in range(n+1):
    wins.append(0)


flag = False
for c in calls:
    boards = bingo_draw(c, boards)
    #check for win
    for m in range(n+1):
        for x in range(5): 
            sumx=0 #initialize sum to 0 #columns
            for y in range(5): 
                sumx+=boards[(x,y,m)][1]
                if sumx==5:
                    print('WINNER Columns!!!', m, x, c)

                    wins[m]=1
                    if sum(wins)==n+1:
                        flag=True
                        #store winning values
                        winning_board=m
                        winning_value=c

                        winning_boardsum = 0 #initialize board sum to zero
                        for x in range(5):
                            for y in range(5):
                                if boards[(x,y,m)][1]==0: #unmarked
                                    winning_boardsum+=int(boards[(x,y,m)][0]) #add value
                        break
            if flag==True:
                break
        if flag==True:
            break 

        for y in range(5): 
            sumy=0 #initialize sum to 0 #rows
            for x in range(5): 
                sumy+=boards[(x,y,m)][1]
                if sumy==5:
                    print('WINNER Rows!!!', m, y, c)

                    wins[m]=1
                    
                    if sum(wins)==n+1:
                        flag=True
                        #store winning values
                        winning_board=m
                        winning_value=c

                        winning_boardsum = 0 #initialize board sum to zero
                        for x in range(5):
                            for y in range(5):
                                if boards[(x,y,m)][1]==0: #unmarked
                                    winning_boardsum+=int(boards[(x,y,m)][0]) #add value
                        break
            if flag==True:
                break
        if flag==True:
            break
    if flag==True:
        break

#winning number is c, winning board is m. need sum of non called numbers on board m


#part 1 answer
print("Part 2 answer is: "+str(winning_boardsum*int(winning_value)))
        