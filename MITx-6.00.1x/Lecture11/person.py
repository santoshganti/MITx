__author__ = 'santoshganti'

import datetime


class person(object):
    def __init__(self, name):
        """created a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """ returns slef's last name """
        return self.lastName

    def setBirthday(self, month, day, year):
        """
        sets self's birthday to birthDate
        """
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        """
        returns self's current age in days
        :return:
        """
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """
        returns true if self's name is lexicographically less than other's
        name, and False otherwise
        """
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """
        :return: self's last name

        """
        return self.name