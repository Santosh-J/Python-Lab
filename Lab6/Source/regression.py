from numpy import *
from matplotlib.pyplot import *

from sklearn.linear_model import LinearRegression
# take two arrays
x=array([0,1,2,3,4,5,6,7,8,9])
y=array([1,3,2,5,7,8,8,9,10,12])
#use polyfit fucntion for linear relation
m=polyfit(x,y,1)

print("The slope is:")
print(m[0])
#print of slope
print("The intercept is:")
print(m[1])
#print of intercept
plot(x,y,'o')
# plotting of the lines
plot(x,polyval(m,x),'r-')
# showing the output
show()
# use of regression model
mod = LinearRegression()
mod.fit(x, y)
# predicting the value
y_predict = mod.predict(x)
#print
print(y_predict)