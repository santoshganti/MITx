'''
Created on 22-Jan-2015

@author: santoshganti
'''
def isIn(char, aStr):
   
  
    
    if aStr == '':
        return False
    mid = aStr[len(aStr) // 2]
    if char == mid:
        return True
    elif len(aStr) == 1:
        return False
    elif char < mid:
        return isIn(char, aStr[:len(aStr) // 2])
    else:
        return isIn(char, aStr[len(aStr) // 2:])
    return isIn(char, aStr)    
print isIn('a', 'Santosh')
