import random
import unittest

from data_structures.linked_list import LinkedList
from data_structures.binary_tree import BinaryTree

class TestLinkedList(unittest.TestCase):
    ##########
    # Config
    ##########
    DEFAULT_MIN_SIZE = 10
    DEFAULT_MAX_SIZE = 50
    DEFAULT_MIN_VAL = 0
    DEFAULT_MAX_VAL = 1000
    DEFAULT_ATTEMPTS = 5
    def setUp(self):
        self.linked_list = LinkedList()

    @staticmethod
    def get_random_index(l: list | LinkedList) -> int:
        return random.randint(0, len(l) - 1)

    def generate_random_list(self, min_size: int = DEFAULT_MIN_SIZE,
                             max_size: int = DEFAULT_MAX_SIZE,
                             min_val: int = DEFAULT_MIN_VAL,
                             max_val: int = DEFAULT_MAX_VAL) -> list:
        # validate sizes
        self.assertLess(min_size, max_size)
        self.assertGreater(min_size, 0)
        # validate ranges
        self.assertLess(min_val, max_val)

        size = random.randint(min_size, max_size)
        return [random.randint(min_val, max_val) for _ in range(size)]

    def append_from_list(self, l: list):
        for i in l:
            self.linked_list.append(i)
        self.assertEqual(len(self.linked_list), len(l))
        self.assertEqual(self.linked_list.values, l)

    def test_append(self):
        l = self.generate_random_list()
        self.append_from_list(l)

    def test_pop(self, attempts: int = DEFAULT_ATTEMPTS):
        # append
        l = self.generate_random_list()
        self.append_from_list(l)
        # validate input args
        self.assertLessEqual(attempts, len(self.linked_list))

        for _ in range(attempts):
            random_idx = self.get_random_index(self.linked_list)
            expected = l.pop(random_idx)
            result = self.linked_list.pop(random_idx)
            self.assertEqual(len(l), len(self.linked_list))
            self.assertEqual(expected, result)

    def test_get_index(self, attempts: int = DEFAULT_ATTEMPTS):
        # append
        l = self.generate_random_list()
        self.append_from_list(l)
        # validate input args
        self.assertLessEqual(attempts, len(self.linked_list))
        for _ in range(attempts):
            random_idx = self.get_random_index(self.linked_list)
            node = self.linked_list.get_index(random_idx)
            self.assertEqual(l[random_idx], node.val)

    def test_insert(self, attempts: int = DEFAULT_ATTEMPTS):
        # append
        l = self.generate_random_list()
        self.append_from_list(l)
        # validate input args
        self.assertLessEqual(attempts, len(self.linked_list))
        for _ in range(attempts):
            random_idx = self.get_random_index(self.linked_list)
            random_int = random.randint(self.DEFAULT_MIN_VAL, self.DEFAULT_MAX_VAL)
            l.insert(random_idx, random_int)
            self.linked_list.insert(random_idx, random_int)
            self.assertEqual(l, self.linked_list.values)
            self.assertEqual(len(l), len(self.linked_list))


    def test_remove(self, attempts: int = DEFAULT_ATTEMPTS):
        # append
        l = self.generate_random_list()
        self.append_from_list(l)
        # validate input args
        self.assertLessEqual(attempts, len(self.linked_list))
        for i in range(attempts):
            random_idx = self.get_random_index(self.linked_list)
            self.linked_list.remove(random_idx)
            self.assertEqual(len(l) - (i+1), len(self.linked_list))

class TestTree(unittest.TestCase):
    pass # TODO

