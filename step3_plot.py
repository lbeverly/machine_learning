#!/usr/bin/python3 

import matplotlib.pyplot as plt
import numpy as np

def yuv444_2_rgb(y, u, v):
    C = y - 16
    D = u - 128 
    E = v - 128 
    R = (int(298 * C + 409 * E + 128) >> 8)
    G = (int(298 * C - 100 * D - 208 * E + 128) >> 8)
    B = (int(298 * C + 516 * D + 128) >> 8)
    return int(R), int(G), int(B)

def ycbcr2rgb(y, cb, cr):
    Y = int(y)
    Cr = int(cr - 128)
    Cb = int(cb - 128)
    R = Y + Cr + (Cr >> 2) + (Cr >> 3) + (Cr >> 5)
    G = Y - ((Cb >> 2) + (Cb >> 4) + (Cb >> 5)) - ((Cr >> 1) + (Cr >> 3) + (Cr >> 4) + (Cr >> 5))
    B = Y + Cb + (Cb >> 1) + (Cb >> 2) + (Cb >> 6)
    return R, G, B

def rgb2hex(R, G, B):
    s = '#{:02X}{:02X}{:02X}'.format(R, G, B)
    return s



X = np.load('5-frames-LowLowResVideo.npy')
embedding = np.load('5-frames-LowLowResVideo.npylle k=64 embedding.npy')
for idx, p in enumerate(embedding):
    yuv = X[idx][3:]
    #print("YUV: " + str(yuv))
    rgb = [int(x) for x in yuv]
    print("RGB: " + str(rgb))
    colorcode = rgb2hex(*rgb)
    print("colorcode: " + colorcode)
    plt.plot(p[0],p[1], color=colorcode)
plt.show()
