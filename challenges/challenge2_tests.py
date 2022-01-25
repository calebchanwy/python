from sys import maxsize
import unittest
import sys
from challenge2 import ReturnSmallestValueInArray


class TestChallenge2(unittest.TestCase):

    def test_returnsmalllest_shouldreturn1(self):
        self.assertEqual(ReturnSmallestValueInArray(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)

    def test_returnsmalllest_shouldreturn2(self):
        self.assertEqual(ReturnSmallestValueInArray([1, 2, -3, 4]), -3)

    def test_returnsmalllest_shouldreturn3(self):
        self.assertEqual(ReturnSmallestValueInArray(
            [-sys.maxsize-1, -sys.maxsize-1, 1, 2, -3, 4]), -sys.maxsize-1)

    def test_returnsmalllest_shouldreturn4(self):
        self.assertEqual(ReturnSmallestValueInArray([0, 0, 0, 0, 0]), 0)

    def test_returnsmalllest_shouldreturn5(self):
        self.assertEqual(ReturnSmallestValueInArray(
            [sys.maxsize]), sys.maxsize)

    def test_returnsmalllest_shouldreturn6(self):
        self.assertEqual(ReturnSmallestValueInArray([]), 0)

    def test_returnsmalllest_shouldreturn7(self):
        self.assertEqual(ReturnSmallestValueInArray(
            [sys.maxsize - 1]), sys.maxsize - 1)


if __name__ == '__main__':
    unittest.main()
