import random


def sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


if __name__ == '__main__':
    array = random.sample(range(0, 100), 50)
    sort(array)

    for i in array:
        print(i)
