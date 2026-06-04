import numpy as np

def gaussian_elimination_pivot(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

    #Forward elimination with partial pivoting
    for k in range(n-1):
        #Find row with largest absolute value in column k
        max_row = np.argmax(np.abs(A[k:, k])) + k 

        #swap rows if necessary
        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]
            b[[k, max_row]] = b[[max_row, k]]

        #eliminate entries below the pivot
        for i in range(k+1, n):
            factor = A[i, k]/A[k, k]
            A[i, k:] = A[i, k:] - factor*A[k, k:]
            b[i] = b[i] - factor*b[k]
    
    #Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        s = np.dot(A[i, i+1:], x[i+1:])
        x[i] = (b[i] - s) / A[i, i]

    return x

A = np.array([[0, 2, 1],
              [4, 1, -2],
              [2, 3, 1]], dtype=float)

b = np.array([7, 0, 11], dtype=float)

x = gaussian_elimination_pivot(A, b)
print("Solution x =")
print(x)