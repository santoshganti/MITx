'''
Created on 13-Jan-2015

@author: santoshganti
'''
epsilon = 0.01
y = 24.0
guess = y / 2.0

while abs(guess * guess - y) >= epsilon:
    guess = guess - (((guess ** 2) - y) / (2 * guess))
    print(guess)
print('Square root of ' + str(y) + ' is about ' + str(guess))
