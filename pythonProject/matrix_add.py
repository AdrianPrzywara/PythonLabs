import numpy as np


def add(mat1, mat2):
    if mat1.shape != mat2.shape:
        return
    else:
        x, y = mat1.shape
        result = np.zeros(shape=(x, y))
        for i in range(x):
            for j in range(y):
                result[i, j] = mat1[i, j] + mat2[i, j]
        print(result)


if __name__ == '__main__':
    mat1 = np.random.rand(128, 128)
    mat2 = np.random.rand(128, 128)
    add(mat1, mat2)
