from complex import Complex_number


def parse(str):
    temp = str.split("+")
    if len(temp) == 1:
        temp = str.split("-")
        if len(temp) == 3:
            imag = (-1) * int(temp[2].replace("i", ""))
        else:
            imag = (-1) * int(temp[1].replace("i", ""))
    else:
        imag = int(temp[1].replace("i", ""))
    if len(temp) == 3:
        real = (-1) * int(temp[1])
    else:
        real = int(temp[0])
    return Complex_number(real, imag)


def calc(rownanie):
    if rownanie[2] == "+":
        return rownanie[0] + rownanie[1]
    elif rownanie[2] == "-":
        return rownanie[0] - rownanie[1]
    elif rownanie[2] == "*":
        return rownanie[0] * rownanie[1]
    else:
        return rownanie[0] / rownanie[1]


if __name__ == '__main__':
    a = input("Podaj pierwsza liczbe\n")
    znak = input("Podaj znak\n")
    b = input("Podaj druga liczbe\n")
    print(calc([parse(a), parse(b), znak]))
