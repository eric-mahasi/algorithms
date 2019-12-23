ages = [1, 3, 7, 10, 11, 13, 15, 16, 19, 20]


def display():
    for i in range(len(ages)):
        print(ages[i])


def binary_search(x):
    lower_bound = 0
    upper_bound = len(ages) - 1
    while True:
        mid = int((lower_bound + upper_bound) / 2)
        if x == ages[mid]:
            print("A student aged", x, "was found.")
            return True
        elif lower_bound > upper_bound:
            print("A student aged", x, "was not found.")
            return False
        else:
            if x < ages[mid]:
                upper_bound = mid - 1
            else:
                lower_bound = mid + 1


if __name__ == '__main__':
    display()
    search_key = int(input("Enter an age to search for: "))
    binary_search(search_key)
