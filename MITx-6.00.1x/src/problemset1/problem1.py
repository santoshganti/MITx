'''
Created on 10-Jan-2015

@author: santoshganti

1. Convert the following into code that uses a while loop.

print 2
print 4
print 6
print 8
print 10
print Goodbye!
'''
limit = 10
x = 2
while x<=limit:
    if x%2==0:
        print x
        x+=2
print "Goodbye!"    
        