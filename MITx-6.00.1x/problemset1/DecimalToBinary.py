'''
Created on 11-Jan-2015

@author: santoshganti

Program to convert decimal into binary
'''
num = -256
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
        result = str(num % 2) + result 
        num = num / 2 
if isNeg:
        result = '-' + result
print result
        
