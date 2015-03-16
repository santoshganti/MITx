'''
Created on 14-Jan-2015

@author: santoshganti
'''
def findRoot1(x, power, epsilon):
    low = 0
    high = x
    ans = (high + low) / 2.0
    while abs(ans ** power) - x > epsilon:
        if ans ** power < epsilon:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans

print findRoot1(25.0, 2, .001)
print findRoot1(27.0, 3, .001)
# print findRoot1(-27.0, 3, .001)
# so can't find cube root of negative number
        
