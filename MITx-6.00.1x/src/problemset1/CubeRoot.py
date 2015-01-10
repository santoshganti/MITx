'''
Created on 10-Jan-2015

@author: santoshganti

Find the cube root of perfect cube
'''
x = int(raw_input('Enter an integer:'))
ans = 0
while ans ** 3 < x:
    ans = ans + 1
if ans ** 3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))
