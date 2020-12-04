# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 4
"""

import pandas as pd
import numpy as np
import re

##PART 1
# --- Day 4: Passport Processing ---
# You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.

# It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.

# Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.

# The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
# Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

# Here is an example batch file containing four passports:

# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm

# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929

# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm

# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in
# The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).

# The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.

# The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.

# According to the above rules, your improved system would report 2 valid passports.

# Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

#
# Using readlines() 
path='Day4.txt'

with open(path, "a") as a_file:
  a_file.write("\n")
  a_file.write("\n")
#make sure last line is always a blank line for final count

file = open(path, 'r') 
Lines = file.readlines() 

#initialize values to 0
byr=0
iyr=0
eyr=0
hgt=0
hcl=0
ecl=0
pid=0
cid=0

passed=0 #total passports cleared

def typecheck(line_input,id_type): #id_type eg: 'byr'
    if id_type in line_input:
        return 1
    else:
        return 0

ppt_index = 0
print("passport #"+str(ppt_index))

for line in Lines:
    if line!='\n':
        byr = byr + typecheck(line, 'byr')
        iyr = iyr + typecheck(line, 'iyr')
        eyr = eyr + typecheck(line, 'eyr')
        hgt = hgt + typecheck(line, 'hgt')
        hcl = hcl + typecheck(line, 'hcl')
        ecl = ecl + typecheck(line, 'ecl')
        pid = pid + typecheck(line, 'pid')
        cid = cid + typecheck(line, 'cid')
    elif line=='\n':
        id_check=(byr+iyr+eyr+hgt+hcl+ecl+pid)/7
        if id_check==1:
            passed+=1
            print("Pass " + str(passed))
        else:
            print("Fail")
            
        ppt_index+=1
        print("passport #"+ str(ppt_index))
        
        #reset values to 0
        byr=0
        iyr=0
        eyr=0
        hgt=0
        hcl=0
        ecl=0
        pid=0
        cid=0
        
#--- Part Two ---
# The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!

# You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
# Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:

# byr valid:   2002
# byr invalid: 2003

# hgt valid:   60in
# hgt valid:   190cm
# hgt invalid: 190in
# hgt invalid: 190

# hcl valid:   #123abc
# hcl invalid: #123abz
# hcl invalid: 123abc

# ecl valid:   brn
# ecl invalid: wat

# pid valid:   000000001
# pid invalid: 0123456789
# Here are some invalid passports:

# eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946

# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007
# Here are some valid passports:

# pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f

# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022

# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
# Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?
        



ppt_index = 0
print("passport #"+str(ppt_index))

ppt_master=[] #master list of lists for passports
ppt_list=[]

#loop thorough passports and create list containing eac
for line in Lines:
    if line!='\n':
        ppt_list = ppt_list +line.rstrip('\n').split(' ')
    elif line=='\n':
        ppt_master.append(ppt_list)
        ppt_index+=1
        print("passport #"+str(ppt_index))
        ppt_list=[]
    

eye_col_list =['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def id_validate(id_val, id_type):
    if id_type=='byr':
        if int(id_val)>=1920 and int(id_val)<=2002:
            return 1
        else:
            return 0
    elif id_type=='iyr':
        if int(id_val)>=2010 and int(id_val)<=2020:
            return 1
        else:
            return 0
    elif id_type=='eyr':
        if int(id_val)>=2020 and int(id_val)<=2030:
            return 1
        else:
            return 0
    elif id_type=='hgt':
        height=id_val[:-2]
        units=id_val[-2:]
        if units=="in":
            if int(height)>=59 and int(height)<=76:
                return 1
            else:
                return 0
        elif units=='cm':
            if int(height)>=150 and int(height)<=193:
                return 1
            else:
                return 0
        else:
            return 0
    elif id_type=='hcl':
        if re.match('[#][a-f0-9]{6}$', id_val):
            return 1
        else:
            return 0
    elif id_type=='ecl':
        if id_val in eye_col_list:
            return 1
        else:
            return 0
    elif id_type=='pid':
        if re.match("[\d]{9}$", id_val):
            return 1
        else:
            return 0
    elif id_type=='cid':
        return 0


def Convert(lst): #converts list paris to dictionary
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
        
id_valid=0
passed=0
ppt_sum=0      
id_totlist=[]
result_out=[]

store_output=[]

for ppt in ppt_master:
    print(ppt)
    for id in ppt:
        id_split = id.split(':')
        
        if id_split[0]=='byr':
            byr=id_validate(id_split[1], id_split[0])
        elif id_split[0]=='iyr':
            iyr=id_validate(id_split[1], id_split[0])
        elif id_split[0]=='eyr':
            eyr=id_validate(id_split[1], id_split[0])
        elif id_split[0]=='hgt':
            hgt=id_validate(id_split[1], id_split[0])
        elif id_split[0]=='byr':
            byr=id_validate(id_split[1], id_split[0])
        elif id_split[0]=='hcl':
            hcl=id_validate(id_split[1], id_split[0])
        elif id_split[0]=='ecl':
            ecl=id_validate(id_split[1], id_split[0])
        elif id_split[0]=='pid':
            pid=id_validate(id_split[1], id_split[0])
        elif id_split[0]=='cid':
            cid=id_validate(id_split[1], id_split[0])
        
        
        id_totlist= id_totlist +id_split
        # id_valid = id_validate(id_split[1], id_split[0])
        # print(id_split)
        # print(id_valid)
        
        # ppt_sum+=id_valid
        # id_valid=0 #reset id valid to 0
    
    id_check=(byr+iyr+eyr+hgt+hcl+ecl+pid)/7
    if id_check==1:
        passed+=1
        print("Pass " + str(passed))
        result='pass'
    else:
        print("Fail")
        result='fail'
    ppt_sum=0
    
    #store output values
    #convert id_totlist to dictionary and store values
    id_dict=Convert(id_totlist)
    
    result_out = [[id_dict.get('byr'), id_dict.get('iyr'), id_dict.get('eyr'), id_dict.get('hgt'), id_dict.get('hcl'), id_dict.get('ecl'),id_dict.get('pid'), id_dict.get('cid')],[byr, iyr, eyr, hgt, hcl, ecl, pid, cid], [result]]
    store_output.append(result_out)
    #reset values to 0
    byr=0
    iyr=0
    eyr=0
    hgt=0
    hcl=0
    ecl=0
    pid=0
    cid=0
    
    id_totlist=[]
    # input("Press Enter to continue...")
        
df = pd.DataFrame(store_output, columns = ['passport', 'itempass', 'passportpass'])  
df.to_csv('output.csv')


       
    
