import numpy as np

#3 input nodes X, 5 hidden nodes Z, 2 output nodes Y
W = np.random.randn(3,5)
V = np.random.randn(5,2)

Sample_Size = 100
 

alpha = 0.05
beta = 0.05

X = np.random.multivariate_normal([1,1,1], [[1,0,0],[0,1,0],[0,0,1]], Sample_Size)
Y = np.matmul(np.atleast_2d([[2, 2.4, -1],[-1, 0, 4]]), X.T).T

for sample, output in zip(X, Y):
	print("Using ", sample, ", ", output)
	Z = np.matmul(sample, W)
	Ycap = np.matmul(Z, V)
	Deltas2 = abs(output-Ycap)
	
	print("Error at the outputs: ", Deltas2)

	Zcap = np.array([])
	for i in range(len(V)):
		backValue = np.dot(Deltas2, V[i])
		Zcap = np.append(Zcap, backValue)
		V[i] = V[i] - beta*backValue*Z[i]

	Deltas1	= abs(Z-Zcap)

	print("Error at the hiddens: ", Deltas1, "\n")
	for i in range(len(W)):
		backValue = np.dot(Deltas1, W[i])
		W[i] = W[i] - alpha*backValue*sample[i]
	


Xtest = X[0]
Ztest = np.matmul(Xtest, W)
Ytest = np.matmul(Ztest, V)
print(Xtest, Ytest, Y[0])

