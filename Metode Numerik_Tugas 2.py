import numpy as np

# matriks koefisien
A = np.array([[1, 1, 1],
              [1, 2, -1],
              [2, 1, 2]])

# vektor hasil
b = np.array([6, 2, 10])

# pake metode numpy untuk menyelesaikan persamaan Ax = b
x = np.linalg.solve(A, b)

# tampil hasil
print("Solusi dari sistem persamaan adalah:")
print(f"x1 = {x[0]}")
print(f"x2 = {x[1]}")
print(f"x3 = {x[2]}")
