low = 0
high = 100
ans = (low + high) / 2
print ("Please think of a number between 0 and 100!")
print ("Is your secret number " + str(ans) + " ?")
while True:
    print "Enter 'h' to indicate the guess is too high.",
    print "Enter 'l' to indicate the guess is too low.",
    userInput = str(raw_input ("Enter 'c' to indicate I guessed correctly."))
 
    if userInput == 'l':
        low = ans
        ans = (low + high) / 2
        print ("Is your secret number " + str(ans) + " ?")
        
    elif userInput == 'h':
        high = ans
        ans = (low + high) / 2
        print ("Is your secret number " + str(ans) + " ?")

    elif userInput == 'c':
        print ("Game over. Your secret number was: " + str(ans))
        break
    else:
        print ("Sorry, I did not understand your input.")
        print ("Is your secret number " + str(ans) + " ?")

    
        
        
    
