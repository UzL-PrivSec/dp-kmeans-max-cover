
# DP-KMeans-Max-Cover
Re-implementation of the differentially private clustering algorithm EMMC from 'Differentially Private K-Means Clustering via Exponential Mechanism and Max Cover'.

## Setup
Install **Python>=3.10** and download the required packages:
```bash
pip install -r requirements.txt
```
## Usage
EMMC can be used as follows:
```Python
from emmc import EMMC

emmc = EMMC()

# ------------- np.ndarray, shape=(k, num_dims)
# |
# v
centres = emmc.cluster(
    data=      # np.ndarray, shape=(num_points, num_dims)
    diameter=  # float, length of the space's diagonal
    k=         # int, number of cluster centres
    epsilon=   # float, epsilon > 0
    delta=     # float, delta < 1
)
```
In `demo.py` you can find a full example of how EMMC can be used to cluster a data set.

## Authors
The code is based on the pseudo-code in the [paper](https://ojs.aaai.org/index.php/AAAI/article/view/17099) 'Differentially Private K-Means Clustering via Exponential Mechanism and Max Cover'.

The implementation is a result of the master thesis of Anton Kosjakov (dev@kosjakov.de) and was modified by Johannes Liebenow (j.liebenow@uni-luebeck.de).



