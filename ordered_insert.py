"""This script demonstrates the ordered insert algorithm in Python 3."""

import bisect

AGES = [1, 3, 7, 10, 11]


def ordered_insert():
    """Insert item into a list, and keep it sorted assuming the list is
    already sorted. If the item is already in the list, insert it to the
    right of the rightmost item.
    """
    count = int(input("How many ages do you want to enter? "))
    for i in range(count):
        x = int(input("Enter an age: "))
        bisect.insort(AGES, x)


if __name__ == '__main__':
    print("The original list is : " + str(AGES))
    ordered_insert()
    print("The list after insertion is : " + str(AGES))
