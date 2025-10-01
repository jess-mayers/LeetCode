import random
import unittest

from algorithms.utils import is_sorted
##########
# config
##########
DEFAULT_LIST_SIZE = 100
MIN_VALUE = 0
MAX_VALUE = 1000

class AbstractTestSearchAlgorithms(unittest.TestCase):
    def setUp(self):
        assert MAX_VALUE - MIN_VALUE >= DEFAULT_LIST_SIZE
        # unique random numbers
        self.l = random.sample(range(MIN_VALUE, MAX_VALUE), DEFAULT_LIST_SIZE)

    @staticmethod
    def get_random_index_and_value(l: list) -> tuple:
        i = random.randint(0, len(l))
        return i, l[i]

class TestBinarySearch(AbstractTestSearchAlgorithms):
    def setUp(self):
        super().setUp()
        # ensure list is sorted
        self.l.sort()

    def test_search(self):
        from algorithms.search.binary_search import binary_search
        idx, value = self.get_random_index_and_value(self.l)
        result_idx = binary_search(self.l, value)
        self.assertGreater(result_idx, 0)
        self.assertEqual(idx, result_idx)
        self.assertEqual(self.l[idx], self.l[result_idx])

    def test_search_recursion(self):
        from algorithms.search.binary_search import binary_search_recursion
        idx, value = self.get_random_index_and_value(self.l)
        result_idx = binary_search_recursion(self.l, value)
        self.assertGreater(result_idx, 0)
        self.assertEqual(idx, result_idx)
        self.assertEqual(self.l[idx], self.l[result_idx])

class TestLinearSearch(AbstractTestSearchAlgorithms):
    def test_search(self):
        from algorithms.search.linear_search import linear_search
        idx, value = self.get_random_index_and_value(self.l)
        result_idx = linear_search(self.l, value)
        self.assertGreater(result_idx, 0)
        self.assertEqual(idx, result_idx)
        self.assertEqual(self.l[idx], self.l[result_idx])
