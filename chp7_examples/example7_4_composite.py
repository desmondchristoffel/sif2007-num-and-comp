import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*np.sin(30*x)

a = 0.0
b = 2*np.pi
n = 1000
h = (b-a)/n

#mid-point method
M = (b-a)*f((a+b)/2)
print('Midpoint', M) 

#trapeziod-point method 
T = ((b-a)/2)*(f(a)+f(b))
print('Trapeziod', T)

#composite trapezoid method
for i in range(0,10):
    Tc = h/2*(f(a)+2*f(a+(i-0.5)+f(b)))
print('trapezoid composite', Tc)

#simpson's rule
S = ((b-a)/6)*(f(a) + 4*f((a+b)/2) + f(b))
print('Simpson', S)

#composite simpson's method 
integral_sum = 0.0
m = int(n/2)
for i in range(1,m+1):
    #calculate x coordinates for this chunk
    x_2i_minus_2 = a + (2*i - 2)*h
    x_2i_minus_1 = a + (2*i - 1)*h
    x_2i = a + (2*i)*h

    #evaluate the function at the coordinates
    f0 = f(x_2i_minus_2)
    f1 = f(x_2i_minus_1)
    f2 = f(x_2i)

    #evaluate the composite simpson's chunk formula
    chunk_sum = (h/3.0)*(f0 + 4.0*f1 + f2)
    integral_sum = integral_sum + chunk_sum

print('Simpson Composite', integral_sum)

#plot the function
x = np.linspace(0,2*np.pi,500)
plt.plot(x,f(x))
#plt.show()

#midpoint, trapezoid and simpson method all fail
#refer pg261 of epperson numerical textbook