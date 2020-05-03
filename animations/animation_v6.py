import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# y = Asin(ax+b)
# x = Bsin(cx+d)
piby2 = np.pi/2
A = 1
a = 1
b = 0
t = np.linspace(0,8*np.pi,400)
fig,ax = plt.subplots()
#plt.subplots_adjust(left=0.1, bottom=0.5, right=0.9, top=0.95, wspace=0, hspace=0)
#ax.axis('square')
ax.set_xlim(0,10)
ax.set_ylim(-3,3)
axamp = plt.axes([0.25, .02, 0.50, 0.02])
axfreq = plt.axes([0.25, .05, 0.50, 0.02])
x_graph, = ax.plot([],[])

# Slider
samp = Slider(axamp, 'A', 0, 2, valinit=A)
sfreq = Slider(axfreq, 'a', 0, 10, valinit=a)

def fun(i):
    global A
    global a
    global b
    yc = A * np.sin(a * t + b)
    x2 = t[0:200]
    y2 = yc[i:200+i]
    x_graph.set_xdata(x2)
    x_graph.set_ydata(y2)

animation = FuncAnimation(fig,func=fun,frames = 100,interval=5)

def update(val):
    global animation
    global A
    global a
    A = samp.val
    a = sfreq.val
    fig.canvas.draw_idle()

samp.on_changed(update)
sfreq.on_changed(update)
plt.show()
