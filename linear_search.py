ages = [19, 20, 13, 1, 15, 7, 11, 3, 16, 10]


def display():
    print("The ages are: ")
    for i in range(len(ages)):
        print(ages[i])


def linear_search(x):
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
