import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 3*x**2 + 2*x

a = 0.0
b = 3.0

#mid-point method
M = (b-a)*f((a+b)/2)
print('Midpoint', M) 

#trapeziod-point method 
T = ((b-a)/2)*(f(a)+f(b))
print('Trapeziod', T)

#simpson's rule
S = ((b-a)/6)*(f(a) + 4*f((a+b)/2) + f(b))
print('Simpson', S)

#plot the function
x = np.linspace(0,3,20)
plt.plot(x,f(x))
plt.show()

#behaviour of result between 3 methods varies
#calculating by hand gives answer 2.25, meaning simpson's rule is most accurate
#you can analyse why by plotting the curve and analysing the shape of the curve in relation to the 3 methods