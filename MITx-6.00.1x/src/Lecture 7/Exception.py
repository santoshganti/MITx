__author__ = 'Santosh'
def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError, e:
        print "Division by Zero!" +str(e)
    except TypeError:
        divide(int(x),int(y))
    else:
        print "Result is ", result
    finally:
        print "executing finally clause"

divide('3','3')