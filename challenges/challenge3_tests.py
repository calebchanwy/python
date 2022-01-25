import datetime
import unittest

from challenge3 import CalculateBestBranch, SalesItem


class TestChallenge3(unittest.TestCase):

    def test_calculatebestbranch_shouldreturncorrectvalue1(self):
        self.assertEqual(CalculateBestBranch([
            SalesItem("ABC", 100, datetime.date.today()),
            SalesItem("ABC", 50, datetime.date.today() +
                      datetime.timedelta(days=-1)),
            SalesItem("ABC", 400, datetime.date.today() +
                      datetime.timedelta(days=-2)),
            SalesItem("DEF", 200, datetime.date.today())
        ]), "ABC")

    def test_calculatebestbranch_shouldreturncorrectvalue2(self):
        self.assertEqual(CalculateBestBranch([
            SalesItem("ABC", 100, datetime.date.today()),
            SalesItem("ABC", 50, datetime.date.today() +
                      datetime.timedelta(days=-1)),
            SalesItem("ABC", 200, datetime.date.today() +
                      datetime.timedelta(days=-2)),
            SalesItem("DEF", 500, datetime.date.today())
        ]), "DEF")


if __name__ == '__main__':
    unittest.main()
