import numpy as np
import pylab
import matplotlib .pyplot as plt

x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([1,3,2,5,7,8,8,9,10,12])
X=np.mean(x)
print(X)

Y=np.mean(y)
print(Y)
#linregress(X, Y)

num= np.sum((x-X)*(y-Y))
den=np.sum((x-X)*(x-X))

m=num/den
print(m)

constant=Y- m*X
print("constant", constant )
Yline= m*x + constant
print(Yline)
plt.plot(x,Yline)
plt.scatter(x,y)
plt.show()

