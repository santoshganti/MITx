__author__ = 'santoshganti'


def search(L,e):
    def binarysearch(L,e,low,high):
        if high == low:
            return L[low] == e
        mid = low + int((high-low)/2)
        if L[mid] == e:
            return True
        if L[mid] > e:
            return binarysearch(L,e,low,mid)
        else:
            return binarysearch(L,e,mid+1,high)
    if len(L) == 0:
        return False
    else:
        return binarysearch(L,e,0,len(L)-1)
