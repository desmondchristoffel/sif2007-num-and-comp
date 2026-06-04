import numpy as np

def crout(A):
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.eye(n)

    for j in range(n):
        #compute column j of L
        for i in range(j, n):
            L[i, j] = A[i, j] - sum(L[i, k]*U[k, j] for k in range(j))

        #compute row j of u
        for i in range(j+1, n):
            U[j, i] = (A[j, i] - sum(L[j, k]*U[k, i] for k in range(j)))/L[j, j]
    
    return L, U

A = np.array([[2, 4, -2],
              [3, 5, -6],
              [1, 6, 16]], dtype=float)

b = np.array([12, 19, -3], dtype=float)

L, U = crout(A)

print("L = ")
print(L)
print("U = ")
print(U)
print("Check LU = ")
print(L @ U)

x = np.linalg.solve(A, b)
print("Solution x = ")
print(x)