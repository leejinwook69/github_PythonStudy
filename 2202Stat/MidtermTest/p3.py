#201811194 이진욱

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = np.array([162, 171, 138, 145, 144, 126, 145, 162, 174, 178, 167,
               98, 161, 152, 182, 136, 165, 137, 133, 143, 184, 166, 115, 115,
               95, 190, 119, 144, 176, 135, 194, 147, 160, 158, 178, 162, 131, 106, 157, 154])

# quantile
#상위 80 기준점수
per = np.percentile(df,[80])
print(per)



plt.figure()
plt.boxplot(df)
plt.show()

#1. 160쪽으로 약간 치우쳐진 박스플롯이다.
#2. 상위 80 기준점수는171.6 점이다.