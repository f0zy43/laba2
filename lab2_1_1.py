import math

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag < 0:
            return f"{self.real} - {abs(self.imag)}i"
        else:
            return f"{self.real} + {self.imag}i"

    def __add__(self, other):
        if isinstance(other, Complex):
            real = self.real + other.real
            imag = self.imag + other.imag
            return Complex(real, imag)
        else:
            raise TypeError("неправильная операция")

    def __sub__(self, other):
        if isinstance(other, Complex):
            real = self.real - other.real
            imag = self.imag - other.imag
            return Complex(real, imag)
        else:
            raise TypeError("неправильная операция")

    def __mul__(self, other):
        if isinstance(other, Complex):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return Complex(real, imag)
        else:
            raise TypeError("неправильная операция")

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denominator = other.real ** 2 + other.imag ** 2
            real = (self.real * other.real + self.imag * other.imag) / denominator
            imag = (self.imag * other.real - self.real * other.imag) / denominator
            return Complex(real, imag)
        else:
            raise TypeError("неправильная операция")

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

if __name__ == "__main__":
    a = Complex(3, 2)
    b = Complex(1, -1)

    print("Первое цчисло:", a, end="     "), print("второе число:", b)


    print("Сложение: a + b =", a + b)
    print("Вычитание: a - b =", a - b)
    print("умножение: a * b =", a * b)
    print("Деление: a / b =", a / b)


    print("Модуль 1 |a| =", abs(a))
    print("Модуль 2 |b| =", abs(b))