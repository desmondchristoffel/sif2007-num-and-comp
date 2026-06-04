import numpy as np

A = np.array([[4, 2, 4],
              [2, 10, -1],
              [4, -1, 9]], dtype=float)

b = np.array([12, 21, 11], dtype=float)

L = np.linalg.cholesky(A)

print("L = ")
print(L)
print("Check L L.T = ")
print(L @ L.T)

x = np.linalg.solve(A, b)
print("Solution x = ")
print(x)