import matplotlib.pyplot as plt #static library
import numpy as np 
from matplotlib.animation import FuncAnimation #dynamics library
 
#def f(x):
#    return np.sin(x)
 
#def g(x): 
#    return np.cos(x)

#define range of x
x = np.linspace(-2*np.pi,2*np.pi,100)
 
#create frame for animation 
fig,ax = plt.subplots()
xdata,ydata=[],[]
line,= ax.plot([],[],'bo')
 
#label the graph
plt.xlabel('x')
plt.ylabel('f(x)')
 
#start our animation/iterated
def init():
    ax.set_xlim(-2*np.pi,2*np.pi)
    ax.set_ylim(-1,1)
    return line,

#update the frame
def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    line.set_data(xdata,ydata)
    return line,
 
ani = FuncAnimation(fig,update,frames=np.linspace(-2*np.pi,2*np.pi,100),init_func=init,blit=True)
 
ani.save('sine.gif',writer="pillow",fps=50)
 
plt.show()