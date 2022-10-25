import matplotlib.pyplot as plt
import numpy as np

import os
os.chdir("D:\\DevResults\\GitProjs\\github_PythonStudy\\2202Stat\\Practice")
os.getcwd()

import pandas as pd
score_df = pd.read_csv('./score.csv',sep=",")
print(score_df)


import numpy as np
print(np.corrcoef(score_df["math"],score_df["english"])[0][1])


#draw the scatter plot


import matplotlib.pyplot as plt

plt.figure()
plt.scatter(score_df["math"], score_df["english"], color ='black')
plt.xlabel('math(score)')
plt.ylabel('english(score)')
plt.title('math and english')
plt.show()
plt.savefig('./mathNenglish.png') # 그림 저장
