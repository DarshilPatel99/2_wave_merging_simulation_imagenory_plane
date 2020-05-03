import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# X = Asin(ax+b)
# Y = Bsin(cx+d)
piby2 = np.pi/2
A = 1
B = 1
a = 2
b = 0
c = 3
d = piby2
r = 0
t = np.linspace(0,4*np.pi,200)
fig,ax = plt.subplots()
plt.subplots_adjust(left=0, bottom=0.3, right=1, top=0.95, wspace=0, hspace=0)
ax.axis('square')
ax.set_xlim(-3.2,8)
ax.set_ylim(-3.2,8)

xamp = plt.axes([0.20, 0.2, 0.25, 0.02])
yamp = plt.axes([0.55, 0.2, 0.25, 0.02])
xfreq = plt.axes([0.20, 0.15, 0.25, 0.02])
yfreq = plt.axes([0.55, 0.15, 0.25, 0.02])
xphase = plt.axes([0.20, 0.1, 0.25, 0.02])
yphase = plt.axes([0.55, 0.1, 0.25, 0.02])

#line, = ax.plot(t+2.5,xc)
#line, = ax.plot(yc,t+2.5)
cir, = ax.plot([],[])
dots, = ax.plot([],[],'--',marker='o')
x_graph, = ax.plot([],[],label = 'Asin(ax+b)')
y_graph, = ax.plot([],[],label = 'Bsin(cx+d)')

sxamp = Slider(xamp, 'A', 0, 3, valinit=A)
syamp = Slider(yamp, 'B', 0, 3, valinit=B)
sxfreq = Slider(xfreq, 'a', 0, 3, valinit=a)
syfreq = Slider(yfreq, 'c', 0, 3, valinit=c)
sxphase = Slider(xphase, 'b', 0, 7, valinit=b)
syphase = Slider(yphase, 'd', 0, 7, valinit=d)

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

def update(val):
    global animation
    global A
    global B
    global a
    global b
    global c
    global d
    global r
    A = sxamp.val
    B = syamp.val
    a = sxfreq.val
    c = syfreq.val
    b = sxphase.val
    d = syphase.val
    fig.canvas.draw_idle()

sxamp.on_changed(update)
syamp.on_changed(update)
sxfreq.on_changed(update)
syfreq.on_changed(update)
sxphase.on_changed(update)
syphase.on_changed(update)

ax.legend()
plt.show()
