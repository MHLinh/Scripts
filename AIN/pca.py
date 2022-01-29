# Solution provided in 6CCS3AIN at KCL

import matplotlib.pyplot as plt
import numpy as np

# The algorithm to compute the PCA for given matrix.

k=2
X = np.array([
  [4, 2, 3],
  [6, 1, 3],
  [4, 2, 5],
  [7, 8, 3]])

print(X.shape)

print("\n######################################")
print("Step 1 (compute mean row vector)")
meanrow = np.zeros((1,X.shape[1]))
for i in range(X.shape[1]):
  meanrow[0,i] = sum(X[:,i]/X.shape[0])
print(meanrow)

print("\n######################################")
print("Step 2 (compute mean row matrix)")
meanrowmatrix = np.ones((X.shape[0],1)) * meanrow
print(meanrowmatrix)

print("\n######################################")
print("Step 3 (subtract mean)")
B= X-meanrowmatrix
print(B)

print("\n######################################")
print("Step 4 (compute covariance matrix)")
Cov = B.T.dot(B)/X.shape[0]
print(Cov)

print("\n######################################")
print("Step 5 (compute k largest neigenvectors)")
eigenValues, eigenVectors = np.linalg.eig(Cov)
idx = eigenValues.argsort()[::-1]
eigenValues = eigenValues[idx]
eigenVectors = eigenVectors[:,idx]
print("eigenVectors")
print(eigenVectors)
print("eigenValues",eigenValues)
print("------------------------------------")
print(f'Check if Av1 = lambda1 v1:\nAv1 = {Cov.dot(eigenVectors[:, 0])}\nlambda1 v1 = {eigenValues[0]*eigenVectors[:, 0]}')
print("------------------------------------")
print(f'Check if Av2 = lambda2 v2:\nAv2 = {Cov.dot(eigenVectors[:, 1])}\nlambda2 v2 = {eigenValues[1]*eigenVectors[:, 1]}')

print("\n######################################")
print("Step 6 (compute W)")
W=eigenVectors[:,0:k]
print(W)

print("\n######################################")
print("step 7 (project)")
for i in range(X.shape[0]):
  transformed = W.T.dot(X[i, :])
  plt.scatter(transformed[0],transformed[1])
  print("transformed= ", i, " ", transformed)
  print("------------------------------------")
print("\n######################################")

if k==2:
  plt.show()
  plt.savefig("PCA_tutorial.png")
  print("END")

