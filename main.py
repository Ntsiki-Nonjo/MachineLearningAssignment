import pandas as pd
import numpy as np

data = pd.read_csv('data/adult.csv')
data = data[data['age'] == 17]
other, count = np.unique(data['class'], return_counts=True)
