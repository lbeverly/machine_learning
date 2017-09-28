#!/usr/bin/python3 

import sys
from matplotlib.figure import SubplotParams
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

data = np.load('bouncing_ball_13_frames_start_1_RGB.npy')

dataT = data.T
t = dataT[0]#[(120 * 90*10):]
x = dataT[1]#[(120 * 90*10):]
y = dataT[2]#[(120 * 90*10):]

rgb = dataT[np.array([3,4,5], dtype=np.intp), :]
rgb /= 255
rgbA = np.zeros((4, rgb.shape[1]))
rgbA[:-1,:] = rgb
rgbA[3,:] = np.array([0.03] * rgbA.shape[1])
print(rgbA)
rgb = rgbA.T
for c in rgb:
    r, g, b, a = c
    if (b*255) > ((g*255) + 10):
        c[:] = [r, g, b, 0.2]

print(rgb)

#rgb = rgb[(120 * 90*10):]


fig = plt.figure(figsize=(11, 8.5), dpi=150, subplotpars=SubplotParams(left=0.1, bottom=0.1, top=1.0, right=1.0))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(t, x, y, c=rgb, marker='o', lw=0.0)
ax.set_xlim(0, 25)

ax.view_init(15,55)
plt.show()
#plt.draw()
#plt.savefig('opaque_image_through_time.png')
