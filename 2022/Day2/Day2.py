"""
Advent of Code 2022
Day 2
"""

#import raw datas
with open('Day2.txt') as f:
    lines = [line.rstrip() for line in f]

#PART 1#

#dict to store points value for move
points = {'X':1, 'Y':2, 'Z':3}
outcome = {'lose':0, 'draw':3, 'win':6}

#function to get score of line
def play(opponent, me):
    if me=='X': #rock
        if opponent=='A': #rock
            return 'draw'
        elif opponent=='B': #paper
            return 'lose'
        elif opponent=='C': #scissors
            return 'win'

    elif me=='Y': #paper
        if opponent=='A': #rock
            return 'win'
        elif opponent=='B': #paper
            return 'draw'
        elif opponent=='C': #scissors
            return 'lose'

    elif me=='Z': #scissors
        if opponent=='A': #rock
            return 'lose'
        elif opponent=='B': #paper
            return 'win'
        elif opponent=='C': #scissors
            return 'draw'

def score(turn):
    turnsplit=turn.split()
    opponent = turnsplit[0]
    me = turnsplit[1]

    return(outcome[play(opponent, me)]+points[me])

totscore=0

for line in lines:
    totscore+=score(line)

print(totscore) #part 1 answer


#PART 2#
points2 = {'R':1, 'P':2, 'S':3}
outcome2= {'X':0, 'Y':3, 'Z':6}

def play2(opponent, me):
    if me=='X': #lose
        if opponent=='A': #rock
            return 'S'
        elif opponent=='B': #paper
            return 'R'
        elif opponent=='C': #scissors
            return 'P'

    elif me=='Y': #tie
        if opponent=='A': #rock
            return 'R'
        elif opponent=='B': #paper
            return 'P'
        elif opponent=='C': #scissors
            return 'S'

    elif me=='Z': #win
        if opponent=='A': #rock
            return 'P'
        elif opponent=='B': #paper
            return 'S'
        elif opponent=='C': #scissors
            return 'R'

def score2(turn):
    turnsplit=turn.split()
    opponent = turnsplit[0]
    me = turnsplit[1]

    return(outcome2[me]+points2[play2(opponent, me)])

totscore=0

for line in lines:
    totscore+=score2(line)

print(totscore) #part 1 answer