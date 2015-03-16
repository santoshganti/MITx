'''
Created on 14-Jan-2015

@author: santoshganti
'''
def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    y = char.lower()
    x = y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u'
    return x

def isVowel2(char):
    x = char.lower()
    return x in ('aeiou')




# print isVowel('a')
# print isVowel('b')
# print isVowel('A')
# print isVowel('B')

print isVowel2('a')
print isVowel2('b')
print isVowel2('A')
print isVowel2('B')
