# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day22 Part 1
"""

#import data        
player1, player2 = open('Day22.txt').read().split("\n\n",1) #splits input file

player1 = player1[10:].split()
player1 = list(map(int, player1)) 
player2=player2[10:].split()
player2 = list(map(int, player2)) 


while len(player1)>0 and len(player2)>0:
    card1=player1[0]
    card2=player2[0]
  
    player1.remove(card1)
    player2.remove(card2)
    
    if card1>card2:
        player1.append(card1)
        player1.append(card2)
    elif card2>card1:
        player2.append(card2)
        player2.append(card1)

print(player1, player2)        

def winner(deck1, deck2):
    if len(deck1)<len(deck2):
        return deck2
    else:
        return deck1

winning_deck=winner(player1, player2)

cardval=len(winning_deck)
count=0
scoresum=0

for card in winning_deck:
    score=card*cardval
    scoresum+=score
    cardval-=1
    
print(scoresum) #part 1 answer
    