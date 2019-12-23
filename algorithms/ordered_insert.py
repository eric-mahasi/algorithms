"""This script demonstrates the ordered insert algorithm in Python 3."""

import bisect

AGES = []


def ordered_insert(array):
    """Insert item into a list, and keep it sorted assuming the list is
    already sorted. If the item is already in the list, insert it to the
    right of the rightmost item.

    Parameters
    ----------
    array : iterable
        A list of unsorted number
    """
    count = int(input("How many ages do you want to enter? "))
    for i in range(count):
        x = int(input("Enter an age: "))
        bisect.insort(array, x)

    return array


if __name__ == '__main__':
    print("The original list is : " + str(AGES))
    print(ordered_insert(AGES))
    print("The list after insertion is : " + str(AGES))
