from sklearn import manifold, utils
from sklearn.manifold import locally_linear_embedding
from sklearn.neighbors import NearestNeighbors
import numpy as np
from scipy import linalg
import sys
import os.path

filename = "butterfly_5_frames_start_250_YUV.npy"
base, extension = os.path.splitext(filename)

neighbors = 64

X = np.load(filename)
print("Done loading data")

embedding, errors = locally_linear_embedding(X, n_neighbors=neighbors, n_components=2, n_jobs=-1)

np.save(base + ' lle k='+str(neighbors)+' 2d embedding.npy', embedding, allow_pickle=False, fix_imports=False)
np.save(base + ' lle k='+str(neighbors)+' 2d errors.npy', errors, allow_pickle=False, fix_imports=False)

print("Done computing 2d embedding, starting 3d")

embedding, errors = locally_linear_embedding(X, n_neighbors=neighbors, n_components=3, n_jobs=-1)
np.save(base + ' lle k='+str(neighbors)+' 3d embedding.npy', embedding, allow_pickle=False, fix_imports=False)
np.save(base + ' lle k='+str(neighbors)+' 3d errors.npy', errors, allow_pickle=False, fix_imports=False)
