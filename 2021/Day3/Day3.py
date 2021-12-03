"""
Advent of Code 2021
Day 3
"""
#PART 1#

#import raw datas
Lines = [line.rstrip() for line in open('Day3.txt')]


#function to count occurances in i'th character in line
def count_bit(line, i, zeros, ones):
    if line[i]=='0':
        zeros+=1
    elif line[i]=='1':
        ones+=1
    return zeros, ones



gamma=""
epsilon=""

for i in range(len(Lines[0])):
    #initialize zeros and ones to 0
    zeros=0
    ones=0
    for line in Lines:
        zeros, ones = count_bit(line, i, zeros, ones)

    if zeros>ones:
        gamma+='0'
        epsilon+='1'
    elif ones>zeros:
        gamma+='1'
        epsilon+='0'
        
    print(i, zeros, ones)

print(gamma)
print(epsilon)

def binaryToDecimal(n):
    return int(n,2)

gamma_dec = binaryToDecimal(gamma)
epsilon_dec = binaryToDecimal(epsilon)

#answer to part 1
print("Answer to part 1 is: "+str(gamma_dec*epsilon_dec))


#PART 2#

#initialize list for oxygen
input = Lines #initialize with all values to start

for i in range(len(Lines[0])):
    output=[]

    #initialize zeros and ones to 0
    zeros=0
    ones=0

    for line in input:
        zeros, ones = count_bit(line, i, zeros, ones) #count zeros and ones in column return result
    
    #print(zeros, ones)

    for line in input:
        if zeros>ones: #more zeros
            if line[i]=='0':
                output.append(line)
                #print(i, "line add", line, output)

        elif ones>zeros: #more ones
            if line[i]=='1':
                output.append(line)
        
        elif ones==zeros:
            if line[i]=='1':
                output.append(line)
                
    print(i, output)

    if len(output)==1:
        break

    input=output #new values

            
       
o2_rating = int(output[0],2) #oxygen generator rating

#initialize list for co2 # there will be a better way to do this with function i am sure

input = Lines #initialize with all values to start

for i in range(len(Lines[0])):
    output=[]

    #initialize zeros and ones to 0
    zeros=0
    ones=0

    for line in input:
        zeros, ones = count_bit(line, i, zeros, ones) #count zeros and ones in column return result
    
    #print(zeros, ones)

    for line in input:
        if zeros<ones: #fewer zeros
            if line[i]=='0':
                output.append(line)
                #print(i, "line add", line, output)

        elif ones<zeros: #fewer ones
            if line[i]=='1':
                output.append(line)
        
        elif ones==zeros:
            if line[i]=='0':
                output.append(line)
                
    print(i, output)

    if len(output)==1:
        break

    input=output #new values

            
       
co2_rating = int(output[0],2) #CO2 scrubber rating

print(o2_rating, co2_rating)

print("Part 2 answer is: "+str(o2_rating*co2_rating))