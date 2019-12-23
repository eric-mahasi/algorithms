"""This script demonstrates the insertion sort algorithm in Python 3."""

AGES = [19, 20, 13, 1, 15, 7, 11, 3, 16, 10]


def display():
    """Prints all the items in the list."""
    print("The ages are: ")
    for i in range(len(AGES)):
        print(AGES[i])
    print("\n")


def insertion_sort(array):
    """Build the final sorted list one item at a time. Time complexity of
    O(n^2).

    Parameters
    ----------
    array : iterable
        A list of unsorted numbers
    Returns
    -------
    array : iterable
        A list of sorted numbers
    """
    for i in range(len(AGES)):
        temp = AGES[i]
        j = i
        while j > 0 and AGES[j - 1] >= temp:
            AGES[j] = AGES[j - 1]
            j = j - 1
        AGES[j] = temp

    return array


if __name__ == '__main__':
    display()
    insertion_sort(AGES)
    display()
