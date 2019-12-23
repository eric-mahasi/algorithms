ages = [19, 20, 13, 1, 15, 7, 11, 3, 16, 10]


def display():
    print("The ages are: ")
    for i in range(len(ages)):
        print(ages[i])
    print("\n")


def bubble_sort():
    for i in range(len(ages) - 1):
        for j in range(len(ages) - 1 - i):
            if ages[j] > ages[j + 1]:
                ages[j], ages[j + 1] = ages[j + 1], ages[j]


if __name__ == '__main__':
    display()
    bubble_sort()
    display()
