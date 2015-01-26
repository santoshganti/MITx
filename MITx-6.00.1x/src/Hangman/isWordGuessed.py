'''
Created on 25-Jan-2015

@author: santoshganti
'''
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE..
#     for c in secretWord:
#         matched = [l for l in lettersGuessed if c == l]
#         if len(matched) == 0:
#             return False
#         
#     return True
    
    for c in secretWord:
            match = []
            for l in lettersGuessed:
                if c == l:
                    match.append(l)
    print match            
    if len(match) == 0:
        return False
    else:
        return True

print isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])
# print isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])
# print isWordGuessed('grapefruit', ['l', 'm', 'b', 'y', 'u', 'i', 'a', 'e', 'j', 'o'])
# print isWordGuessed('carrot', [])
# print isWordGuessed('lettuce', ['z', 'x', 'q', 'l', 'e', 't', 't', 'u', 'c', 'e'])
    
