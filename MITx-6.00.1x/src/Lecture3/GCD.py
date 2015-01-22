'''
Created on 22-Jan-2015

@author: santoshganti
'''
def gcd(a, b):
    if a > b:
        test = b
    else:
        test = a
    for i in range(1,test + 1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i

    return gcd

print gcd(2, 12)