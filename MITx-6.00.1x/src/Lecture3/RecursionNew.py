'''
Created on 22-Jan-2015

@author: santoshganti

'''
def recurPowerNew(base,exp):
    if exp<=0:
        return 1
    elif (exp%2==0):
        return recurPowerNew(base*base, exp/2) 
    else:
        return base*recurPowerNew(base, exp-1)

print recurPowerNew(2, 2)
print recurPowerNew(2, 3)
print recurPowerNew(-2.88, 5)