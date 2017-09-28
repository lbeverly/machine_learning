#!/usr/bin/python3 

import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

def rgb2hex(R, G, B):
    s = '#{:02X}{:02X}{:02X}'.format(R, G, B)
    return s

embedding = np.load('butterfly_5_frames_start_250_YUV.npylle k=64 embedding.npy')
colordata = np.load('butterfly_5_frames_start_250_RGB.npy')
rgb = colordata[:, np.array([3,4,5])]
rgb /= 255
print(rgb)

x = embedding.T[np.array([0]), :]
y = embedding.T[np.array([1]), :]


fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x, y, c=rgb, marker='o')
plt.show()
#plt.draw()
#plt.savefig('image_data.png')
