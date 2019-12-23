"""This script demonstrates the bubble sort algorithm in Python 3."""

AGES = [19, 20, 13, 1, 15, 7, 11, 3, 16, 10]


def display():
    """Prints all the items in the list."""
    print("The ages are: ")
    for i in range(len(AGES)):
        print(AGES[i])
    print("\n")


def bubble_sort(array):
    """Repeatedly step through the list, compare adjacent items and swap
    them if they are in the wrong order. Time complexity of O(n^2).

    Parameters
    ----------
    array : iterable
        A list of unsorted numbers
    Returns
    -------
    array : iterable
        A list of sorted numbers
    """
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    display()
    bubble_sort(AGES)
    display()
