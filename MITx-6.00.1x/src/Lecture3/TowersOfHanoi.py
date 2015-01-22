'''
Created on 22-Jan-2015

@author: santoshganti
'''

def printMove(fr,to):
    print('move from '+str(fr)+ ' to '+str(to))

def Towers(n,fr,to,spare):
    if n==1:
        printMove(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr)
        
# Towers(1, 'f', 't', 's')
# Towers(2, 'f', 't', 's')
