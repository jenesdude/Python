import math


class Complex:
    """Class for representation of complex numbers

    It supports basic functions used complex numbers
    """
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return "Complex({}, {})".format(str(self.real),
                                        str(round(self.imag)))

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __str__(self):
        return "({:-}{:+}j)".format(self.real, self.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + other.real * self.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __hash__(self):
        return self.real * 1000 + self.imag

    def __ne__(self, other):
        return not self == other

    def __pow__(self, exponent):
        """Trigonometric way to calculate exponentiation

        """
        if exponent % 1 == 0:
            return self.int_pow(exponent)
        r = self.real
        i = self.imag
        angle = 90 if r == 0 else 0 if i == 0 else math.atan(i / r) * 180 / math.pi
        angle = (angle * exponent) % 360
        cos = math.cos(angle * math.pi / 180)
        sin = math.sin(angle * math.pi / 180)
        length = math.sqrt(r ** 2 + i ** 2) ** exponent
        return Complex(round(length * cos, 4), round(length * sin))

    def int_pow(self, exponent):
        """Simple integer exponentiation

        """
        result = Complex(1, 0)
        for i in range(exponent):
            result *= self
        return result

    def __int__(self):
        return self.real

    @property
    def conjugate(self):
        return Complex(self.real, -self.imag)

    @property
    def magnitude(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)