__author__ = 'Santosh'


def getRations(v1, v2):
    '''
    Assuems: v1 and v2 are lists of equal length of numbers
    Returns a list containing meaningful values of
    v1[i]/v2[i]
    '''

    ratios = []
    for index in range(len(v1)):
        try:
            ratios.append(v1[index] / float(v2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))  # NaN = Not a Number
        except:
            raise ValueError('getRatios called with bad arg')
    return ratios
