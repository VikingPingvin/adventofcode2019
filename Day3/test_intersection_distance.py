import unittest
from Day3.intersection_distance import is_intersect_result_tuple

class distance_test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(1, 1)

        
    def test_example2(self):
        self.assertEqual(1, 1)

class core_test(unittest.TestCase):
    def test_is_tuple_with_tuple(self):
        self.assertEqual(True, is_intersect_result_tuple((1, 2)))

    def test_is_tuple_with_not_tuple(self):
        self.assertEqual(False, is_intersect_result_tuple('awsed'))