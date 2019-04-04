

import unittest
from functools import reduce
import math
from random import uniform
from collector import Collector


class TestStatFunctions(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.__init__(self)
        self.data = []
        for i in range(40):
            self.data.append(uniform(-8, 10))
        # self.data = [2, 3, 4, 5, 6]
        self.count = len(self.data)
        self.sum = reduce(lambda x, y: x + y, self.data)
        self.sumsq = reduce(lambda x, y: x + y*y, self.data, 0)
        self.avg = self.sum/len(self.data)
        self.var = self.sumsq / self.count - self.avg * self.avg
        self.stdev = math.sqrt(self.var)

    def test1(self):
        coll = Collector()
        for x in self.data:
            coll.add(x)
        self.assertAlmostEqual(self.stdev, coll.standard_deviation())
        self.assertAlmostEqual(self.var, coll.variance(), 5)
        self.assertAlmostEqual(self.avg, coll.average(), 5)
        self.assertAlmostEqual(self.sumsq, coll.sum_squares(), 5)
        self.assertAlmostEqual(self.sum, coll.sum(), 5)
        self.assertEqual(self.count, coll.count())


if __name__ == '__main__':
    unittest.main()