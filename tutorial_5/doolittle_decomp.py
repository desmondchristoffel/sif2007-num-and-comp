import numpy as np

def doolittle(A):
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros((n, n))

    for i in range(n):
        #compute row i of U
        for k in range (i, n): 
            U[i, k] = A[i, k] - sum(L[i, j]*U[j, k] for j in range(i))

        #compute column i of L
        for k in range(i+1, n):
            L[k, i] = (A[k, i] - sum(L[k, j]*U[j, i] for j in range(i)))/U[i,i]

    return L, U

A = np.array([[4, -2, 1],
              [8, -1, 7],
              [-4, 11, 16]], dtype=float)

b = np.array([13, 38, 29], dtype=float)

L, U = doolittle(A)

print("L = ")
print(L)
print("U = ")
print(U)
print("Check LU = ")
print(L @ U)

#solve using numpy for final verification
x = np.linalg.solve(A, b)
print("Solution x = ")
print(x)