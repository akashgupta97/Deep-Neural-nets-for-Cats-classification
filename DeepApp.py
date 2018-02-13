
import time
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage
from dnn_app_utils_v2 import *


get_ipython().magic('matplotlib inline')
plt.rcParams['figure.figsize'] = (5.0, 4.0)  # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'


get_ipython().magic('load_ext autoreload')
get_ipython().magic('autoreload 2')

np.random.seed(1)

# ## 2 - Dataset

train_x_orig, train_y, test_x_orig, test_y, classes = load_data()

# The following code will show you an image in the dataset. Feel free to change the index and re-run the cell multiple times to see other images.

# In[6]:

# Example of a picture
index = 15
plt.imshow(train_x_orig[index])
print(train_x_orig.shape)
print("y = " + str(train_y[0, index]) + ". It's a " + classes[train_y[0, index]].decode("utf-8") + " picture.")
