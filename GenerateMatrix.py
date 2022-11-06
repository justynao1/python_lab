import numpy

def matrix():
    A = numpy.random.randint(0, 10, size=(128, 128))
    B = numpy.random.randint(0, 10, size=(128, 128))

    '''
    for i in range(len(A)):
        #columns
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + B[i][j]

    for r in C:
        print(r)
    '''
    result = A+B
    print(result)