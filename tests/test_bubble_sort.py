import unittest

from algorithms import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort_positive_numbers(self):
        self.assertEqual(bubble_sort.bubble_sort([19, 20, 13, 1, 15]), [1,
                                                                        13,
                                                                        15,
                                                                        19,
                                                                        20])

    def test_bubble_sort_negative_numbers(self):
        self.assertEqual(bubble_sort.bubble_sort([-1, -3, -5, -7, -9, -5]),
                         [-9, -7, -5, -5, -3, -1])

    def test_bubble_sort_same_numbers(self):
        self.assertEqual(bubble_sort.bubble_sort([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_bubble_sort_empty_list(self):
        self.assertEqual(bubble_sort.bubble_sort([]), [])

    def test_bubble_sort_already_sorted(self):
        self.assertEqual(bubble_sort.bubble_sort([1, 2, 3, 4]), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
