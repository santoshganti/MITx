'''
Created on 22-Jan-2015

@author: santoshganti
'''
def fibonacci(x):
    if x==0 or x==1:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)
    
print fibonacci(5)