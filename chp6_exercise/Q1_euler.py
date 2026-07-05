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

for i in range(1, steps + 1):
    #calculate the next u using EUler's formula
    y = y + h*f(x,y)
    x = x+h 

    #store the values 
    x_vals.append(x)
    y_vals.append(y)

    print(f"{i} | {x:.4f} | {y:.4f}")
    plt.plot(x,y,"kd-")

plt.title("Euler Method Approximation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

