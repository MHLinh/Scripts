import numpy as np

# Matrix multiplication using numpy
# Parameters:
#   matA, matB - matrices of size a x b and b x c
def mul(matA, matB):
  print()
  print("Matrix A:")
  print(matA)
  print("Matrix B:")
  print(matB)
  print("Result:")
  print(np.matmul(matA, matB))

# Matrix transpose using numpy
# Parameters:
#   mat - matrix
def transpose(mat):
  print()
  print("Matrix:")
  print(mat)
  print("Transpose:")
  print(np.transpose(mat))

matA = np.array([[1, 5], [0, 1]])

matB = np.array([[2], [0]])

mul(matA, matB)

matX = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

transpose(matX)
