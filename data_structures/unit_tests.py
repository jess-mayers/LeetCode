import random
import unittest

from data_structures.linked_list import LinkedList
from data_structures.tree import Tree

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def generate_random_list(self, min_size: int = 10, max_size: int = 50, min_val: int = 0, max_val: int = 1000) -> list:
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


    def test_pop(self, attempts: int = 5):
        # append
        l = self.generate_random_list()
        self.append_from_list(l)
        # validate input args
        self.assertLessEqual(attempts, len(self.linked_list))

        for _ in range(attempts):
            random_idx = random.randint(0, len(self.linked_list) - 1)
            expected = l.pop(random_idx)
            result = self.linked_list.pop(random_idx)
            self.assertEqual(len(l), len(self.linked_list))
            self.assertEqual(expected, result)

    def test_get_index(self, attempts: int = 5):
        # append
        l = self.generate_random_list()
        self.append_from_list(l)
        # validate input args
        self.assertLessEqual(attempts, len(self.linked_list))
        for i in range(attempts):
            random_idx = random.randint(0, len(self.linked_list) - 1)
            node = self.linked_list.get_index(random_idx)
            self.assertEqual(l[random_idx], node.val)

    def test_remove(self, attempts: int = 5):
        # append
        l = self.generate_random_list()
        self.append_from_list(l)
        # validate input args
        self.assertLessEqual(attempts, len(self.linked_list))

        for i in range(attempts):
            random_idx = random.randint(0, len(self.linked_list) - 1)
            self.linked_list.remove(random_idx)
            self.assertEqual(len(l) - (i+1), len(self.linked_list))

class TestTree(unittest.TestCase):
    pass # TODO

