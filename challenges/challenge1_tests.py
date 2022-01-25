from challenges.challenge1 import (Add_Tax, Buy_One_Get_One_Half_Price,
                                   Calculate_Total_Cost, Discount)
import sys
import unittest


class TestChallenge1(unittest.TestCase):

    def test_addtax_shouldCalculate1(self):
        self.assertEqual(Add_Tax(10, 0.5), 15)

    def test_addtax_shouldCalculate2(self):
        self.assertEqual(Add_Tax((sys.maxsize - 1) / 2, 1), sys.maxsize - 1)

    def test_addtax_shouldCalculate3(self):
        self.assertEqual(Add_Tax(1, 0), 1)

    def test_addtax_shouldCalculate4(self):
        self.assertEqual(Add_Tax(0, 1), 0)

    def test_discount_shouldcalculate1(self):
        self.assertEqual(Discount(10, 0.2), 8)

    def test_discount_shouldcalculate2(self):
        self.assertEqual(Discount(78, 0.4), 46.8)

    def test_discount_shouldcalculate3(self):
        self.assertEqual(Discount(100, 1,), -1)

    def test_discount_shouldcalculate4(self):
        self.assertEqual(Discount(100, 2,), -1)

    def test_discount_shouldcalculate5(self):
        self.assertEqual(Discount(100, -1), -1)

    def test_bogof_shouldcalculate1(self):
        self.assertEqual(Buy_One_Get_One_Half_Price(10, 10), 15)

    def test_bogof_shouldcalculate2(self):
        self.assertEqual(Buy_One_Get_One_Half_Price(10, 20), 25)

    def test_bogof_shouldcalculate3(self):
        self.assertEqual(Buy_One_Get_One_Half_Price(20, 10), 25)

    def test_totalcost_shouldcalculate1(self):
        self.assertEqual(Calculate_Total_Cost([1, 2, 3, 4, 5]), 15)

    def test_totalcost_shouldcalculate2(self):
        self.assertEqual(Calculate_Total_Cost([10, 20, 30, 40, 50]),  150)

    def test_totalcost_shouldcalculate3(self):
        self.assertEqual(Calculate_Total_Cost([-1, -2, -3, -4, -5]),  -15)

    def test_totalcost_shouldcalculate4(self):
        self.assertEqual(Calculate_Total_Cost([-1, -2, -3, -4, 5]),  -5)


if __name__ == '__main__':
    unittest.main()
