# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day22 Part 2
"""

#import data        
player1, player2 = open('Day22.txt').read().split("\n\n",1) #splits input file

player1 = player1[10:].split()
player1 = list(map(int, player1)) 
player2=player2[10:].split()
player2 = list(map(int, player2)) 

#print(player1, player2)



def winner(d1, d2):
    if len(d1)<len(d2):
        return d2
    else:
        return d1

def cardcount(deck):
    return len(deck)
    


def recursive_combat(decks_store_sub, deck1, deck2):
   
    while len(deck1)>0 and len(deck2)>0:
        if [deck1,deck2] not in decks_store_sub:
            #print('store deck:', [deck1, deck2])
            decks_store_sub.append([deck1.copy(), deck2.copy()])
        else:
            #print('decks seen before! Player 1 wins!', decks_store_sub, [deck1, deck2])
            deck1=[1]
            deck2=[]
            break
            
        
        card_1=deck1[0]
        card_2=deck2[0]
        
        deck1.remove(card_1)
        deck2.remove(card_2)
        
        #print("recursive", card_1, cardcount(deck1), card_2, cardcount(deck1))
        
        if card_1<=cardcount(deck1) and card_2<=cardcount(deck2):
            recursive_combat([], deck1[:card_1].copy(), deck2[:card_2].copy())
        else:
            if card_1>card_2:
                deck1.append(card_1)
                deck1.append(card_2)
            elif card_2>card_1:
                deck2.append(card_2)
                deck2.append(card_1)
        
        #print('recursion', deck1, deck2)
    
    #print('decks:', deck1, deck2)
    if winner(deck1, deck2)==deck1:
        winnum=1
    elif winner(deck1, deck2)==deck2:
        winnum=2
    return [True, deck1, deck2, winnum]
        

    
  
#main game
# decks_store=[]
while len(player1)>0 and len(player2)>0:
    # if [player1,player2] not in decks_store:
    #         decks_store.append([player1,player2])
    # else:
    #     print('decks seen before! Player 1 wins!')
    #     player1=[1]
    #     player2=[]
    #     break
    
    card1=player1[0]
    card2=player2[0]
  
    player1.remove(card1)
    player2.remove(card2)
    
    #print(card1, cardcount(player1), card2, cardcount(player2))
    
    if card1<=cardcount(player1) and card2<=cardcount(player2): #goto recursive combat

        player1new=player1[:card1].copy() #initial inputs for recursive
        player2new=player2[:card2].copy() #initial inputs for recursive
        
        #print('new decks:', card1, player1new, card2, player2new)
        
        deckstore=[]
        round_i = recursive_combat([], player1new, player2new)
        
        win = round_i[0]
        win_play=round_i[3]
                  
        
        if win==True:
            if win_play==1: #player 1 wins round
                player1.append(card1)
                player1.append(card2)
            elif win_play==2: #player 2 wins round
                player2.append(card2)
                player2.append(card1)
                
    else: #standard rules
        if card1>card2:
            player1.append(card1)
            player1.append(card2)
        elif card2>card1:
            player2.append(card2)
            player2.append(card1)
    
    #print(player1, player2)

            
            
            
#print(player1, player2)        



winning_deck=winner(player1, player2)

cardval=len(winning_deck)
count=0
scoresum=0

for card in winning_deck:
    score=card*cardval
    scoresum+=score
    cardval-=1
    
print(scoresum) #part 2 answer