__author__ = 'santoshganti'


class Location(object):
    def __init__(self, x, y):
        """
        x and y are floating point numbers
        """
        self.x = x
        self.y = y

    # function to move the farmer
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    # function to get x
    def getX(self):
        return self.x

    # function to get y
    def getY(self):
        return self.y

    # using pythagorean theorem to find the new location or you could say distance of the farmer
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5

    # A way to print the location
    def __str__(self):
        return '<'+self.x+', '+self.y+'>'


class Field(object):
    #init
    def __init__(self):
        self.drunks = {}
    #add drunk method
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate Drunk')
        else:
            self.drunks[drunk] = loc
    #move drunk method
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    #get location of the drunk
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

import random


class Drunk(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "This drunk is named "+self.name


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =  [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)