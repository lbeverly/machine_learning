#!/usr/bin/python3 

import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

embedding = np.load('bouncing_ball_13_frames_start_1_YUV lle k=64 2d embedding.npy')
colordata = np.load('bouncing_ball_13_frames_start_1_RGB.npy')

rgb = colordata[:, np.array([3,4,5])]
#print(embedding)
#for idx, c in enumerate(rgb):
#    if c[0] != c[1] and c[1] != c[2]:
#        print("POINT: {} is {}, it's location in the embedding is ({}, {})".format(idx, c, embedding[idx][0], embedding[idx][1]))

rgb /= 255
#print(rgb)
x = embedding.T[np.array([0]), :]
y = embedding.T[np.array([1]), :]
#print(x.shape)
#print(y)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x, y, c=rgb, marker='o')
ax.set_xlim(0.00323543, 0.00323545)
ax.set_ylim(-0.0003445, -0.00034431)
plt.show()
#plt.draw()
#plt.savefig('image_data.png')
