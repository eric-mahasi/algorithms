"""This script demonstrates the bubble sort algorithm in Python 3."""

AGES = [19, 20, 13, 1, 15, 7, 11, 3, 16, 10]


def display():
    """Prints all the items in the list."""
    print("The ages are: ")
    for i in range(len(AGES)):
        print(AGES[i])
    print("\n")


def bubble_sort():
    """Repeatedly step through the list, compare adjacent items and swap
    them if they are in the wrong order. Time complexity of O(n^2).
    """
    for i in range(len(AGES) - 1):
        for j in range(len(AGES) - 1 - i):
            if AGES[j] > AGES[j + 1]:
                AGES[j], AGES[j + 1] = AGES[j + 1], AGES[j]


if __name__ == '__main__':
    display()
    bubble_sort()
    display()
