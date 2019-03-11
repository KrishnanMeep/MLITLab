import numpy as np
import matplotlib.pyplot as plt

mu1 = np.array([np.random.randint(-10,10),np.random.randint(-10,10)])
mu2 = np.array([np.random.randint(-10,10),np.random.randint(-10,10)])
cov1 = np.array([[3,0],[0,4]])
cov2 = np.array([[2,0],[0,3]]) 

A = np.random.multivariate_normal(mu1, cov1, 300)
B = np.random.multivariate_normal(mu2, cov2, 300)


a = np.random.randint(10)
b = np.random.randint(10)
c = np.random.randint(10)
print("Original: ", a, b,c)
alpha = 0.1

y = a*A[:,0] + b*A[:,1] + c
#W = np.where(y > 0)
#print(W)

for j in range(len(B)):
	for i in range(len(A)):
		z1 = A[i,0]*-a + A[i,1]*b - c
		z2 = B[j,0]*-a + B[j,1]*b - c
		e = (z1/z2)
		e2 = abs(e) 		
		if e2 > 1:
			a += e*alpha*A[i,0]
			b += e*alpha*A[i,1]
			c += e*alpha
		if e2 < 1:
			a -= (1/e)*alpha*B[i,0]
			b -= (1/e)*alpha*B[i,1]
			c -= (1/e)*alpha
		#print(e, e>1)

print("Later: ",a,b,c)	

x, y = int(min(min(A[:, 0]), min(B[:, 0]))), int(max(max(A[:, 0]), max(B[:, 0])))
plt.plot(range(x,y), [ a*i/b + c/b for i in range(x,y)])
plt.plot(A[:, 0], A[:,1], 'r.')
plt.plot(B[:, 0], B[:,1], 'b.')
plt.show()



