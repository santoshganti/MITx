'''
Created on 18-Jan-2015

@author: santoshganti
'''
balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month = 1
totalPaid = 0
while month < 13:
    print "Month: " + str(month)
    print "Minimum monthly payment: " + str(round(balance*monthlyPaymentRate, 2))
    totalPaid+= (balance*monthlyPaymentRate)
    balance = (balance - (balance*monthlyPaymentRate))*(1+(annualInterestRate/12))
    print "Remaining balance: " + str(round(balance, 2))
    month += 1
    if(month == 13):
        print "Total Paid:" +str(round(totalPaid,2))
        print "Remaining balance: "+str(round(balance,2))