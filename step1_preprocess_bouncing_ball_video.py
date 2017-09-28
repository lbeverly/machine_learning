#!/usr/bin/env python

import sys
import numpy as np
from skvideo.io import FFmpegReader, ffprobe
import colorsys


def PreProcessVideo(fmt, filename, output, start=250, n_frames=5):
    info = ffprobe(filename)
    vinfo = info['video']

    v = FFmpegReader(filename, outputdict={'-pix_fmt': fmt})

    X = np.ndarray( (int(vinfo['@height']) * int(vinfo['@width']) * n_frames, 6) )
    n = 0
    t = 0
    frames = v.nextFrame()
    for t, frame in enumerate(frames):
        if t < start:
            continue
        if t >= start + n_frames:
            break
        print(t)
        sys.stdout.flush()
        printed = False
        for row_n, line in enumerate(frame):
            for col_n, pixel in enumerate(line):
                c1, c2, c3= pixel
                t_scaled = (float(t - start) / float(vinfo['@width'])) * 255.0
                x_scaled = (float(col_n) / float(vinfo['@width'])) * 255.0
                y_scaled = (float(row_n) / float(vinfo['@width'])) * 255.0
                X[n] = np.array([t_scaled, x_scaled, y_scaled, c1, c2, c3])
                n += 1

    print("Done with the encode part")
    np.save(output, X, allow_pickle=False, fix_imports=False)

if __name__ == '__main__':
    filename = "BouncingBall.mp4"
    output = "bouncing_ball_13_frames_start_1_YUV.npy"
    PreProcessVideo('yuv444p', filename, output, start=10, n_frames=13)
    output = "bouncing_ball_13_frames_start_1_RGB.npy"
    PreProcessVideo('rgb24', filename, output, start=10, n_frames=13)
