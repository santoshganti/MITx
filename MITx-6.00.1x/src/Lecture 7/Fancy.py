__author__ = 'Santosh'


def FancyDivide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception, e:
        print e

# FancyDivide([0, 2, 4], 1)
#FancyDivide([0, 2, 4], 4)
FancyDivide([0, 2, 4], 0)