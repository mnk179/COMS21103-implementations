import unittest
from Order_Statistics import *

class RandomisedSelectTestCase(unittest.TestCase):

    def setUp(self):
        self.listA = [3, 8, 1, 7, 4, 6, 2, 5, 9] # example by MM
        self.listB = [i + 1 for i in range(10)]
        self.listC = [5, 2, 9, 1, 10, 3, 4, 6, 8, 7]

    def test6thInA(self):
        self.assertEqual(randomisedSelect(self.listA, 0, len(self.listA) - 1, 6), 6, "found order statistic incorrectly")

    def test8thInB(self):
        self.assertEqual(randomisedSelect(self.listB, 0, len(self.listB) - 1, 8), 8, "found order statistic incorrectly")

    def test2ndInC(self):
        self.assertEqual(randomisedSelect(self.listC, 0, len(self.listC) - 1, 2), 2, "found order statistic incorrectly")

if __name__ == "__main__":
    unittest.main()
