import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import csv
#pd.set_option('display.max_rows', 500)
#pd.set_option('display.height', None)
df=pd.read_csv("Boston.csv")
print(df.head())

plt.show(block=sns.scatterplot(x="rm",y="medv",data=df))
print(df.shape)
"""
v=df[["rm","medv"]]
print(v.corr())
os.system("pause")
"""
