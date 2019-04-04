#  Kirsty Russell
#  CS 4720
#  Assignment 1 Test
#  Professor Setzer
#  January 22, 2019

import collector as col

a = col.Collector()
a.add(1)
a.add(5)
a.add(6)
a.add(10)
a.add(20)
print("Sum:                 ", a.sum())
print("Count:               ", a.count())
print("Sum of Squares:      ", a.sum_squares())
print("Average:             ", a.average())
print("Variance:            ", a.variance())
print("Standard Deviation:  ", a.standard_deviation())
