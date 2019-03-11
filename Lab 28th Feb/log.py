import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import log, exp

def Sigmoid(weights, input):
	A = np.dot(weights, input)
	A2 = exp(-1*A)
	if A2 == 1 : return 0
	B = 1/(1+A2)
	return B

def AboveThreshold(value):
	threshold = 0.8
	if value > threshold:
		return True
	return False

mu1 = np.array([1,1])
mu2 = np.array([-1,1])
cov1 = np.array([[10,0],[0,6]])
cov2 = np.array([[6,0],[0,10]])

D1 = np.random.multivariate_normal(mu1, cov1, 200)
D1 = np.array([ np.append(x, [1]) for x in D1 ])
D2 = np.random.multivariate_normal(mu2, cov2, 200)
D2 = np.array([ np.append(x, [1]) for x in D2 ])

MiN = min(min(D1.reshape(-1)), min(D2.reshape(-1))) 
MaX = max(max(D1.reshape(-1)), max(D2.reshape(-1)))

W = np.append(np.random.rand(2),[1])
alpha = 0.1

l = len(D1)
n = len(D1)+len(D2)

for i in range(len(D1)):
	A = Sigmoid(W,D1[i])
	if not AboveThreshold(A):
		R = Sigmoid(W,D1[i])
		W = W - alpha*D1[i]*(l-n*R)*R
		e = 1 - R
		#W = W + alpha*e*D1[i]

print("Weights : ", W)

X_Rand = [ [i,j] for i in np.linspace(MiN,MaX,150) for j in np.linspace(MiN,MaX,150) ]
X_Rand = np.array([ np.append(x, [1]) for x in X_Rand ])
S_Plot = np.array([ Sigmoid(W, X_Rand[i]) for i in range(len(X_Rand)) ])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(D1[:,0], D1[:,1], np.ones(len(D1)))
ax.scatter(D2[:,0], D2[:,1], np.zeros(len(D2)))
ax.plot(X_Rand[:,0], X_Rand[:,1], S_Plot, 'g', alpha = 0.4)

ax.plot_surface(X_Rand[:,0], X_Rand[:,1], S_Plot)
#plt.plot(D1[:, 0], D1[:, 1], '.')
#plt.plot(D2[:, 0], D2[:, 1], '.')
plt.show()