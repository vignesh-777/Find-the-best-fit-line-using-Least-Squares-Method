import numpy as np
import matplotlib.pyplot as plt
X=np.array(eval(input()))
Y=np.array(eval(input()))
X_mean =np.mean(X)
Y_mean =np.mean(Y)
num=0
denom=0
for i in range(len(X)):
  num+=(X[i]-X_mean)*(Y[i]-Y_mean)
  denom+=(X[i]-X_mean)**2
m=num/denom
b=Y_mean - m*X_mean
print(m,b)
Y_predicted=m*X+b
print(Y_predicted)
plt.scatter(X,Y)
plt.plot(X,Y_predicted,color='red')
plt.show()