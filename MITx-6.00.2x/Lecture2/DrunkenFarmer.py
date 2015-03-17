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