# print("Hello World")

# name, surname, birthday = input("Enter your name, surname and birthday\n").split()
# print("Your name: {}\nYour surname: {}\nYour birthday: {}\n".format(name, surname, birthday))

saved_code = 7132


def check_code():
    code = input("Enter code to check: ")
    if code == saved_code:
        print("True")
    else:
        print("False")

