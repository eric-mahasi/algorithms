"""This script demonstrates the binary search algorithm in Python 3."""

AGES = [1, 3, 7, 10, 11, 13, 15, 16, 19, 20]


def display():
    """Prints all the items in the list."""
    print("The ages are: ")
    for i in range(len(AGES)):
        print(AGES[i])


def binary_search(array, x):
    """Find the position of a target value, x, in a sorted array. Time
    complexity of O(log n).

    Parameters
    ----------
    array : iterable
        A list of sorted numbers
    x : int
        The number to be searched for
    """
    lower_bound = 0
    upper_bound = len(array) - 1
    while True:
        mid = int((lower_bound + upper_bound) / 2)
        if x == array[mid]:
            print("A student aged", x, "was found.")
            return 0
        elif lower_bound > upper_bound:
            print("A student aged", x, "was not found.")
            return -1
        else:
            if x < array[mid]:
                upper_bound = mid - 1
            else:
                lower_bound = mid + 1


if __name__ == '__main__':
    display()
    search_key = int(input("Enter an age to search for: "))
    binary_search(AGES, search_key)
