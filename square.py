# równanie kwadratowe

import math
def square():
    a = float(input("Input the first value (a): "))
    b = float(input("Input the second value (b): "))
    c = float(input("Input the third value (c): "))
    d = (b**2) - 4 * a * c
    if d > 0:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        print("The solution is: ")
        print(x1, x2)
    elif float(d) == 0:
        x = -b / 2 * a
        print("The solution is: ")
        print(x)
    else:
        print("Can't be resolved")
