def find_max(arr, number):
    hash = [0] * 10

    for i in range(number):
        hash[arr[i]] += 1

    for i in range(9, -1, -1):
        for j in range(hash[i]):
            print(i, end=" ")


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 0]
    number = len(arr)
    find_max(arr, number)
