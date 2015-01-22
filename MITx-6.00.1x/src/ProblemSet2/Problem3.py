'''
Created on 18-Jan-2015

@author: santoshganti
'''
balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12
lowerBound = balance / 12
upperBound = (balance * (1 + annualInterestRate / 12) ** 12) / 12
originalBalance = balance
lowestBalance = 0.01 # Error margin e.g. $0.01

# Keep testing new payment values until the balance is +/- lowestBalance
while abs(balance) > lowestBalance:
    # Reset the value of balance to its original value
    balance = originalBalance
    # Calculate a new monthly payment value from the bounds
    payment = (upperBound - lowerBound) / 2 + lowerBound

    # Test if this payment value is sufficient to pay off the entire balance in 12 months
    for month in range(12):
        balance -= payment
        balance *= 1 + monthlyInterestRate

    # Reset bounds based on the final value of balance
    if balance > 0:
        # If the balance is too big, need higher payment so we increase the lower bound
        lowerBound = payment
    else:
        # If the balance is too small, we need a lower payment, so we decrease the upper bound
        upperBound = payment

# When the while loop terminates, we know we have our answer!
print "Lowest Payment:", round(payment, 2)