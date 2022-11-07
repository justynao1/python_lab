def Calculator():

    def Complex():
        def __init__(self, realpart, imagpart):
            self.re = realpart
            self.im = imagpart

        def __add__(self, other):
            return Complex(self.re + other.re, self.im + other.im)

        def __sub__(self, other):
            return Complex(self.re - other.re, self.im - other.im)

        def __mult__(self, other):
            return Complex()

    comp1 = input("Input the first number: ")
    comp1 = complex(comp1)
    op = input("Enter an operation (+, -, * or /): ")
    comp2 = input("Input the second number: ")
    comp2 = complex(comp2)

    def operations():
        if op == "+":
            result = comp1 + comp2
        elif op == "-":
            result = comp1 - comp2
        elif op == "*":
            result = comp1 * comp2
        elif op == "/":
            result = comp1 / comp2
        try:
            print(result)
        except NameError:
            print("Unknown operation")

    operations()


Calculator()