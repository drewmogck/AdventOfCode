# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 19
"""

#code started from: https://gist.github.com/tanelikaivola/0ecc8fecd6035472daebb3b171016218 and modified/commented for my understanding

import regex
import re

#import data        
rules_s, messages_s = open('Day19.txt').read().split("\n\n",1) #splits input file

def defs(rules):
    for rule in rules.split('\n'):
        n,s = rule.split(': ',1)
        #print(n, s)
        s = regex.sub(r'\s*(\d+)\s*',r'(?&r\1)',s) #turns ' 2 3 | 5 5' into: '(?&r2)(?&r3)|(?&r5)(?&r5)'
            #\s is whitespace
            #\d is digit, + is any number of times
            #star will catch 0 or more repittions as many as possible. eg. ab* will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.
            #The 'r' at the start of the pattern string designates a python "raw" string which passes through backslashes without change
            #The question mark quantifier indicates that you want to match either one or zero occurrences of this pattern.
            #If sub-expression is placed in parentheses, it can be accessed with \1 or $1 and so on.
            
        s = regex.sub(r'"(\w+)"',r'\1',s) #converts '"b"' to 'b'
        yield "(?P<r{}>{})".format(n,s)
        
        #The format() method formats the specified value(s) and insert them inside the string's placeholder.
        #The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.
        
        #The P is Python identifier for a named capture group.
        
        


def r(rules):
    return regex.compile(r'(?(DEFINE){})^(?&r0)$'.format(''.join(defs(rules))))
    #^ indicates beginning of text
    #(?&r0)$ is showing end of line??
    #DEFINE is captureing group number? maybe?



print("part1:", sum(1 if r(rules_s).match(msg) else 0 for msg in messages_s.split('\n')))

#modify rules for part 2
rules_p2 = regex.sub(r'8: 42','8: 42 | 42 8',rules_s)
rules_p2 = regex.sub(r'11: 42 31','11: 42 31 | 42 11 31',rules_p2)

print("part2:", sum(1 if r(rules_p2).match(msg) else 0 for msg in messages_s.split('\n')))


