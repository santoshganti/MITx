__author__ = 'santoshganti'

import random

class intDict(object):
    def __init__(self, numBuckets):
        """
        Creates an empty dictionary
        :param numBuckets:
        :return:
        """
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])

    def addEntry(self, dictKey, dictVal):
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == dictKey:
                hashBucket[i] = (dictKey, dictVal)
                return
        hashBucket.append((dictKey, dictVal))


    def getVal(self, dictKey):
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
            return None

    def __str__(self):
        res = "{"
        for b in self.buckets:
            for t in b:
                res = res + str(t[0])+":"+str(t[1])+","
            return res[:-1]+"}"

D = intDict(29)
for i in range(20):
    #choose a random int in range(10**5)
    key = random.choice(range(10**5))
    D.addEntry(key, i)

print '\n', 'The buckets are:'
for hashBucket in D.buckets: #violates abstraction barrier
    print '  ', hashBucket

