import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider ,RadioButtons
from graphs import graph

# X = Asin(at+b)
# Y = Bsin(ct+d)

# angle value values [0,4π]
t = np.linspace(0,4*np.pi,200)

A = 1
B = 1
a = 1
b = 0
c = 1
d = 0
# phase difference = (a-c)t + (b-d)
# r is changing rate in phase difference
r = 0

fig,ax = plt.subplots(figsize=(18, 12))
plt.subplots_adjust(left=0, bottom=0.3, right=1, top=0.95, wspace=0, hspace=0)
ax.axis('square')
ax.set_xlim(-3.2,8)
ax.set_ylim(-3.2,8)
ax.set_title("2 Wave merging simulation imagenory plane")

#widgets's position
xamp = plt.axes([0.70, 0.9, 0.25, 0.05])
yamp = plt.axes([0.70, 0.8, 0.25, 0.05])
xfreq = plt.axes([0.70, 0.7, 0.25, 0.05])
yfreq = plt.axes([0.70, 0.6, 0.25, 0.05])
xphase = plt.axes([0.70, 0.5, 0.25, 0.05])
yphase = plt.axes([0.70, 0.4, 0.25, 0.05])
phase_diff = plt.axes([0.70, 0.3, 0.25, 0.05])
rax = plt.axes([0.02, 0.1, 0.30, 0.85])

#graphs ploting started
dots, = ax.plot([],[],'--',marker='o')
x_graph, = ax.plot([],[],label = 'X = Asin(at+b)')
y_graph, = ax.plot([],[],label = 'Y = Bsin(ct+d)')
figure, = ax.plot([],[],label = 'X+i*Y ,i = root(-1)')

#Slider Widgets
sxamp = Slider(xamp, 'A', 0, 3, valinit=A)
syamp = Slider(yamp, 'B', 0, 3, valinit=B)
sxfreq = Slider(xfreq, 'a', 0, 4, valinit=a)
syfreq = Slider(yfreq, 'c', 0, 4, valinit=c)
sxphase = Slider(xphase, 'b', 0, 7, valinit=b)
syphase = Slider(yphase, 'd', 0, 7, valinit=d)
sphase_diff = Slider(phase_diff, 'Rotate', 0, 1, valinit=r)

#Text in window
plt.text(0.40, -0.90,'controlers',fontsize=14)

#Radio button for graphs
radio = RadioButtons(rax, ('(0,0)','y=0','x=0','y=x(/)' ,'y=-x(\)' ,'y=x^2(∪)','y=-x^2(∩)','x=y^2(⊂)','x=-y^2(⊃)','x^2+y^2=1(o)','Eight(8)','Infinity(∞)','N','И','Z','S','Alpha(∝)','Mirror of ∝','Gujarati four','Mirror of Gujarati four','Rotation(∪,∩)3D','Rotation(⊂,⊃)3D','Rotation(N,И)3D','Rotation(Z,S)3D','Bangles_X','Bangles_Y','Crown_X','Crown_Y','Atom'), active=3)

#animation function
def animate(i):
    #not creating exctra variable using global variables
    global A
    global B
    global a
    global b
    global c
    global d
    global r

    #shape will draw for period of 4π
    yc = A * np.sin(a * t + b)
    xc = B * np.sin(c * t + d)

    #display movement of points on shape and starting of wave
    x1 = np.array([xc[i],xc[i],B+0.5])
    y1 = np.array([A+0.5,yc[i],yc[i]])

    # Waves will draw for period of 2π
    x2 = t[0:100]
    y2 = yc[i:100+i]
    y3 = t[0:100]
    x3 = xc[i:100+i]
    x2 = x2 + (B + 0.5)
    y3 = y3 + (A + 0.5)

    # set data of graph
    figure.set_xdata(xc)
    figure.set_ydata(yc)
    dots.set_xdata(x1)
    dots.set_ydata(y1)
    x_graph.set_xdata(x2)
    x_graph.set_ydata(y2)
    y_graph.set_xdata(x3)
    y_graph.set_ydata(y3)

    #for rotation
    b = (b+r/20)%(2*np.pi)

#animation
animation = FuncAnimation(fig,func=animate,frames = range(0,100),interval=5)

#Execute when any slider's value changes
def update(val):
    # not creating exctra variable using global variables
    global animation
    global A
    global B
    global a
    global b
    global c
    global d
    global r

    # set velue of sliders to variable
    A = sxamp.val
    B = syamp.val
    a = sxfreq.val
    c = syfreq.val
    b = sxphase.val
    d = syphase.val
    r = sphase_diff.val

    fig.canvas.draw_idle()

#Execute when Radio button clicked
def shape(s):
    # not creating exctra variable using global variables
    global animation
    global A
    global B
    global a
    global b
    global c
    global d
    global r

    #set variables as radio button
    A,B,a,c,b,d,r = graph(s)

    # set value of sliders as radio button
    sxphase.valinit,syphase.valinit,sxamp.valinit,syamp.valinit,sxfreq.valinit,syfreq.valinit,sphase_diff.valinit = b,d,A,B,a,c,r
    sxphase.reset()
    syphase.reset()
    sxamp.reset()
    syamp.reset()
    sxfreq.reset()
    syfreq.reset()
    sphase_diff.reset()

    fig.canvas.draw_idle()

sxamp.on_changed(update)
syamp.on_changed(update)
sxfreq.on_changed(update)
syfreq.on_changed(update)
sxphase.on_changed(update)
syphase.on_changed(update)
sphase_diff.on_changed(update)

radio.on_clicked(shape)

ax.legend(fontsize=12)
plt.show()
