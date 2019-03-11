import numpy as np

A = np.random.rand(40,50)
B = np.random.rand(40,50)

C = A.argsort()[0, 0:20]
D = B.argsort()[0, 0:20]
E = A[0, C[:]] < B[0, D[:]]
F = np.where(E)

print(E)
print(F)
print( np.all(E) )
print(A[0].shape)
print( A[0][C[F[:]]] )