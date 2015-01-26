'''
Created on 22-Jan-2015

@author: santoshganti
'''

def factRec(n):
    if n == 1:
        return 1
    else:
        return n * factRec(n - 1)
    

print factRec(5)
