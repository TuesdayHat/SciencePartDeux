import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')

x = dataset.iloc[:, :-1].values
# [:, ] => take all rows of dataset (left)
# [, :-1] => take all columns of dataset (-1 means skip the last column)(right)
# [row, column]
y = dataset.iloc[:, 3].values
# take only the index 3 column

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = "mean", axis = 0)
# commands for what to do when data is missing. 
# missing-values = what missing values will be called when it loads the data
# strategy = what to replace the missing data with. Defaults to mean
# axis = look along columns (0) or rows (1)

imputer = imputer.fit(x[:, 1:3])
# upper bound is excluded in python
x[:, 1:3] = imputer.transform(x[:, 1:3])
print(x)