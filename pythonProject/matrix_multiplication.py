import numpy as np


def multipy(mat1, mat2):
    if mat1.shape != mat2.shape:
        return
    else:
        print(mat1 * mat2)


if __name__ == '__main__':
    mat1 = np.random.rand(8, 8)
    mat2 = np.random.rand(8, 8)
    multipy(mat1, mat2)
