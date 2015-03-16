'''
Created on 14-Jan-2015

@author: santoshganti
'''
print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = (raw_input("Enter a word:"))
if (len(original) > 0) and original.isalpha():
    print 'You have entered: ' + original
else:
    print "empty"
