'''
Created on 13-Jan-2015

@author: santoshganti
'''
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    #z = ((a*(x**2)) + (b*x) + c)
    return ((a*(x**2)) + (b*x) + c)

print evalQuadratic(1,2,3,4)