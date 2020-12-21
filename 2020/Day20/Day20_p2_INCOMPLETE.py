# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 20
"""
import numpy as np

#import data        
Lines = [line.rstrip() for line in open('Day20.txt')]

tiles = {}
tilelist=[]

#import data
for line in Lines:
    if not not line:
        if line.startswith('Tile'):
            tileno = line[5:9]
            tilelist.append(tileno)
            rowcount=0
        else:
            tiles[tileno,rowcount]=line
            rowcount+=1

def reverse_txt(x): #function to reverse strings
  return x[::-1]


def edgemaker(tileinput):
    edges={}
              
    for tile in tileinput:
        top_f = tiles[tile,0]
        top_r = reverse_txt(top_f)
        
        bot_f = tiles[tile,9]
        bot_r = reverse_txt(bot_f)
        
        left_f = ''
        left_f = left_f.join([tiles[tile , i][0] for i in range(0,10)])
        left_r = reverse_txt(left_f)
            
        right_f = ''
        right_f = right_f.join([tiles[tile , i][-1] for i in range(0,10)])    
        right_r = reverse_txt(right_f)
        
        edges[tile]=[top_f, bot_f, top_r, bot_r, right_f, right_r, left_f, left_r]
    
    edgematch_count=[]    
    for tile in edges:
        for t in edges[tile]:
            for tile2 in edges:
                if tile2 is not tile:
                    for t2 in edges[tile2]:
                        if t==t2:
                            edgematch_count.append(tile)
                            #print(tile, tile2, 'MATCH', t, t2)
    
    corners=[]                        
    for tile in tilelist:
        if edgematch_count.count(tile)==4:
            corners.append(tile)
                         
       
    sides=[]
    for tile in tilelist:
        if edgematch_count.count(tile)==6:
            sides.append(tile)
            
    return corners, sides

level=0
tilesin= tilelist.copy() #first round, all tiles
store={}
newtileslen=len(tilesin)

while newtileslen>=4:
    newtiles=[]
        
    store[level] = edgemaker(tilesin)
    used_tiles=store[level][0]+store[level][1]
    for element in tilesin:
        print(element)
        #print(element in used_tiles)
        if element not in used_tiles:
             newtiles.append(element)
    tilesin=newtiles
    newtileslen=len(newtiles)
    level+=1
        

#get tile back
def get_tile(t_no):
    return [tiles[t_no, i] for i in range(0,10)]

