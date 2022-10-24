def calculate_scalar(arr1, arr2):
    if len(arr1) != len(arr2):
        return None
    ret = 0
    for i in range(len(arr1)):
        ret += arr1[i] * arr2[i]
    return ret


if __name__ == '__main__':
    print(calculate_scalar([1, 2, 12, 4], [2, 4, 2, 8]))
