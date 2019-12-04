import unittest

from Day2.opCodeComputer import handle_intcode


class opCodeTest(unittest.TestCase):
    def testForOpCode(self):
        self.assertEqual(2, handle_intcode(0, [1, 0, 0, 0, 99]))

    def testForOpCode2(self):
        self.assertEqual(2, handle_intcode(0, [2, 3, 0, 3, 99]))

    def testForOpCode3(self):
        self.assertEqual(30, handle_intcode(0, [1, 1, 1, 4, 99, 5, 6, 0, 99]))
