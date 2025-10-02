import random
import unittest

# TODO
from data_structures.linked_list import LinkedList



class TestLinkedList(unittest.TestCase):
    RANDOM_MIN_VALUE = 0
    RANDOM_MAX_VALUE = 1000
    def setUp(self):
        self.linked_list = LinkedList()

    def test_append(self, min_appends: int = 10, max_appends: int = 50):
        self.assertLess(min_appends, max_appends)
        self.assertGreater(min_appends, 0)
        num_appends = random.randint(min_appends, max_appends)
        print(f'Appending {num_appends} random values between {self.RANDOM_MIN_VALUE} and {self.RANDOM_MAX_VALUE}')
        for i in range(num_appends):
            self.linked_list.append(random.randint(self.RANDOM_MIN_VALUE, self.RANDOM_MAX_VALUE))
        self.assertEqual(num_appends, len(self.linked_list))

    def test_index(self):
        self.test_append()
        values = self.linked_list.values
        random_index = random.randint(0, len(self.linked_list) - 1)
        x=1



