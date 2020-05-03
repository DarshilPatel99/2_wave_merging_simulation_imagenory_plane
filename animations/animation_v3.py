import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# X = Asin(ax+b)
# Y = Bsin(cx+d)
piby2 = np.pi/2
A = 1
B = 1
a = 1
b = 0
c = 1
d = piby2
t = np.linspace(0,4*np.pi,200)
fig,ax = plt.subplots()
plt.subplots_adjust(left=0, bottom=0.3, right=1, top=0.95, wspace=0, hspace=0)
ax.axis('square')
ax.set_xlim(-3,8)
ax.set_ylim(-3,8)
xc = A * np.sin(a * t + b)
yc = B * np.sin(c * t + d)
ax.plot(xc,yc)
cir, = ax.plot([],[])

dots, = ax.plot([],[],'--',marker='o')

def fun(i):
    x1 = np.array([xc[i],xc[i],B+0.5])
    y1 = np.array([A+0.5,yc[i],yc[i]])
    dots.set_xdata(x1)
    dots.set_ydata(y1)

animation = FuncAnimation(fig,func=fun,frames = 100,interval=5)

plt.show()
