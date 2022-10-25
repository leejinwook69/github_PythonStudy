import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

os.chdir("D:\\DevResults\\GitProjs\\github_PythonStudy\\2202Stat")
os.getcwd()

df = pd.read_csv('./2장-6-16.txt', sep = '\t', header=None)
print(df)



plt.figure()
n, bins, patches = plt.hist(df, bins = 12, facecolor="blue", alpha = 0.5)
print(n, bins)
x = [(bins[i]+bins[i+1])/2 for i in range(len(bins)-1)]   #도수다각형
w_bin = bins[1]-bins[0]   #도수다각형
x.insert(0,x[0]-w_bin)   #도수다각형
x.append(x[-1]+w_bin)   #도수다각형
n = np.insert(n,0,0.0)   #도수다각형
n = np.append(n,0.0)   #도수다각형
plt.xlabel('ozone')
plt.ylabel('Frequency')
plt.title("LA OZONE")
plt.plot(x,n,'blue',marker='o')   #도수다각형

plt.savefig('./plot/그림26.png')
plt.show()