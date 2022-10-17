from pathlib import Path


def print_files_in_directory(x):
    for i in (x.glob("*")):
        if i.is_dir():
            q = x / i
            print_files_in_directory(q)
        else:
            print(i)


if __name__ == '__main__':
    p = Path('.')
    print_files_in_directory(p)
