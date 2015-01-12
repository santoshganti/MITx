'''
Created on 13-Jan-2015

@author: santoshganti
'''
def iterativePower(x, p):
    result = 1
    for turn in range(p):
        print ('iteration: ' + str(turn) + ' current result: ' + str(result))
        result = result * x
    return result

print iterativePower(3, 5)