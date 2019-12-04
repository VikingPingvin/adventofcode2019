import unittest

from Day1.payloadFuel_extended import calcExtendedFuel


class fuelTest_extented(unittest.TestCase):
    def testForFuel(self):
        self.assertEqual(2, calcExtendedFuel(14))
        self.assertEqual(966, calcExtendedFuel(1969))
        self.assertEqual(50346, calcExtendedFuel(100756))

