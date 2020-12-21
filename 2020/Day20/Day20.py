# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 20
"""

#import data        
Lines = [line.rstrip() for line in open('Day20.txt')]

tiles = {}
tilelist=[]

for line in Lines:
    if not not line:
        if line.startswith('Tile'):
            tileno = line[5:9]
            tilelist.append(tileno)
            rowcount=0
        else:
            tiles[tileno,rowcount]=line
            rowcount+=1

def reverse_txt(x):
  return x[::-1]

edges={}
          
for tile in tilelist:
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
                        print(tile, tile2, 'MATCH', t, t2)
                        
corners=[]                        
for tile in tilelist:
    if edgematch_count.count(tile)==4:
        corners.append(tile)
        
print(corners)

def product(list):
    p = 1
    for i in list:
        p *= int(i)
    return p

print(product(corners)) #part 1 answer      
                        