import numpy as np


def calc(mat):
    if mat.shape[0] != mat.shape[1]:
        return
    else:
        print(np.linalg.det(mat))


if __name__ == '__main__':
    mat = np.random.rand(8, 8)
    calc(mat)
