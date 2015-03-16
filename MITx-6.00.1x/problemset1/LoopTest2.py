'''
Created on 10-Jan-2015

@author: santoshganti

2. Convert the following code into code that uses a for loop.

print "Hello!"
print 10
print 8
print 6
print 4
print 2

'''
print 'Hello!'
x = 10
for num in range(5):
    if x % 2 == 0 and x > 0:
            print x
            x -= 2
    
