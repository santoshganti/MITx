'''
Created on 14-Jan-2015

@author: santoshganti
'''
def findRoot2(x, power, epsilon):
    if x < 0 and power % 2 == 0:
        return str('Cannot find root of negative number')
    low = min(0, x)
    high = max(0, x)
    ans = (high + low) / 2.0
    while abs(ans ** power - x) > epsilon:
        if ans ** power < x:
            low = ans 
        else:
            high = ans 
        ans = (low + high) / 2.0
    return ans
