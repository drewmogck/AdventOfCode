"""
Advent of Code 2021
Day 13
"""
import numpy as np
import matplotlib.pyplot as plt

#PART 1#

#import raw data
inputfile='Day13.txt'

Lines = [line.rstrip() for line in open(inputfile)]

#first need to get the initial dimensions of the paper

def get_dimensions(input):
    max_x=0
    max_y=0

    for line in input:
        if line =='':
            break
        else:
            x,y= line.split(sep=",")
            if int(x)>max_x:
                max_x=int(x)
            if int(y)>max_y:
                max_y=int(y)
    
    return max_x, max_y

dim_x, dim_y = get_dimensions(Lines)

#initialize sheet

def read_page(input):
    page = np.zeros((dim_y+1,dim_x+1)) 
    for line in input:
        if line =='':
            break
        else:
            x,y= line.split(sep=",")
            x=int(x)
            y=int(y)
            page[y,x]=1

    return page

page = read_page(Lines)

def get_folds(input):
    f=0
    folds={}
    for line in input:
        if line.startswith('fold'):
            folddir, num = line[11:].split(sep="=")
            folds[f] = {'folddir': folddir, 'num': int(num)}
            f+=1

    return(folds)

folds = get_folds(Lines)

#do folding

def folding(fold, page, folds):
    if folds[fold]['folddir']=='x': #fold left
        page=np.delete(page, (folds[fold]['num']), axis=1) #delete column

        page1, page2 = np.hsplit(page,[folds[fold]['num']])

        #get dimensions of page 1 and page 2
        p1_shp= page1.shape
        p2_shp= page2.shape

        #calculate difference in dimensions

        x_dif = p1_shp[1]-p2_shp[1]
        #print(x_dif)

        #place page 2 at right of equivilant sized page as page1
        page2_stack = np.zeros((p2_shp[0],x_dif))

        #add stack to end
        page2 = np.hstack((page2, page2_stack))        

        #flip page 2 left
        page2flip=np.fliplr(page2)

        result=np.where(page2flip+page1 > 0, 1, 0)

    elif folds[fold]['folddir']=='y': #fold up
        page=np.delete(page, (folds[fold]['num']), axis=0) #delete row

        page1, page2 = np.vsplit(page,[folds[fold]['num']])

        #get dimensions of page 1 and page 2
        p1_shp= page1.shape
        p2_shp= page2.shape

        #calculate difference in dimensions

        y_dif = p1_shp[0]-p2_shp[0]

        #place page 2 at bottom of equivilant sized page as page1
        page2_stack = np.zeros((y_dif, p2_shp[1]))

        #add stack to end
        page2 = np.vstack((page2, page2_stack))

        #flip page 2 up
        page2flip=np.flipud(page2)

        result=np.where(page2flip+page1 > 0, 1, 0)
    return result

for fold in [0]:
    print(np.sum(folding(fold, page, folds))) #part 1 answer

##part 2

page = read_page(Lines)
for fold in folds:
    page = folding(fold, page, folds)

plt.imshow(page)
plt.show()