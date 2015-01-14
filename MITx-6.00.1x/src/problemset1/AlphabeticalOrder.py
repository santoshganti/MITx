'''
Created on 14-Jan-2015

@author: santoshganti
Assume s is a string of lower case characters.

Write a program that prints the longestSubstring substring of s in 
which the letters occur in alphabetical order. For example, 
if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

'''
s = 'azcbobobegghakl'
StringSlice = s[0]
longestSubstring = s[0]
for i in range(1, len(s)):
    if s[i] >= StringSlice[-1]:
        StringSlice += s[i]
        if len(StringSlice) > len(longestSubstring):
            longestSubstring = StringSlice
    else:
        StringSlice = s[i]
print 'Longest substring in alphabetical order is:', longestSubstring
