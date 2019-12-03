import unittest

from Day1.payloadFuel import calcFuel


class fuelTest(unittest.TestCase):
    def testForFuel(self):
        self.assertEqual(2, calcFuel(12))
        self.assertEqual(2, calcFuel(14))
        self.assertEqual(654, calcFuel(1969))
        self.assertEqual(33583, calcFuel(100756))
