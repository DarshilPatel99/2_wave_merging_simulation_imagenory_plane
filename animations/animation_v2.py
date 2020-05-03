import numpy as np
import matplotlib.pyplot as plt
#here is no any animation

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
yc = A * np.sin(a * t + b)
xc = B * np.sin(c * t + d)
ax.plot(xc,yc)
plt.show()
