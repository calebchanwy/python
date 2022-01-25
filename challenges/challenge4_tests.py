import math
import unittest

from challenge4 import StampDuty


class TestChallenge4(unittest.TestCase):

    def test_stampouty_shouldcalculate1(self):
        self.assertEqual(StampDuty(125000), 0)

    def test_stampouty_shouldcalculate2(self):
        self.assertEqual(StampDuty(300000), 0)

    def test_stampouty_shouldcalculate3(self):
        self.assertEqual(StampDuty(300001), round(1 * 0.05, 0))

    def test_stampouty_shouldcalculate4(self):
        self.assertEqual(StampDuty(500000), round(
            (500000-300001) * 0.05, 0))

    def test_stampouty_shouldcalculate5(self):
        self.assertEqual(StampDuty(925000), round(
            (925000-300001) * 0.05, 0))

    def test_stampouty_shouldcalculate6(self):
        self.assertEqual(StampDuty(925001), round(
            (925000-300001) * 0.05, 0))

    def test_stampouty_shouldcalculate7(self):
        self.assertEqual(StampDuty(1500000), round(
            (574999 * 0.1) + ((925000-300001) * 0.05), 0))

    def test_stampouty_shouldcalculate8(self):
        self.assertEqual(StampDuty(2500000), round(
            ((2500000 - 1500001) * 0.12) + (574999 * 0.1) + ((925000-300001) * 0.05), 0))

    def test_stampouty_shouldcalculate9(self):
        self.assertEqual(StampDuty(1595000), 100150)


if __name__ == '__main__':
    unittest.main()
