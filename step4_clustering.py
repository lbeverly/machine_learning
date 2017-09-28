import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.vq import kmeans2
from scipy.stats import gaussian_kde

data = np.load('bouncing_ball_13_frames_start_1_YUV lle k=64 2d embedding.npy')

centroids, labels = kmeans2(data, 4)
plt.plot(labels)
plt.show()

#density = gaussian_kde(data)

#xs = np.linspace(0,8,200)
#density.covariance_factor = lambda : .25
#density._compute_covariance()
#plt.plot(xs,density(xs))
#plt.show()
