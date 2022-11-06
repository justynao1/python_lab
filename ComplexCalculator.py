def Complex():
    def __init__(self, realpart, imagpart):
        self.re = realpart
        self.im = imagpart

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)


comp1 = complex(2, 3)
comp2 = complex(5, -2)

