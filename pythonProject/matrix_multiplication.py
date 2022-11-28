import numpy as np


def multipy(mat1, mat2):
    x1, y1 = mat1.shape
    x2, y2 = mat2.shape
    if y1 != x2:
        return
    else:
        result = np.zeros(shape=(x1, y2))
        for i in range(x1):
            for j in range(y2):
                for k in range(x2):
                    result[i, j] += mat1[i, k] * mat2[k, j]
        print(result)


if __name__ == '__main__':
    mat1 = np.random.rand(8, 8)
    mat2 = np.random.rand(8, 8)
    multipy(mat1, mat2)
