from math import sqrt


def get_roots(a, b, c):
    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        return x1, x2
    elif delta == 0:
        x = -b / (2 * a)
        return x
    else:
        return None


if __name__ == '__main__':
    print(get_roots(2, 4, 5))
