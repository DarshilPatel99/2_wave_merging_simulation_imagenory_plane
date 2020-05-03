import numpy as np
piby2 = np.pi/2
piby3 = np.pi/3
piby4 = np.pi/4

def graph(s):
    if (s == '(0,0)'):
        return 1, 1, 0, 0, 0, 0, 0
    elif (s == 'y=0'):
        return 1, 1, 1, 0, 0, 0, 0
    elif (s == 'x=0'):
        return 1, 1, 0, 1, 0, 0, 0
    elif(s == 'y=x(/)'):
        return 1, 1, 1, 1, 0, 0, 0
    elif(s == 'y=-x(\)'):
        return 1, 1, 1, 1, 0, np.pi, 0
    elif (s == 'y=x^2(∪)'):
        return 1, 1, 2, 1, 0, piby4, 0
    elif (s == 'y=-x^2(∩)'):
        return 1, 1, 2, 1, piby2, 0, 0
    elif (s == 'x=y^2(⊂)'):
        return 1, 1, 1, 2, piby4, 0, 0
    elif (s == 'x=-y^2(⊃)'):
        return 1, 1, 1, 2, 0, piby2, 0
    elif (s == 'x^2+y^2=1(o)'):
        return 1, 1, 1, 1, 0, piby2, 0
    elif (s == 'Eight(8)'):
        return 1, 1, 1, 2, 0, 0, 0
    elif (s == 'Infinity(∞)'):
        return 1, 1, 2, 1 ,0, 0, 0
    elif (s == 'N'):
        return 1, 1, 3, 1, 0, piby3, 0
    elif (s == 'И'):
        return 1, 1, 3, 1, 0, 0, 0
    elif (s == 'Z'):
        return 1, 1, 1, 3, 0, 0, 0
    elif (s == 'S'):
        return 1, 1, 1, 3, piby3, 0, 0
    elif (s == 'Alpha(∝)'):
        return 1, 1, 3, 2, piby2, piby2, 0
    elif (s == 'Mirror of ∝'):
        return 1, 1, 3, 2, 0, piby2, 0
    elif (s == 'Gujarati four'):
        return 1, 1, 2, 3, piby2, piby2, 0
    elif (s == 'Mirror of Gujarati four'):
        return 1, 1, 2, 3, piby2, 0, 0
    elif (s == 'Rotation(∪,∩)3D'):
        return 1, 1, 2, 1, 0, 0, 0.5
    elif (s == 'Rotation(⊂,⊃)3D'):
        return 1, 1, 1, 2, 0, 0, 0.2
    elif (s == 'Rotation(N,И)3D'):
        return 1, 1, 3, 1, 0, 0, 0.5
    elif (s == 'Rotation(Z,S)3D'):
        return 1, 1, 1, 3, 0, 0, 0.2
    elif (s == 'Bangles_X'):
        return 1, 1, 3, 2, 0, 0 ,0.5
    elif (s == 'Bangles_Y'):
        return 1, 1, 2, 3, 0, 0, 0.2
    elif (s == 'Crown_X'):
        return 1, 1, 4, 1, 0, 0 ,0.5
    elif (s == 'Crown_Y'):
        return 1, 1, 1, 4, 0, 0, 0.5
    elif (s == 'Atom'):
        return 1, 1, 4, 3, 0, 0, 0.25

