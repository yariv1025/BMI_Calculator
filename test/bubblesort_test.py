import unittest
from src.bubble_sort import *


class MyTestCase(unittest.TestCase):

    def test_return_value(self):
        self.assertEqual(bubble_sort(None), not None)

    def test_no_lost_values(self):
        stub = [3, 1, 2, 5, 4]
        ex_result = 5
        self.assertEqual(len(bubble_sort(stub)), ex_result)

    def test_list_sort(self):
        stub = [3, 1, 2, 5, 4]
        ex_result = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(stub), ex_result)

    def test_sort_sorted_list(self):
        stub = [1, 2, 3, 4, 5]
        ex_result = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(stub), ex_result)

    def test_sort_empty_list(self):
        stub = []
        ex_result = []
        self.assertEqual(bubble_sort(stub), ex_result)


if __name__ == '__main__':
    unittest.main()
