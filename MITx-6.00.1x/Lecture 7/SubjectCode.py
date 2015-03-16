__author__ = 'Santosh'


def getSubjectState(subject, weights):
    return [[elt[0], elt[1], avg(elt[1], weights)] for elt in subject]


def dotProduct(a, b):
    result = 0.0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

def ag(grades, weights):
    try:
        return dotProduct(grades, weights)/len(grades)
    except ZeroDivisionError:
        print 'no grades data'
        return 0.0
