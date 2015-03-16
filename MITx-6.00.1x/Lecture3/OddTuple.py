'''
Created on 24-Jan-2015

@author: santoshganti
'''
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    return aTup[0:len(aTup):2]

print oddTuples((13, 5, 0, 3, 6, 10, 0, 14, 12, 19))
print oddTuples((15, 9, 0, 18, 1, 2, 12, 8))
