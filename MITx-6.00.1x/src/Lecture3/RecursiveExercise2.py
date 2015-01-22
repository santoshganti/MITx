'''
Created on 22-Jan-2015

@author: santoshganti
'''
def isitIn(char, aStr):
    if aStr == '':  # Check for empty string
        return False
    m = aStr[len(aStr) // 2]
    if char == m:
        return True
    elif len(aStr) == 1:
        return False
    else:
        if char < m:
            return isitIn(char, aStr[:len(aStr) // 2])
        elif char > m:
            return isitIn(char, aStr[len(aStr) // 2:])
    return isitIn(char, aStr)

print isitIn('a','santosh')