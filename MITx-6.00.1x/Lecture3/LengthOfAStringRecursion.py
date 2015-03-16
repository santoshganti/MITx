'''
Created on 22-Jan-2015

@author: santoshganti
'''
def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    
    if aStr == '':
        return 0
    else:
        return lenRecur(aStr[1:]) + 1
    
print lenRecur('Hello') 
