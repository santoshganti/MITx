'''
Created on 12-Jan-2015

@author: santoshganti
'''
x = 9
epsilon = 0.1
numGuesses = 0
low = 0.0
high = x
ans = (high + low) / 2.0
while abs(ans ** 2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))