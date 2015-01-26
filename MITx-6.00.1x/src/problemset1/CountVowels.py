'''
Created on 14-Jan-2015

@author: santoshganti

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
'''
s = 'arwrulenpoauyacmm'
countA = s.lower().count('a') + s.lower().count('e') + s.lower().count('i') + s.lower().count('o') + s.lower().count('u')
print "Number of vowels: " + str(countA)
