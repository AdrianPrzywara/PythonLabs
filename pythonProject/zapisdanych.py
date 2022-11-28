def check_code():
    code = input("Enter code to check: ")
    if int(code) == saved_code:
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    saved_code = 7132
    check_code()