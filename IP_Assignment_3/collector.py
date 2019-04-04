#  Kirsty Russell
#  CS 4720
#  Assignment 3
#  Professor Setzer
#  February 12, 2019


class Collector:
    def __init__(self):
            self.list = []

    """Add the value x to the collection"""
    def add(self, x):
        self.list.append(float(x))

    """Return the number of values collected so far"""
    def count(self):
        return len(self.list)

    """Return the sum of the values collected so far"""
    def sum(self):
        return sum(self.list)

    """Return the sum of the squares of the values collected so far"""
    def sum_squares(self):
        square = 0
        for x in self.list:
            square += (x ** 2)
        return square

    """Return the average of the values collected so far"""
    def average(self):
        return self.sum() / len(self.list)

    """Return the variance of the values collected so far"""
    def variance(self):
        var = 0
        for x in self.list:
            var += (x - self.average()) ** 2
        return var / self.count()

    """Return the standard deviation of the values collected so far"""
    def standard_deviation(self):
        return (self.variance()) ** 0.5
