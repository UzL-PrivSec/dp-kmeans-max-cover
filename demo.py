import numpy as np

from emmc import EMMC
from sklearn.datasets import make_blobs


num_clusters = 16
num_dims = 10
num_points = 10000

data, _ = make_blobs(
    num_points, num_dims, centers=num_clusters, center_box=(-100, 100), random_state=42
)

emmc = EMMC()

centres = emmc.cluster(
    data=data,
    diameter=np.sqrt(num_dims) * 100 * 2,
    k=16,
    epsilon=1.0,
    delta=1 / (np.sqrt(num_points) * num_points),
)

print(centres)
