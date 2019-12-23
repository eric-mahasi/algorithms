import unittest

from algorithms import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        array = [1, 3, 7, 10, 11]
        self.assertEqual(binary_search.binary_search([1, 2, 4], 3), -1)
        self.assertEqual(binary_search.binary_search(array, 3), 0)
        self.assertEqual(binary_search.binary_search(array, 5), -1)
        self.assertEqual(binary_search.binary_search([15, 16, 19, 20], 20),
                         0)
        self.assertEqual(binary_search.binary_search([16, 19, 20, 15], 15),
                         -1)


if __name__ == '__main__':
    unittest.main()
