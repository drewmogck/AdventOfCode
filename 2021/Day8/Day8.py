"""
Advent of Code 2021
Day 8
"""
#PART 1#

#import raw datas
Lines = [line.rstrip() for line in open('Day8ex.txt')]

#split signals and output value and store in dictionary
inputs ={}

i=0
for line in Lines:
    line= line.split(sep=' | ')
    inputs['signal_'+str(i)]= line[0].split(sep=' ')
    inputs['output_'+str(i)]= line[1].split(sep=' ')
    i+=1

#print(inputs)

#loop through
count=0
for j in range(len(Lines)):
    for k in range(len(inputs['output_'+str(j)])):
        if len(inputs['output_'+str(j)][k])==2 or len(inputs['output_'+str(j)][k])==4 or len(inputs['output_'+str(j)][k])==3 or len(inputs['output_'+str(j)][k])==7:
            #print(inputs['output_'+str(j)][k])
            count+=1

print(count)

#PART 2# Unfinished

data={}

i=0
for line in Lines:
    line= line.split(sep=' | ')
    data[str(i)]={'signal':line[0].split(sep=' '), 'output':line[1].split(sep=' '), 'value':None}
    i+=1

print(data['5']['output'])

#function to test for similarity between string and list
def similarity(str1,list):
    out=[]
    for l in list:
        c=0
        for s in str1:  
            if s in l:
                c+=1
        out.append(c)
    return out



#start with first line for testing
    
i=0
signal = data[str(i)]['signal']

grp_069=[]
grp_235=[]

for s in signal:
    print(s)
    if len(s)==2:
        data[str(i)]['value']=1
    elif len(s)==4:
        data[str(i)]['value']=4
    elif len(s)==3:
        data[str(i)]['value']=7
    elif len(s)==7:
        data[str(i)]['value']=8
    elif len(s)==6: #0,6, or 9
        grp_069.append(s)
    elif len(s)==5: #2,3,5
        grp_235.append(s)

#sort strings for ease of readability
grp_069 = [''.join(sorted(ele)) for ele in grp_069]
grp_235 = [''.join(sorted(ele)) for ele in grp_235]

print(grp_069)
print(grp_235)

# for g in grp_069:
#     for val in similarity(g, grp_069):
#         if val !=len(g):
            
for g in grp_235:
    for val in similarity(g, grp_235):
        print(val)