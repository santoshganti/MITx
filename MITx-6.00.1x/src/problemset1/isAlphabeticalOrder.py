'''
Created on 14-Jan-2015

@author: santoshganti
'''
def isInAlphabeticalOrder(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True

print isInAlphabeticalOrder('abcd')
