import unittest

from algorithms import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort_same_numbers(self):
        self.assertEqual(insertion_sort.insertion_sort([1, 1, 1, 1]), [1, 1,
                                                                       1, 1])

    def test_insertion_sort_empty_list(self):
        self.assertEqual(insertion_sort.insertion_sort([]), [])

    def test_insertion_sort_already_sorted(self):
        self.assertEqual(insertion_sort.insertion_sort([1, 2, 3, 4]), [1, 2, 3,
                                                                       4])


if __name__ == '__main__':
    unittest.main()
