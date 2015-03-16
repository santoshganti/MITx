'''
Created on 13-Jan-2015

@author: santoshganti
'''
def f(x):
    y = 1
    x = x + y
    print('x= ' + str(x))
    return x

x = 3
y = 2
z = f(x)
print ('z= ' + str(z))
print ('y=' + str(y))
print ('z= ' + str(z))
