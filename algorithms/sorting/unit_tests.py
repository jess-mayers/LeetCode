import random
import unittest
##########
# config
##########
DEFAULT_LIST_SIZE = 100
MIN_VALUE = 0
MAX_VALUE = 1000

class AbstractTestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.l = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(DEFAULT_LIST_SIZE)]

    @staticmethod
    def is_sorted(l: list) -> bool:
        return all(l[i] <= l[i + 1] for i in range(len(l) - 1))

class TestQuickSort(AbstractTestSortingAlgorithms):
    def test_sort(self):
        from algorithms.sorting.quick_sort import quick_sort
        sorted_l = quick_sort(self.l)
        self.assertTrue(self.is_sorted(sorted_l))
        self.assertTrue(sorted_l == sorted(self.l))

class TestSelectionSort(AbstractTestSortingAlgorithms):
    def test_sort(self):
        from algorithms.sorting.selection_sort import selection_sort
        sorted_l = selection_sort(self.l)
        self.assertTrue(self.is_sorted(sorted_l))
        self.assertTrue(sorted_l == sorted(self.l))

class TestInsertionSort(AbstractTestSortingAlgorithms):
    def test_sort(self):
        from algorithms.sorting.insertion_sort import insertion_sort
        sorted_l = insertion_sort(self.l)
        self.assertTrue(self.is_sorted(sorted_l))
        self.assertTrue(sorted_l == sorted(self.l))

class TestBubbleSort(AbstractTestSortingAlgorithms):
    def test_sort(self):
        from algorithms.sorting.bubble_sort import bubble_sort
        sorted_l = bubble_sort(self.l)
        self.assertTrue(self.is_sorted(sorted_l))
        self.assertTrue(sorted_l == sorted(self.l))

    def test_sort_recursion(self):
        from algorithms.sorting.bubble_sort import bubble_sort_recursion
        sorted_l = bubble_sort_recursion(self.l)
        self.assertTrue(self.is_sorted(sorted_l))
        self.assertTrue(sorted_l == sorted(self.l))