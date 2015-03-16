__author__ = 'santoshganti'


def rsearch(l,element):
    if element == l[0]:
        return True
    if len(l) == 0:
        return False
    return rsearch(l[1:],element)