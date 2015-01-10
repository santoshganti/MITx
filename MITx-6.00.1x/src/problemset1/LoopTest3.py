'''
Created on 10-Jan-2015

@author: santoshganti

3. Write a while loop that sums the values 1 through end, inclusive. 
end is a variable that we define for you. So, for example, if we define 
end to be 6, your code should print out the result

'''
end = 6

for num in reversed(range(end)):
        end = end+num
        
print end
        