'''
Created on 13-Jan-2015

@author: santoshganti
'''
# From Lecture 4, How Environments Separate Variable Bindings

def square(x):
    return x*x

def twoPower(x,n):
    while n > 1:
        x = square(x)
        n = n/2
    return x

print twoPower(2,4)