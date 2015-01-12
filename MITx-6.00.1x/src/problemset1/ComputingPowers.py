'''
Created on 13-Jan-2015

@author: santoshganti
'''
x = float(raw_input('Input a number: '))
p = int(raw_input('Enter an integer power'))
result = 1
for turn in range(p):
    print('iteration' + str(turn) + 'current result' + str(result))
result = result * x
