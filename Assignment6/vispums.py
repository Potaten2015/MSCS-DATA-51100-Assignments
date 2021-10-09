import numpy as np
import pandas as pd
from pprint import pprint
import matplotlib as plt

data = pd.read_csv('ss13hil.csv')

HHL = data['HHL']
unique_HHL, unique_HHL_count = np.unique(HHL, return_counts=True)
unique_HHL_filtered = 