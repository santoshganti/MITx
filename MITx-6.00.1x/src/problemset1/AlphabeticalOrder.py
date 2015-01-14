'''
Created on 14-Jan-2015

@author: santoshganti
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in 
which the letters occur in alphabetical order. For example, 
if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

'''
def isInAlphabeticalOrder(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True

print isInAlphabeticalOrder('abcd')
