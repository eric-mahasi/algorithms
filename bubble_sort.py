"""This script demonstrates the bubble sort algorithm in Python 3."""

ages = [19, 20, 13, 1, 15, 7, 11, 3, 16, 10]


def display():
    """Prints all the items in the list."""
    print("The ages are: ")
    for i in range(len(ages)):
        print(ages[i])
    print("\n")


def bubble_sort():
    """Repeatedly step through the list, compare adjacent items and swap
    them if they are in the wrong order. Time complexity of O(n^2).
    """
    for i in range(len(ages) - 1):
        for j in range(len(ages) - 1 - i):
            if ages[j] > ages[j + 1]:
                ages[j], ages[j + 1] = ages[j + 1], ages[j]


if __name__ == '__main__':
    display()
    bubble_sort()
    display()
