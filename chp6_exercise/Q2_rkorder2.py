import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    #differential eqn: dy/dx = f(x, y)
    if np.isclose(x,0):
        return y*1.0
    else:
        return (y*np.sin(x))/x
    
#initial conditions
x = 0
y = 2
h = 0.25
steps = 4

#list to store values for plotting 
x_vals = [x]
y_vals = [y]

print("Step | x | y")
print ("-" * 25)
print(f"0 | {x:.4f} | {y:.4f}")
plt.plot(x,y,"kd-")

for i in range (1, steps + 1):
    K1 = f(x, y)
    K2 = f(x+h, y+h*f(x,y))
    y = y + (h/2)*(K1+K2)
    x = x+h
    print(f"{i} | {x:.4f} | {y:.4f}")
    plt.plot(x,y,"kd-")

plt.title("RK2 Method Approximation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()