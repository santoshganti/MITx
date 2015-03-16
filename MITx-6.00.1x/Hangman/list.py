'''
Created on 25-Jan-2015

@author: santoshganti
'''
letters = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']
secretWord = 'apple'
def convertString(secretWord):
    string1 = []
    
    for i in secretWord:
        string1 += i
    return string1
convertString('apple')
