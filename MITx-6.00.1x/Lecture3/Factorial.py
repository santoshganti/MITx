'''
Created on 22-Jan-2015

@author: santoshganti
'''
def fact(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result

print fact(5)
