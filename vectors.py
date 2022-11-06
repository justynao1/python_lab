# iloczyn skalarny
def vectors():
    a = [1, 2, 12, 4]
    b = [2, 4, 2, 8]
    for i in range(len(a)):
        for j in range(len(b)):
            v = a[i] * b[i] + a[i-1] * b[i-1] + a[i-2] * b[i-2] + a[i-3] * b[i-3]
    print(v)
#vectors()