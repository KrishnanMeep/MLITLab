import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,40)
m = np.random.randint(10)
c = np.random.randint(50)

y = m*x + c
y += np.random.normal(0,10,len(y))
print(m,c)

X = np.vstack([np.ones(len(x)), x]).T
XT = X.T
W = np.linalg.pinv(np.matmul(XT, X))
W = np.matmul(W, XT)
W = np.matmul(W, y)
print(W)

plt.plot(x,y,'.')
plt.plot(x,x*W[1]+W[0], 'r')
lim = max(max(x),max(y))
plt.axis((0,lim,0,lim))
plt.show() 