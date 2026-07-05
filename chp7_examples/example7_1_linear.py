import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*x + 3

a = 0.0
b = 2.0

#mid-point method
M = (b-a)*f((a+b)/2)
print('Midpoint', M) 

#trapeziod-point method 
T = ((b-a)/2)*(f(a)+f(b))
print('Trapeziod', T)

#simpson/s rule
S = ((b-a)/6)*(f(a) + 4*f((a+b)/2) + f(b))
print('Simpson', S)

#all 3 method gives exact answer, 10.0
#this is the same answer as when you solve by hand because this is a linear equation, a very simple function

#plot the function
x = np.linspace(0,2,10)
plt.plot(x,f(x))
#plt.show()