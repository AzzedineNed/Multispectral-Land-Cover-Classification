


import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image
from tqdm import tqdm
from tqdm.notebook import tqdm
import seaborn as sns
import random

from sklearn.metrics import confusion_matrix
from sklearn import model_selection
from sklearn.model_selection import train_test_split

import torch
import torchvision.models as models
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset, random_split
from torchvision.transforms import transforms
from torchvision.utils import make_grid
import torch.nn.functional as F

import matplotlib

matplotlib.rcParams['axes.grid'] = False

# ## Config

# In[3]:


ROOT_PATH = 'C:/Users/aacer/PycharmProjects/PFE_IVA'
BASE_PATH = 'C:/Users/aacer/PycharmProjects/PFE_IVA/Dataset'
FULL_DATA_DF = os.path.join(ROOT_PATH, 'dataset_label.csv')

IDX_CLASS_LABELS = {
    0: 'AnnualCrop',
    1: 'Forest',
    2: 'HerbaceousVegetation',
    3: 'Highway',
    4: 'Industrial',
    5: 'Pasture',
    6: 'PermanentCrop',
    7: 'Residential',
    8: 'River',
    9: 'SeaLake'
}
CLASSES = ['AnnualCrop', 'Forest', 'HerbaceousVegetation', 'Highway', 'Industrial', 'Pasture', 'PermanentCrop',
           'Residential', 'River', 'SeaLake']
CLASS_IDX_LABELS = dict()
for key, val in IDX_CLASS_LABELS.items():
    CLASS_IDX_LABELS[val] = key

NUM_CLASSES = len(IDX_CLASS_LABELS.items())
torch.manual_seed(1021)







## Give idx of each class name
def encode_label(label):
    idx = CLASS_IDX_LABELS[label]
    return idx


## Take in idx and return the class name
def decode_target(target, text_labels=True):
    result = []
    if text_labels:
        return IDX_CLASS_LABELS[target]
    else:
        return target





## Example for decoding and encoding
print(encode_label('Forest'))
print(decode_target(1))
print(decode_target(2, text_labels=True))




print(f"Total number of images in the dataset: {len(os.listdir(BASE_PATH))}")





i = 0
DATA_DF = pd.DataFrame(columns=['image_id', 'label'])

# for (dirpath, dirname, filename) in walk(BASE_PATH):
#   for each_file in filename:

for each_file in os.listdir(BASE_PATH):
    DATA_DF.loc[i] = [each_file, each_file.split('_')[0]]
    i += 1
print(i)
DATA_DF.to_csv(FULL_DATA_DF, index=False)
DATA_DF.head()

# In[8]:


print(f"Uniques values for labels are...")
for ind, each in enumerate(DATA_DF.label.unique()):
    print(ind + 1, ":", each)

