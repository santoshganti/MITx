'''
Created on 22-Jan-2015

@author: santoshganti
'''
def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    length = 0
    for i in aStr:
        length+=1
    return length
    
print lenIter('hello')