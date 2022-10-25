import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.chdir("D:\\DevResults\\GitProjs\\github_PythonStudy\\2202Stat\\contents")
os.getcwd()

waiting_df = pd.read_csv('./6.13-14.csv', sep=',', header=None)
print(waiting_df)

waiting = waiting_df.values.flatten()
print(waiting[:-3])

waiting_df = pd.DataFrame(waiting)
print(waiting_df.describe())

plt.figure()
plt.boxplot(waiting)
plt.show()