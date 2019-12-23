ages = [19, 20, 13, 1, 15, 7, 11, 3, 16, 10]


def display():
    print("The ages are: ")
    for i in range(len(ages)):
        print(ages[i])
    print("\n")


def insertion_sort():
    for i in range(len(ages)):
        temp = ages[i]
        j = i
        while j > 0 and ages[j - 1] >= temp:
            ages[j] = ages[j - 1]
            j = j - 1
        ages[j] = temp


if __name__ == '__main__':
    display()
    insertion_sort()
    display()
