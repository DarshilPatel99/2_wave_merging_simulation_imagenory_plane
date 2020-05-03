import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

'''
A = 1
B = 1
a = 1
b = 0
c = 1
d = 0
'''
yc = np.zeros(200)
xc = np.zeros(200)

t = np.linspace(0,8,200)

for i in range(0,200):
    if (i < 25):
        xc[25+i]=yc[i] = 1
    elif (i < 50):
        xc[25+i]=yc[i] = yc[i - 1] - (2 / 25)
    elif (i < 75):
        xc[25+i]=yc[i] = -1
    elif (i < 100):
        xc[25+i]=yc[i] = yc[i - 1] + (2 / 25)
    elif (i < 125):
        xc[25+i]=yc[i] = 1
    elif (i < 150):
        xc[25+i]=yc[i] = yc[i - 1] - (2 / 25)
    elif (i < 175):
        xc[25+i]=yc[i] = -1
    elif (i < 200):
        xc[i-175]=yc[i] = yc[i - 1] + (2 / 25)


fig,ax = plt.subplots()
plt.subplots_adjust(left=0, bottom=0.3, right=1, top=0.95, wspace=0, hspace=0)
ax.axis('square')
ax.set_xlim(-3,10)
ax.set_ylim(-3,10)
squre, = ax.plot(xc,yc)
#line, = ax.plot(t+2.5,xc)
#line, = ax.plot(yc,t+2.5)
dots, = ax.plot([],[],'--',marker='o')
x_graph, = ax.plot([],[])
y_graph, = ax.plot([],[])

def fun(i):
    '''
    global A
    global B
    global a
    global b
    global c
    global d
    '''
    global yc
    global xc
    x1 = np.array([xc[i],xc[i],2+0.5])
    y1 = np.array([2+0.5,yc[i],yc[i]])
    x2 = t[0:100]
    y2 = yc[i:100+i]
    y3 = t[0:100]
    x3 = xc[i:100+i]
    x2 = x2 + (2 + 0.5)
    y3 = y3 + (2 + 0.5)
    squre.set_xdata(xc)
    squre.set_ydata(yc)
    dots.set_xdata(x1)
    dots.set_ydata(y1)
    x_graph.set_xdata(x2)
    x_graph.set_ydata(y2)
    y_graph.set_xdata(x3)
    y_graph.set_ydata(y3)

animation = FuncAnimation(fig,func=fun,frames = range(0,100),interval=5)

plt.show()
