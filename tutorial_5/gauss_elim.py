import numpy as np

A = np.array([[3,-1,2],
              [2,4,1],
              [1,-3,5]], dtype=float)

b = np.array([7,13,10],dtype=float)

x = np.linalg.solve(A, b)

print("Solution x =")
print(x)