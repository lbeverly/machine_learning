#!/usr/bin/env python3

import numpy as np
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

color = np.load('bouncing_ball_13_frames_start_1_RGB.npy')
d13 = np.load('bouncing_ball_13_frames_start_1_YUV lle k=64 2d embedding.npy')
#d5 = np.load('bouncing_ball_5_frames_start_250_YUV lle k=64 2d embedding.npy')



new_points = []
rgb = []
for idx, p in enumerate(color):
    t, x, y, r, g, b = p
    if r > g + 10 and b > g + 10:
        new_points.append(d13[idx])
        rgb.append([r, g, b, 255])

embedding = np.matrix(new_points)
rgb = np.matrix(rgb)
rgb /= 255

#rgb = color[:, np.array([3,4,5])]

x = embedding.T[np.array([0]), :]
y = embedding.T[np.array([1]), :]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x, y, c=rgb, marker='o')
plt.show()






