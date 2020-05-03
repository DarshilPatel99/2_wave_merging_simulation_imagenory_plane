import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# x = Asin(ax+b)
# y = Bsin(cx+d)
piby2 = np.pi/2
A = 1
B = 1
a = 1
b = 0
c = 2
d = 0
t = np.linspace(0,4*np.pi,200)
fig,ax = plt.subplots()
plt.subplots_adjust(left=0, bottom=0.3, right=1, top=0.95, wspace=0, hspace=0)
ax.axis('square')
ax.set_xlim(-3,8)
ax.set_ylim(-3,8)
cir, = ax.plot([],[])

dots, = ax.plot([],[],'--',marker='o')
x_graph, = ax.plot([],[])
y_graph, = ax.plot([],[])

def fun(i):
    global A
    global B
    global a
    global b
    global c
    global d
    yc = A * np.sin(a * t + b)
    xc = B * np.sin(c * t + d)
    x1 = np.array([xc[i],xc[i],B+0.5])
    y1 = np.array([A+0.5,yc[i],yc[i]])
    x2 = t[0:100]
    y2 = yc[i:100+i]
    y3 = t[0:100]
    x3 = xc[i:100+i]
    x2 = x2 + (B + 0.5)
    y3 = y3 + (A + 0.5)
    cir.set_xdata(xc)
    cir.set_ydata(yc)
    dots.set_xdata(x1)
    dots.set_ydata(y1)
    x_graph.set_xdata(x2)
    x_graph.set_ydata(y2)
    y_graph.set_xdata(x3)
    y_graph.set_ydata(y3)

animation = FuncAnimation(fig,func=fun,frames = 100,interval=5)

plt.show()
