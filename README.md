
# DP-KMeans-Max-Cover
Re-implementation of the differentially private clustering algorithm EMMC from 'Differentially Private K-Means Clustering via Exponential Mechanism and Max Cover'.

## Setup
Install **Python>=3.10** and download the required packages:
```bash
pip install -r requirements.txt
```
## Usage
DPM can be used as follows:
```Python
from emmc import EMMC

clusters = EMMC(
  TODO
)
```
In `demo.py` you can find a full example of how DPM can be used to cluster a data set.

## Authors
The code is based on the pseudo-code in the [paper](https://ojs.aaai.org/index.php/AAAI/article/view/17099) 'Differentially Private K-Means Clustering via Exponential Mechanism and Max Cover'.

The implementation was done by Anton Kosjakov (dev@kosjakov.de) and modified by Johannes Liebenow (j.liebenow@uni-luebeck.de).



