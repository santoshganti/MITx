'''
Created on 14-Jan-2015

@author: santoshganti
'''
s='azcbobobegghakl'
def alphabetical_substring(s):
    substring = {}
    max_value = 0

    for i in range(len(s)):
        count = 0
        sub_value  = s[i]

        while i+1 < len(s) and s[i] <= s[i+1]:
            count += 1
            i += 1
            sub_value += s[i]

        substring[count] = substring.get(count, sub_value)
        max_value = max(substring.keys())
    
    return substring[max_value]

print 'Longest substring in alphabetical order is:', alphabetical_substring(s)