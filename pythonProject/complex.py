class Complex_number:
    real = 0
    imag = 0

    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def __add__(self, other):
        self.real += other.real
        self.imag += other.imag
        return self

    def __sub__(self, other):
        self.real -= other.real
        self.imag -= other.imag
        return self

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        self.real = real
        self.imag = imag
        return self

    def __truediv__(self, other):
        real = (self.real * other.real + self.imag * other.imag) / (
                    other.real * other.real + other.imag * other.imag)
        imag = (self.imag * other.real - self.real * other.imag) / (
                    other.real * other.real + other.imag * other.imag)
        self.real = real
        self.imag = imag
        return self

    def __repr__(self):
        if self.imag >= 0:
            return f"Wynik: {self.real} + {self.imag}i"
        else:
            return f"Wynik: {self.real} - {abs(self.imag)}i"


def start():
    number1 = Complex_number(1, 8)
    number2 = Complex_number(-2, -3)

    number3 = number1 / number2
    print(number3)


if __name__ == '__main__':
    start()
