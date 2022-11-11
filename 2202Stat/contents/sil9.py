import numpy as np
from scipy.stats import norm
import math

m=[]
n=[]

for i in range(1000):
    m.append(np.random.poisson(lam = 3, size = 109))
    n.append(np.mean(m[i]))

m = np.array(m)
n=np.array(n)

# print(m)
# print(n)

# 이론적 : 표준편차 = 루트n
# 모분산이 9, 이론적 표준편차 : 루트3을 3으로 나눈다

print("x_bar, stdev , ideal stdev ", np.mean(n), np.std(n), math.sqrt(3)/3 )


# #히스토그램

import matplotlib.pyplot as plt
plt.hist(n, bins=9)
plt.xlabel('m')
plt.ylabel('Frequency')
plt.title('Historam of m')
plt.show()