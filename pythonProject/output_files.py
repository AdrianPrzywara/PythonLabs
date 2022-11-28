from pathlib import Path


def print_files_in_directory(x):
    count = 0
    for i in (x.glob("*")):
        if i.is_dir():
            q = x / i
            count += print_files_in_directory(q)
        else:
            count += 1
            print(i)
    return count


if __name__ == '__main__':
    p = Path('.')
    print(print_files_in_directory(p))
