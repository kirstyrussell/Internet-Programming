import unittest
from functools import reduce
import math
from random import uniform
from collector import Collector


class TestStatFunctions(unittest.TestCase):



    def test1(self):
        coll1 = Collector()
        coll2 = Collector()
        n = 40
        s1 = 0
        s2 = 0
        q1 = 0
        q2 = 0
        for i in range(n):
            x1 = uniform(5, 15)
            x2 = uniform(20, 30)
            coll1.add(x1)
            coll2.add(x2)
            s1 += x1
            s2 += x2
            q1 += x1 * x1
            q2 += x2 * x2
            self.assertAlmostEqual(q1, coll1.sum_squares(), 5)
            self.assertAlmostEqual(q2, coll2.sum_squares(), 5)
            self.assertAlmostEqual(s1, coll1.sum(), 5)
            self.assertEqual(i+1, coll1.count())
            self.assertAlmostEqual(s2, coll2.sum(), 5)
            self.assertEqual(i+1, coll2.count())

        self.assertAlmostEqual(math.sqrt(q1/n - s1*s1/n/n), coll1.standard_deviation(), 5)
        self.assertAlmostEqual(math.sqrt(q2/n - s2*s2/n/n), coll2.standard_deviation(), 5)
        self.assertAlmostEqual(q1/n - s1*s1/n/n, coll1.variance(), 5)
        self.assertAlmostEqual(q2/n - s2*s2/n/n, coll2.variance(), 5)
        self.assertAlmostEqual(s1 / n, coll1.average(), 5)
        self.assertAlmostEqual(s2 / n, coll2.average(), 5)


if __name__ == '__main__':
    unittest.main()