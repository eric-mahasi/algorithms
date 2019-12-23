"""This script demonstrates the linear search algorithm in Python 3."""

ages = [19, 20, 13, 1, 15, 7, 11, 3, 16, 10]


def display():
    """Prints all the items in the list."""
    print("The ages are: ")
    for i in range(len(ages)):
        print(ages[i])


def linear_search(x):
    """Sequentially check each element of the list until a match is found or
    until the whole list has been searched. Time complexity of O(n).
    """
    for i in range(len(ages)):
        if x == ages[i]:
            print("A student aged ", x, " was found.")
            return True
        else:
            print("A student aged", x, "was not found.")
            return False


if __name__ == '__main__':
    display()
    search_key = int(input("Enter an age to search for: "))
    linear_search(search_key)
