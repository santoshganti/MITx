'''
Created on 14-Jan-2015

@author: santoshganti

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2

'''
s = 'obooubyobnoboboottobobobobobvobobgobob'
bob=0
for x,element in enumerate(s):
    if s[x:x+3] == 'bob':
        bob+=1
 
print "Number of times bob occurs is: " +str(bob)


