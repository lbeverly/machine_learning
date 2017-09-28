#!/usr/bin/python3 

import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

def rgb2hex(R, G, B):
    s = '#{:02X}{:02X}{:02X}'.format(R, G, B)
    return s

data = np.load('butterfly_5_frames_start_250_RGB.npy')

dataT = data.T
t = dataT[0]
x = dataT[1]
y = dataT[2]

rgbA = dataT[np.array([3,4,5], dtype=np.intp), :]
print(rgbA)
rgb = rgbA.T
rgb /= 255
print(rgb)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(t, x, y, c=rgb, marker='o')

ax.view_init(45,45)
plt.show()
#plt.draw()
#plt.savefig('image_data.png')
