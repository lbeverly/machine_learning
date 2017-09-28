#!/usr/bin/python3 

import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

def rgb2hex(R, G, B):
    s = '#{:02X}{:02X}{:02X}'.format(R, G, B)
    return s

embedding = np.load('butterfly_5_frames_start_250_YUV lle k=64 3d embedding.npy')
colordata = np.load('butterfly_5_frames_start_250_RGB.npy')

rgb = colordata[:, np.array([3,4,5])]
rgb /= 255

x = embedding.T[1]
y = embedding.T[2]
z = embedding.T[0]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=rgb, marker='o')

ax.view_init(45,45)
plt.show()
#plt.draw()
#plt.savefig('image_data.png')
