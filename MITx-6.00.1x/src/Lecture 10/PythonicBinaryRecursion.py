__author__ = 'santoshganti'


def rBinarySearch(l,e):
    if len(l) == 1:
        return e == l[0]
    mid = len(l)/2

    if l[mid] > e:
        return rBinarySearch(l[:mid],e)
    if l[mid] < e:
        return rBinarySearch(l[mid:],e)
    return True
