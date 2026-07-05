import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x)

a = 0.0
b = 1.0

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
x = np.linspace(0,1,20)
plt.plot(x,f(x))
plt.show()

#Simpson is the most accurate
#trailing decimals may differ depending on computer chip and exponent value stored in python library 
